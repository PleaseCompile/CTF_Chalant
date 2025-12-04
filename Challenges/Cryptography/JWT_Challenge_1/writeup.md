# The Three-Part Puzzle - Writeup

## 📚 พื้นฐานที่ต้องรู้ (สอนตั้งแต่ 0)

### Base64 คืออะไร?

Base64 เป็นวิธีการเข้ารหัสข้อมูล binary ให้เป็นข้อความที่อ่านได้ ใช้ตัวอักษร 64 ตัว:
- A-Z (26 ตัว)
- a-z (26 ตัว)  
- 0-9 (10 ตัว)
- + และ / (2 ตัว)
- = ใช้เป็น padding

### Base64URL คืออะไร?

Base64URL เป็นเวอร์ชันที่ปลอดภัยสำหรับ URL โดย:
- แทนที่ `+` ด้วย `-`
- แทนที่ `/` ด้วย `_`
- ไม่ใช้ `=` padding

### JWT (JSON Web Token) คืออะไร?

JWT เป็นมาตรฐานในการส่งข้อมูลระหว่างระบบอย่างปลอดภัย รูปแบบ:

```
xxxxx.yyyyy.zzzzz
```

ประกอบด้วย 3 ส่วน คั่นด้วยจุด (`.`):

1. **Header** - ข้อมูลประเภทและ algorithm
2. **Payload** - ข้อมูลที่ต้องการส่ง (claims)
3. **Signature** - ลายเซ็นดิจิทัล

⚠️ **สำคัญ**: Header และ Payload แค่ encode ด้วย Base64URL ไม่ได้เข้ารหัส!

---

## 🔍 วิธีแก้โจทย์ทีละขั้นตอน

### ขั้นตอนที่ 1: สังเกต Pattern

เมื่อดู data.txt จะเห็น:
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkhhY2tlciBIZXJvIiwiZmxhZyI6ImZsYWd7and0X2QzYzBkM19tNHN0M3J9IiwiaWF0IjoxNTE2MjM5MDIyfQ.abc123xyz789
```

สังเกต:
- มี 3 ส่วน คั่นด้วยจุด
- ตัวอักษรเป็น A-Z, a-z, 0-9 → น่าจะเป็น Base64
- โครงสร้างนี้เป็น JWT!

### ขั้นตอนที่ 2: แยกส่วน

```
Part 1 (Header): eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
Part 2 (Payload): eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkhhY2tlciBIZXJvIiwiZmxhZyI6ImZsYWd7and0X2QzYzBkM19tNHN0M3J9IiwiaWF0IjoxNTE2MjM5MDIyfQ
Part 3 (Signature): abc123xyz789
```

### ขั้นตอนที่ 3: Decode Part 2 (Payload)

ใช้ Base64 decode:

```python
import base64

payload = "eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkhhY2tlciBIZXJvIiwiZmxhZyI6ImZsYWd7and0X2QzYzBkM19tNHN0M3J9IiwiaWF0IjoxNTE2MjM5MDIyfQ"

# เพิ่ม padding
payload += '=' * (4 - len(payload) % 4)

# decode
result = base64.urlsafe_b64decode(payload)
print(result)
```

ผลลัพธ์:
```json
{
  "sub": "1234567890",
  "name": "Hacker Hero",
  "flag": "flag{jwt_d3c0d3_m4st3r}",
  "iat": 1516239022
}
```

### ขั้นตอนที่ 4: หา Flag

```
🚩 FLAG: flag{jwt_d3c0d3_m4st3r}
```

---

## 💻 วิธีแก้หลายแบบ

### วิธี 1: ใช้ jwt.io (ง่ายที่สุด!)

1. ไปที่ https://jwt.io
2. วาง token ลงในช่อง "Encoded"
3. ดูผลลัพธ์ในส่วน "PAYLOAD"

### วิธี 2: Python Script

```python
import base64
import json

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkhhY2tlciBIZXJvIiwiZmxhZyI6ImZsYWd7and0X2QzYzBkM19tNHN0M3J9IiwiaWF0IjoxNTE2MjM5MDIyfQ.abc123xyz789"

# แยกส่วน payload
payload_b64 = token.split('.')[1]

# เพิ่ม padding
payload_b64 += '=' * (4 - len(payload_b64) % 4)

# decode
payload = json.loads(base64.urlsafe_b64decode(payload_b64))
print(payload['flag'])
```

### วิธี 3: Command Line

```bash
echo "eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkhhY2tlciBIZXJvIiwiZmxhZyI6ImZsYWd7and0X2QzYzBkM19tNHN0M3J9IiwiaWF0IjoxNTE2MjM5MDIyfQ==" | base64 -d
```

### วิธี 4: CyberChef

1. ไปที่ https://gchq.github.io/CyberChef/
2. ลาก "From Base64" มาใส่ Recipe
3. วาง payload ลงใน Input

---

## 🎓 สิ่งที่ได้เรียนรู้

1. **JWT Structure** - เข้าใจโครงสร้าง 3 ส่วนของ JWT
2. **Base64URL** - การเข้ารหัสที่ปลอดภัยสำหรับ URL
3. **Security Awareness** - JWT payload ไม่ได้เข้ารหัส ใครก็อ่านได้!

---

## 🔐 Key Takeaways

| หัวข้อ | รายละเอียด |
|-------|-----------|
| Format | `header.payload.signature` |
| Encoding | Base64URL (ไม่ใช่การเข้ารหัส!) |
| Security | Payload อ่านได้โดยทุกคน |
| Tool | jwt.io ใช้ง่ายที่สุด |

---

## 📚 Further Learning

1. **JWT.io Introduction**: https://jwt.io/introduction
2. **RFC 7519 (JWT)**: https://datatracker.ietf.org/doc/html/rfc7519
3. **OWASP JWT Cheat Sheet**: https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html
4. **JWT Security Best Practices**: https://curity.io/resources/learn/jwt-best-practices/

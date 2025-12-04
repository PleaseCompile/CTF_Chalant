# 🔐 The Prime Minister's Secret - Writeup

## 📚 พื้นฐานที่ต้องรู้ (สอนตั้งแต่ 0)

### Prime Numbers คืออะไร?
**Prime Number (จำนวนเฉพาะ)** คือตัวเลขที่หารลงตัวได้เพียงแค่ 1 และตัวมันเอง

ตัวอย่าง:
- 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61...
- 4 ไม่ใช่ prime เพราะ 4 = 2 × 2
- 61 เป็น prime เพราะหารลงตัวได้แค่ 1 และ 61

### RSA คืออะไร?
**RSA** เป็นระบบเข้ารหัสที่ตั้งชื่อตามผู้คิดค้น 3 คน:
- **R**ivest
- **S**hamir
- **A**dleman

RSA เป็นการเข้ารหัสแบบ **Asymmetric** หมายความว่ามีกุญแจ 2 ตัว:
1. **Public Key** - ใช้เข้ารหัส (ใครก็ใช้ได้)
2. **Private Key** - ใช้ถอดรหัส (เจ้าของเท่านั้น)

### หลักการของ RSA

#### 1. การสร้างกุญแจ (Key Generation)
```
1. เลือก prime numbers 2 ตัว: p และ q
2. คำนวณ n = p × q (นี่คือส่วนหนึ่งของ public key)
3. คำนวณ φ(n) = (p-1) × (q-1) (Euler's totient function)
4. เลือก e ที่ gcd(e, φ(n)) = 1 (e เป็นส่วนหนึ่งของ public key)
5. คำนวณ d ที่ (e × d) mod φ(n) = 1 (d คือ private key)
```

#### 2. การเข้ารหัส (Encryption)
```
c = m^e mod n

โดยที่:
- m = ข้อความต้นฉบับ (message)
- e = public exponent
- n = modulus
- c = ciphertext (ข้อความที่เข้ารหัสแล้ว)
```

#### 3. การถอดรหัส (Decryption)
```
m = c^d mod n

โดยที่:
- c = ciphertext
- d = private exponent (private key)
- n = modulus
- m = ข้อความต้นฉบับ
```

---

## 🔍 วิธีแก้โจทย์ทีละขั้นตอน

### ขั้นตอนที่ 1: อ่านโจทย์และเข้าใจ
จาก story:
- นายกรัฐมนตรีใช้ "ตัวเลขพิเศษ" = **Prime Numbers**
- เขาคูณตัวเลข 2 ตัวเข้าด้วยกัน = **p × q = n**
- ถ้าใครรู้ 2 ตัวนี้ก็สามารถ "กลับ" กระบวนการได้ = **คำนวณ private key d**

### ขั้นตอนที่ 2: ดูข้อมูลใน data.txt
```python
p = 61       # Prime number ตัวที่ 1
q = 53       # Prime number ตัวที่ 2
n = 3233     # p × q
e = 17       # Public exponent

encrypted_message = [1369, 745, 1632, 2923, 855, ...]
```

### ขั้นตอนที่ 3: คำนวณ φ(n)
```python
φ(n) = (p-1) × (q-1)
φ(n) = (61-1) × (53-1)
φ(n) = 60 × 52
φ(n) = 3120
```

### ขั้นตอนที่ 4: คำนวณ Private Key (d)
เราต้องหา `d` ที่ทำให้:
```
(e × d) mod φ(n) = 1
(17 × d) mod 3120 = 1
```

นี่คือการหา **Modular Multiplicative Inverse**

วิธีคำนวณ (Extended Euclidean Algorithm):
```python
d = mod_inverse(17, 3120) = 2753
```

ตรวจสอบ: `(17 × 2753) mod 3120 = 46801 mod 3120 = 1` ✓

### ขั้นตอนที่ 5: ถอดรหัสแต่ละตัวเลข
```python
# สำหรับแต่ละ c ใน encrypted_message:
m = c^d mod n

# ตัวอย่าง: ถอดรหัสตัวแรก (1369)
m = 1369^2753 mod 3233
m = 102  # ซึ่งเป็น ASCII ของ 'f'
```

### ขั้นตอนที่ 6: แปลง ASCII เป็นตัวอักษร
```python
decrypted = []
for c in encrypted_message:
    m = pow(c, d, n)
    decrypted.append(chr(m))

flag = ''.join(decrypted)
# flag = "flag{rsa_pr1m3_p0w3r}"
```

---

## 💻 วิธีแก้หลายแบบ

### วิธีที่ 1: Python Script
```python
def mod_inverse(e, phi):
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd_val, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd_val, x, y
    
    _, x, _ = extended_gcd(e % phi, phi)
    return (x % phi + phi) % phi

# Given values
p, q, e = 61, 53, 17
n = p * q  # 3233
phi_n = (p - 1) * (q - 1)  # 3120
d = mod_inverse(e, phi_n)  # 2753

encrypted = [1369, 745, 1632, 2923, 855, 2412, 1230, 1632, 119, 612, 
             2412, 2906, 2271, 368, 119, 612, 624, 1107, 368, 2412, 1516]

flag = ''.join([chr(pow(c, d, n)) for c in encrypted])
print(flag)  # flag{rsa_pr1m3_p0w3r}
```

### วิธีที่ 2: ใช้ Online Tools

**dCode RSA Cipher** (https://www.dcode.fr/rsa-cipher)
1. ไปที่เว็บไซต์
2. เลือก "Decrypt"
3. ใส่ค่า:
   - N = 3233
   - E = 17
   - P = 61
   - Q = 53
4. ใส่ encrypted message
5. กด Decrypt

**CyberChef**
1. ใช้ "From Decimal" เพื่อแปลง
2. ใช้ RSA Decrypt recipe

### วิธีที่ 3: RsaCtfTool
```bash
# ติดตั้ง
git clone https://github.com/Ganapati/RsaCtfTool

# ใช้งาน
python3 RsaCtfTool.py -n 3233 -e 17 --uncipher [encrypted]
```

---

## 🎓 สิ่งที่ได้เรียนรู้

1. **RSA Basics**
   - RSA ใช้ prime numbers 2 ตัวในการสร้างกุญแจ
   - ความปลอดภัยอยู่บนความยากของการ factorize n

2. **Key Components**
   - p, q: Prime factors
   - n = p × q: Modulus
   - φ(n) = (p-1)(q-1): Euler's totient
   - e: Public exponent
   - d: Private exponent

3. **Mathematical Operations**
   - Modular exponentiation: `pow(base, exp, mod)`
   - Modular inverse: `d = e^(-1) mod φ(n)`

---

## 🔐 Key Takeaways

1. **ถ้ารู้ p และ q** → สามารถคำนวณ private key d ได้
2. **RSA ที่ปลอดภัย** ต้องใช้ prime ที่ใหญ่มาก (2048 bits ขึ้นไป)
3. **อย่าเปิดเผย p และ q** เพราะนั่นคือจุดอ่อนของ RSA

---

## 📚 Further Learning

1. **RSA Attacks**
   - Small e attack
   - Common modulus attack
   - Wiener's attack
   - Fermat's factorization

2. **Resources**
   - [RSA Wikipedia](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
   - [Crypto101](https://crypto101.io/)
   - [CryptoHack](https://cryptohack.org/)

---

## 🚩 Flag
```
flag{rsa_pr1m3_p0w3r}
```

---
*"The security of RSA relies on the difficulty of factoring large numbers. But if you have the factors... the secret is yours."*

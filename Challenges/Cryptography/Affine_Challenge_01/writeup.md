# 📜 สูตรลับแห่งปิทาโกรัส - Writeup

## 📚 พื้นฐานที่ต้องรู้ (สอนตั้งแต่ 0)

### Affine Cipher คืออะไร?

**Affine Cipher** เป็นการเข้ารหัสแบบแทนที่ (substitution cipher) ที่ใช้สูตรทางคณิตศาสตร์:

```
E(x) = (ax + b) mod m
```

โดยที่:
- `x` = ตำแหน่งของตัวอักษร (A=0, B=1, ..., Z=25)
- `a` = ค่าคงที่การคูณ (multiplier)
- `b` = ค่าคงที่การบวก (shift)
- `m` = จำนวนตัวอักษรในตารางแอลฟาเบต (26)

### เงื่อนไขสำคัญ

**ค่า `a` ต้อง coprime กับ `m`** หมายความว่า GCD(a, m) = 1

สำหรับ m = 26:
- ค่า a ที่ใช้ได้: **1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25** (12 ค่า)
- ค่า b: **0-25** (26 ค่า)
- รวม keys ทั้งหมด: **12 × 26 = 312 keys**

### การถอดรหัส

สูตรถอดรหัส:
```
D(y) = a⁻¹ × (y - b) mod m
```

โดย `a⁻¹` คือ **modular multiplicative inverse** ของ a

---

## 🔍 วิธีแก้โจทย์ทีละขั้นตอน

### ขั้นตอนที่ 1: วิเคราะห์โจทย์

จากโจทย์เราได้เบาะแส:
1. **"สูตรเชิงเส้น y = ax + b"** → บอกใบ้ว่าเป็น Affine cipher
2. **ตัวเลข 5 และ 8** → นี่คือค่า a และ b
3. **"a ต้องเป็นจำนวนที่ไม่มีตัวหารร่วมกับ 26"** → ยืนยันว่า a=5 เพราะ GCD(5,26)=1

### ขั้นตอนที่ 2: หา Modular Inverse ของ a

เราต้องหา `a⁻¹` ที่ทำให้:
```
(a × a⁻¹) mod 26 = 1
(5 × a⁻¹) mod 26 = 1
```

ลองทีละค่า:
```
5 × 1 = 5   mod 26 = 5  ❌
5 × 2 = 10  mod 26 = 10 ❌
5 × 3 = 15  mod 26 = 15 ❌
...
5 × 21 = 105 mod 26 = 1 ✅
```

ดังนั้น **a⁻¹ = 21**

### ขั้นตอนที่ 3: ถอดรหัส

สูตร: `D(y) = 21 × (y - 8) mod 26`

ถอดรหัสตัวอย่าง ตัวแรก "Z":
```
y = ord('Z') - ord('A') = 25
x = 21 × (25 - 8) mod 26
x = 21 × 17 mod 26
x = 357 mod 26
x = 19
ตัวอักษร = chr(19 + ord('A')) = 'T'
```

### ขั้นตอนที่ 4: ถอดรหัสทั้งหมด

```
Ciphertext: ZRCHLIMWUIVSWCVZQIZRUCSPCZ
Plaintext:  THEFLAGISANCIENTMATHSECRET
```

### ขั้นตอนที่ 5: สร้าง Flag

ข้อความ: `THEFLAGIS` + `ANCIENTMATHSECRET`

Flag content: `ANCIENT_MATH_SECRET` (เพิ่ม underscore ตามรูปแบบมาตรฐาน)

```python
import hashlib
flag_content = "ANCIENT_MATH_SECRET"
md5_hash = hashlib.md5(flag_content.encode()).hexdigest()
print(f"flag{{{md5_hash}}}")
```

**Flag: `flag{9d37a9d51f3eccaf63c460cf6bb94648}`**

---

## 💻 วิธีแก้หลายแบบ

### วิธี 1: ใช้ Python Script

```python
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def affine_decrypt(ciphertext, a, b):
    m = 26
    a_inv = mod_inverse(a, m)
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            y = ord(char.upper()) - ord('A')
            x = (a_inv * (y - b)) % m
            plaintext += chr(x + ord('A'))
    return plaintext

ciphertext = "ZRCHLIMWUIVSWCVZQIZRUCSPCZ"
print(affine_decrypt(ciphertext, 5, 8))
# Output: THEFLAGISANCIENTMATHSECRET
```

### วิธี 2: ใช้ CyberChef

1. ไปที่ https://gchq.github.io/CyberChef/
2. ค้นหา "Affine Cipher Decode"
3. ตั้งค่า: a=5, b=8
4. วาง ciphertext
5. ดูผลลัพธ์

### วิธี 3: ใช้ dCode

1. ไปที่ https://www.dcode.fr/affine-cipher
2. วาง ciphertext
3. เลือก "Decrypt with key A=5 B=8"
4. หรือใช้ "Automatic" ให้ bruteforce

### วิธี 4: Bruteforce

ถ้าไม่ทราบค่า a, b:

```python
from math import gcd

def bruteforce_affine(ciphertext):
    valid_a = [a for a in range(1, 26) if gcd(a, 26) == 1]
    for a in valid_a:
        for b in range(26):
            result = affine_decrypt(ciphertext, a, b)
            if "FLAG" in result or "THE" in result:
                print(f"a={a}, b={b}: {result}")
```

---

## 🎓 สิ่งที่ได้เรียนรู้

1. **Affine Cipher** - การเข้ารหัสแบบเชิงเส้น E(x) = ax + b mod m
2. **Modular Arithmetic** - การคำนวณแบบ modulo
3. **Modular Inverse** - การหาตัวผกผันในระบบ modular
4. **Coprime Numbers** - ตัวเลขที่มี GCD = 1
5. **Substitution Cipher** - การเข้ารหัสแบบแทนที่

---

## 🔐 Key Takeaways

| หัวข้อ | รายละเอียด |
|--------|------------|
| ประเภท | Monoalphabetic Substitution |
| สูตร | E(x) = (ax + b) mod 26 |
| Key Space | 312 keys (เล็กมาก) |
| จุดอ่อน | Bruteforce ได้ง่าย, Frequency Analysis |
| เครื่องมือ | CyberChef, dCode, Python |

---

## 📚 Further Learning

1. **Hill Cipher** - ใช้ matrix แทนที่จะเป็น linear function
2. **Playfair Cipher** - ใช้ digraphs
3. **Vigenère Cipher** - polyalphabetic substitution
4. **Frequency Analysis** - วิเคราะห์ความถี่ตัวอักษร

### แหล่งเรียนรู้เพิ่มเติม

- [CrypTool Online](https://www.cryptool.org/en/)
- [Crypto Corner](https://crypto.interactive-maths.com/)
- [Khan Academy - Cryptography](https://www.khanacademy.org/computing/computer-science/cryptography)

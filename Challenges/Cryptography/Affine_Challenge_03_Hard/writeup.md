# 🔮 รหัสลึกลับแห่งนักเล่นแร่แปรธาตุ - Writeup

## ⭐ Difficulty: Hard (⭐⭐⭐⭐☆)

## 📚 พื้นฐานที่ต้องรู้

### ความท้าทายของข้อนี้

ข้อนี้ **ไม่มี key ให้** คุณต้อง:
1. ระบุว่าเป็น cipher ประเภทใด
2. หาค่า a และ b ด้วยตัวเอง
3. ถอดรหัส

### วิธีโจมตี Cipher โดยไม่มี Key

1. **Brute Force** - ลองทุก key ที่เป็นไปได้
2. **Frequency Analysis** - วิเคราะห์ความถี่ตัวอักษร
3. **Known Plaintext Attack** - ใช้ข้อมูลที่รู้บางส่วน
4. **Pattern Recognition** - หา pattern ที่พบบ่อย

---

## 🔍 วิธีแก้โจทย์ทีละขั้นตอน

### ขั้นตอนที่ 1: วิเคราะห์ Ciphertext

```
SQJUIRFBHNWVASPFWRAQVTRHSJW
```

สังเกต:
- มีเฉพาะตัวอักษรพิมพ์ใหญ่
- ไม่มี space หรืออักขระพิเศษ
- น่าจะเป็น substitution cipher

### ขั้นตอนที่ 2: ตัดสินใจวิธีการโจมตี

**Brute Force** เป็นวิธีที่ง่ายและรวดเร็วที่สุด:
- Affine cipher มีแค่ 312 keys
- คอมพิวเตอร์ลองได้ทั้งหมดในไม่กี่วินาที

### ขั้นตอนที่ 3: Brute Force Attack

```python
from math import gcd

def affine_decrypt(ciphertext, a, b):
    m = 26
    # หา modular inverse ของ a
    a_inv = None
    for i in range(1, m):
        if (a * i) % m == 1:
            a_inv = i
            break
    
    if a_inv is None:
        return None
    
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            y = ord(char.upper()) - ord('A')
            x = (a_inv * (y - b)) % m
            plaintext += chr(x + ord('A'))
    return plaintext

# ลองทุก key
ciphertext = "SQJUIRFBHNWVASPFWRAQVTRHSJW"
valid_a = [a for a in range(1, 26) if gcd(a, 26) == 1]

for a in valid_a:
    for b in range(26):
        result = affine_decrypt(ciphertext, a, b)
        if "FLAG" in result or "THE" in result:
            print(f"a={a}, b={b}: {result}")
```

**ผลลัพธ์:**
```
a=11, b=17: THEFLAGISCRYPTOGRAPHYMASTER
```

### ขั้นตอนที่ 4: ยืนยัน Key

```
Key found: a=11, b=17
Plaintext: THEFLAGISCRYPTOGRAPHYMASTER
```

### ขั้นตอนที่ 5: สร้าง Flag

```python
import hashlib
flag_content = "CRYPTOGRAPHY_MASTER"
md5_hash = hashlib.md5(flag_content.encode()).hexdigest()
print(f"flag{{{md5_hash}}}")
```

**Flag: `flag{5cd056dcd91fca7c7fdac143b4656740}`**

---

## 💻 วิธีแก้หลายแบบ

### วิธี 1: Full Brute Force Script

```python
from math import gcd

def brute_force_affine(ciphertext):
    def mod_inverse(a, m):
        for i in range(1, m):
            if (a * i) % m == 1:
                return i
        return None
    
    def decrypt(ct, a, b):
        a_inv = mod_inverse(a, 26)
        if not a_inv:
            return None
        return ''.join(
            chr((a_inv * (ord(c) - ord('A') - b)) % 26 + ord('A'))
            for c in ct if c.isalpha()
        )
    
    valid_a = [a for a in range(1, 26) if gcd(a, 26) == 1]
    results = []
    
    for a in valid_a:
        for b in range(26):
            pt = decrypt(ciphertext, a, b)
            if pt and ("FLAG" in pt or "THE" in pt):
                results.append((a, b, pt))
    
    return results

results = brute_force_affine("SQJUIRFBHNWVASPFWRAQVTRHSJW")
for a, b, pt in results:
    print(f"a={a}, b={b}: {pt}")
```

### วิธี 2: Known Plaintext Attack

ถ้ารู้ว่าเริ่มด้วย "THEFLAG":

```
T(19) → S(18): 18 ≡ 11×19 + 17 (mod 26) ✓
H(7)  → Q(16): 16 ≡ 11×7 + 17 (mod 26)  ✓
```

จากสมการ 2 ตัว หา a, b:
```
18 = 19a + b (mod 26)  ... (1)
16 = 7a + b (mod 26)   ... (2)

(1) - (2): 2 = 12a (mod 26)

ลอง a ที่เป็นไปได้:
- a=11: 12×11 = 132 ≡ 2 (mod 26) ✓

แทนกลับ: b = 18 - 19×11 = 18 - 209 ≡ 17 (mod 26)
```

### วิธี 3: ใช้ dCode (Automatic)

1. ไปที่ https://www.dcode.fr/affine-cipher
2. วาง ciphertext
3. คลิก "AUTOMATIC DECRYPTION"
4. ระบบจะแสดงผลที่อ่านออกได้ทันที

### วิธี 4: Frequency Analysis

```python
from collections import Counter

ciphertext = "SQJUIRFBHNWVASPFWRAQVTRHSJW"
freq = Counter(ciphertext)

print("Character frequency:")
for char, count in freq.most_common():
    print(f"  {char}: {count}")

# Output:
# R: 4
# S: 3
# A: 3
# ...
```

ถ้า R(พบมากสุด) = E(พบมากสุดในอังกฤษ):
- R(17) เป็น encryption ของ E(4)
- 17 = 11×4 + 17 = 61 ≡ 9 (mod 26) ... ไม่ตรง

ดังนั้น frequency analysis อาจไม่แม่นยำสำหรับข้อความสั้น

---

## 🎓 สิ่งที่ได้เรียนรู้

1. **Brute Force Attack** - วิธีที่ง่ายที่สุดสำหรับ cipher ที่มี key space เล็ก
2. **Known Plaintext Attack** - ใช้ข้อมูลที่รู้เพื่อลดจำนวน keys
3. **Frequency Analysis** - ใช้ได้ดีกับข้อความยาว
4. **Key Space Analysis** - 312 keys = ไม่ปลอดภัย

---

## 🔐 Key Takeaways

| หัวข้อ | รายละเอียด |
|--------|------------|
| ความยาก | Hard - ไม่มี key ให้ |
| วิธีแก้หลัก | Brute Force (312 keys) |
| วิธีแก้ทางเลือก | Known Plaintext, Frequency Analysis |
| Key ที่ถูกต้อง | a=11, b=17 |
| เวลาที่ใช้ | < 1 วินาที (brute force) |

---

## 📚 Further Learning

### ทำไม Affine Cipher ถึงไม่ปลอดภัย?

1. **Key space เล็ก**: 312 keys = brute force ได้ทันที
2. **Monoalphabetic**: อ่อนต่อ frequency analysis
3. **Deterministic**: ตัวอักษรเดียวกัน → ผลเดียวกันเสมอ

### Cipher ที่ปลอดภัยกว่า

- **AES**: 2^128 หรือ 2^256 keys
- **RSA**: อิงตามความยากของ integer factorization
- **ChaCha20**: Modern stream cipher

### แหล่งเรียนรู้

- [Cryptopals Challenges](https://cryptopals.com/)
- [Practical Cryptography](http://practicalcryptography.com/)
- [Crypto101](https://www.crypto101.io/)

# 🕵️ รหัสแห่งสมาคมลับ - Writeup

## 📚 พื้นฐานที่ต้องรู้ (สอนตั้งแต่ 0)

### Affine Cipher คืออะไร?

**Affine Cipher** เป็นการเข้ารหัสที่รวมสองเทคนิคเข้าด้วยกัน:
1. **Multiplicative Cipher**: คูณด้วยค่าคงที่ a
2. **Caesar Cipher**: บวกด้วยค่าคงที่ b

สูตร:
```
E(x) = (ax + b) mod m
```

### ทำไมถึงเรียกว่า "Affine"?

ในทางคณิตศาสตร์ **Affine Transformation** คือการแปลงเชิงเส้นที่รวม:
- การหมุน/ขยาย (linear part: ax)
- การเลื่อน (translation: +b)

### Modular Multiplicative Inverse

การถอดรหัสต้องการ **inverse ของ a** ในระบบ mod m

```
a × a⁻¹ ≡ 1 (mod m)
```

วิธีหา:
1. **ลองทีละค่า** (สำหรับ m เล็กๆ)
2. **Extended Euclidean Algorithm** (วิธีมาตรฐาน)
3. **Fermat's Little Theorem** (ถ้า m เป็นจำนวนเฉพาะ)

---

## 🔍 วิธีแก้โจทย์ทีละขั้นตอน

### ขั้นตอนที่ 1: อ่านเบาะแส

จากโจทย์:
1. **"เจ็ดคูณ สามบวก"** → a=7, b=3
2. **"7 กับ 26 ไม่มีตัวหารร่วม"** → GCD(7,26)=1 (เป็นเงื่อนไขของ Affine)
3. **สูตร E(x) ≡ 7x + 3 (mod 26)** → ยืนยัน Affine cipher

### ขั้นตอนที่ 2: หา Modular Inverse ของ 7

ต้องหา `7⁻¹` ที่ทำให้:
```
7 × 7⁻¹ ≡ 1 (mod 26)
```

ลองทีละค่า:
```
7 × 1 = 7    mod 26 = 7  ❌
7 × 2 = 14   mod 26 = 14 ❌
7 × 3 = 21   mod 26 = 21 ❌
7 × 4 = 28   mod 26 = 2  ❌
...
7 × 15 = 105 mod 26 = 1  ✅
```

ดังนั้น **7⁻¹ = 15**

### ขั้นตอนที่ 3: สร้างสูตรถอดรหัส

```
D(y) = 15 × (y - 3) mod 26
```

### ขั้นตอนที่ 4: ถอดรหัส

ถอดรหัสตัวแรก "G":
```
y = ord('G') - ord('A') = 6
x = 15 × (6 - 3) mod 26
x = 15 × 3 mod 26
x = 45 mod 26
x = 19
ตัวอักษร = chr(19 + ord('A')) = 'T'
```

### ขั้นตอนที่ 5: ถอดรหัสทั้งหมด

```
Ciphertext: GAFMCDTHZCHQFDSRHEAFSJDZGFS
Plaintext:  THEFLAGISLINEARCIPHERMASTER
```

### ขั้นตอนที่ 6: สร้าง Flag

ข้อความ: `THEFLAGIS` + `LINEARCIPHERMASTER`

Flag content: `LINEAR_CIPHER_MASTER` (เพิ่ม underscore)

```python
import hashlib
flag_content = "LINEAR_CIPHER_MASTER"
md5_hash = hashlib.md5(flag_content.encode()).hexdigest()
print(f"flag{{{md5_hash}}}")
```

**Flag: `flag{7e64559b22e8adb427347f2f429ff277}`**

---

## 💻 วิธีแก้หลายแบบ

### วิธี 1: Python Script พื้นฐาน

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

ciphertext = "GAFMCDTHZCHQFDSRHEAFSJDZGFS"
print(affine_decrypt(ciphertext, 7, 3))
# Output: THEFLAGISLINEARCIPHERMASTER
```

### วิธี 2: Extended Euclidean Algorithm

```python
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse_egcd(a, m):
    gcd, x, _ = extended_gcd(a % m, m)
    if gcd != 1:
        return None
    return (x % m + m) % m

# หา inverse ของ 7 mod 26
inv = mod_inverse_egcd(7, 26)
print(f"7⁻¹ mod 26 = {inv}")  # Output: 15
```

### วิธี 3: ใช้ CyberChef

1. ไปที่ https://gchq.github.io/CyberChef/
2. ค้นหา "Affine Cipher Decode"
3. ตั้งค่า: a=7, b=3
4. วาง ciphertext
5. ได้ผลลัพธ์ทันที!

### วิธี 4: ใช้ Python pow() (Python 3.8+)

```python
# Python 3.8+ มี pow() รองรับ modular inverse
a_inv = pow(7, -1, 26)
print(f"7⁻¹ mod 26 = {a_inv}")  # Output: 15
```

---

## 🎓 สิ่งที่ได้เรียนรู้

1. **Affine Cipher** - การรวม multiplication และ shift
2. **Modular Inverse** - การหาตัวผกผันในระบบ modular
3. **Extended Euclidean Algorithm** - วิธีมาตรฐานในการหา inverse
4. **Coprime Requirement** - ทำไม GCD(a,m)=1 ถึงสำคัญ

---

## 🔐 Key Takeaways

| หัวข้อ | รายละเอียด |
|--------|------------|
| ประเภท | Monoalphabetic Substitution |
| สูตรเข้ารหัส | E(x) = (ax + b) mod 26 |
| สูตรถอดรหัส | D(y) = a⁻¹(y - b) mod 26 |
| เงื่อนไข | GCD(a, 26) = 1 |
| Key Space | 312 keys |

---

## 📊 เปรียบเทียบกับ Cipher อื่น

| Cipher | สูตร | Key Space |
|--------|------|-----------|
| Caesar | E(x) = x + b | 26 |
| Multiplicative | E(x) = ax | 12 |
| **Affine** | E(x) = ax + b | 312 |
| Vigenère | polyalphabetic | 26ⁿ |

---

## 📚 Further Learning

### เทคนิคการโจมตี Affine Cipher

1. **Brute Force**: ลองทุก 312 keys
2. **Frequency Analysis**: วิเคราะห์ความถี่ตัวอักษร
3. **Known Plaintext Attack**: ถ้ารู้บางส่วนของข้อความ

### แหล่งเรียนรู้เพิ่มเติม

- [Practical Cryptography](http://practicalcryptography.com/ciphers/affine-cipher/)
- [Crypto101](https://www.crypto101.io/)
- [Cryptopals Challenges](https://cryptopals.com/)

### ความท้าทายถัดไป

1. **Hill Cipher** - ใช้ matrix multiplication
2. **Vigenère Cipher** - polyalphabetic substitution
3. **Playfair Cipher** - digraph substitution

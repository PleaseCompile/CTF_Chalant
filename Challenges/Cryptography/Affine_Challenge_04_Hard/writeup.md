# 🎭 ประตูสองชั้นแห่งเงามืด - Writeup

## ⭐ Difficulty: Very Hard (⭐⭐⭐⭐⭐)

## 📚 พื้นฐานที่ต้องรู้

### Double Encryption คืออะไร?

**Double Encryption** คือการเข้ารหัสซ้ำ 2 ครั้งด้วย key คนละตัว:

```
Plaintext → [Encryption 1] → Intermediate → [Encryption 2] → Ciphertext
```

### ความท้าทายของข้อนี้

1. ข้อความถูกเข้ารหัส **2 ครั้ง**
2. ต้องถอดรหัส **ย้อนกลับ** (Gate 2 ก่อน, แล้ว Gate 1)
3. หรือต้องเข้าใจว่า **Double Affine = Single Affine**

---

## 🔍 วิธีแก้โจทย์ทีละขั้นตอน

### ขั้นตอนที่ 1: เข้าใจโจทย์

```
Ciphertext: WSRACHJBNIDFQCRCHPRERGMREW

Gate 1: E₁(x) = 5x + 8 (mod 26)
Gate 2: E₂(x) = 7x + 3 (mod 26)

Encryption process:
Plaintext → [5x+8] → Intermediate → [7x+3] → Ciphertext
```

### ขั้นตอนที่ 2: วิธี A - ถอดรหัสทีละชั้น

**สำคัญ: ต้องถอดย้อนกลับ!**
- Decrypt Gate 2 ก่อน (ชั้นนอก)
- แล้วค่อย Decrypt Gate 1 (ชั้นใน)

#### Step 2.1: หา Inverse ของแต่ละ key

```
Gate 2 (a=7): 7 × 15 ≡ 1 (mod 26) → a₂⁻¹ = 15
Gate 1 (a=5): 5 × 21 ≡ 1 (mod 26) → a₁⁻¹ = 21
```

#### Step 2.2: ถอดรหัส Gate 2

```
D₂(y) = 15 × (y - 3) mod 26

Ciphertext:  WSRACHJBNIDFQCRCHPRERGMREW
After D₂:    ZRCHLIMWUXAENLCLIYCPCTFCPZ
```

#### Step 2.3: ถอดรหัส Gate 1

```
D₁(y) = 21 × (y - 8) mod 26

Intermediate: ZRCHLIMWUXAENLCLIYCPCTFCPZ
After D₁:     THEFLAGISDOUBLELAYEREXPERT
```

### ขั้นตอนที่ 3: วิธี B - หา Combined Key

**ทฤษฎีสำคัญ: Double Affine = Single Affine**

```
E₂(E₁(x)) = a₂(a₁x + b₁) + b₂
          = (a₂·a₁)x + (a₂·b₁ + b₂)
```

**คำนวณ Combined Key:**
```
a_combined = (7 × 5) mod 26 = 35 mod 26 = 9
b_combined = (7 × 8 + 3) mod 26 = 59 mod 26 = 7
```

**ถอดรหัสครั้งเดียว:**
```
Combined key: a=9, b=7
9⁻¹ mod 26 = 3 (เพราะ 9×3 = 27 ≡ 1 mod 26)

D(y) = 3 × (y - 7) mod 26

Ciphertext: WSRACHJBNIDFQCRCHPRERGMREW
Plaintext:  THEFLAGISDOUBLELAYEREXPERT
```

### ขั้นตอนที่ 4: สร้าง Flag

```python
import hashlib
flag_content = "DOUBLE_LAYER_EXPERT"
md5_hash = hashlib.md5(flag_content.encode()).hexdigest()
print(f"flag{{{md5_hash}}}")
```

**Flag: `flag{886030e82cb2c2f24958896aef066e7a}`**

---

## 💻 Python Scripts

### วิธี A: ถอดทีละชั้น

```python
def mod_inverse(a, m=26):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def affine_decrypt(ciphertext, a, b):
    a_inv = mod_inverse(a)
    return ''.join(
        chr((a_inv * (ord(c) - ord('A') - b)) % 26 + ord('A'))
        for c in ciphertext if c.isalpha()
    )

ciphertext = "WSRACHJBNIDFQCRCHPRERGMREW"

# Step 1: Decrypt Gate 2 (a=7, b=3)
intermediate = affine_decrypt(ciphertext, 7, 3)
print(f"After Gate 2: {intermediate}")

# Step 2: Decrypt Gate 1 (a=5, b=8)
plaintext = affine_decrypt(intermediate, 5, 8)
print(f"Plaintext: {plaintext}")
```

### วิธี B: Combined Key

```python
ciphertext = "WSRACHJBNIDFQCRCHPRERGMREW"

# Calculate combined key
a1, b1 = 5, 8
a2, b2 = 7, 3

a_combined = (a2 * a1) % 26  # 35 % 26 = 9
b_combined = (a2 * b1 + b2) % 26  # 59 % 26 = 7

print(f"Combined key: a={a_combined}, b={b_combined}")

# Decrypt with combined key
plaintext = affine_decrypt(ciphertext, a_combined, b_combined)
print(f"Plaintext: {plaintext}")
```

---

## 🎓 สิ่งที่ได้เรียนรู้

### 1. Function Composition

```
(f ∘ g)(x) = f(g(x))

E₂ ∘ E₁ = E₂(E₁(x)) = (a₂a₁)x + (a₂b₁ + b₂)
```

### 2. Affine Group

Affine transformations ภายใต้ composition เป็น **Group**:
- **Closure**: E₂ ∘ E₁ ยังเป็น Affine
- **Identity**: E(x) = 1·x + 0
- **Inverse**: มี D(y) สำหรับทุก E(x)
- **Associativity**: (E₃ ∘ E₂) ∘ E₁ = E₃ ∘ (E₂ ∘ E₁)

### 3. Security Implication

**Double Affine ไม่ปลอดภัยกว่า Single Affine!**

เพราะ:
- n ครั้งของ Affine = 1 ครั้งของ Affine
- Key space ยังคง 312
- Brute force ยังง่าย

---

## 🔐 Key Takeaways

| หัวข้อ | รายละเอียด |
|--------|------------|
| ความยาก | Very Hard - Double encryption |
| Key 1 | a₁=5, b₁=8 |
| Key 2 | a₂=7, b₂=3 |
| Combined Key | a=9, b=7 |
| บทเรียน | Double Affine = Single Affine |

---

## 📊 เปรียบเทียบวิธีการ

| วิธี | ข้อดี | ข้อเสีย |
|------|-------|---------|
| ถอดทีละชั้น | เข้าใจง่าย, ตรวจสอบได้ทีละ step | ต้องถอด 2 ครั้ง |
| Combined Key | ถอดครั้งเดียว, เร็ว | ต้องคำนวณ key ก่อน |

---

## 📚 Further Learning

### Group Theory และ Cryptography

1. **Why this matters**: หลาย cipher ไม่มี closure property
2. **DES case**: 2DES ≠ DES แต่ก็ไม่ปลอดภัย (meet-in-the-middle attack)
3. **Triple DES**: ต้องใช้ EDE mode (Encrypt-Decrypt-Encrypt)

### Modern Cipher Composition

- **AES-CBC**: Chain multiple blocks
- **HMAC**: Nested hash functions
- **Hybrid encryption**: RSA + AES

### แหล่งเรียนรู้

- [Abstract Algebra in Cryptography](https://www.youtube.com/watch?v=BwQk_irPytk)
- [Group Theory Primer](https://en.wikipedia.org/wiki/Group_(mathematics))
- [Cryptopals Set 2](https://cryptopals.com/sets/2) - Block cipher attacks

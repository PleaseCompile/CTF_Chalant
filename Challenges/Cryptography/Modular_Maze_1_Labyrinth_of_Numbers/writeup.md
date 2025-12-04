# 🌀 The Labyrinth of Numbers - Writeup
# เขาวงกตแห่งตัวเลข - วิธีทำ

## 📚 พื้นฐานที่ต้องรู้ (สอนตั้งแต่ 0)

### 🔢 Modular Arithmetic คืออะไร?

**Modular Arithmetic** (เลขคณิตมอดุลาร์) คือการคำนวณที่เกี่ยวข้องกับ "เศษเหลือ" จากการหาร โดยมีคุณสมบัติพิเศษคือเมื่อค่าเกินขอบเขตที่กำหนด มันจะ "วนกลับ" มาเริ่มต้นใหม่

#### ตัวอย่างในชีวิตจริง:

1. **นาฬิกา (12 ชั่วโมง)**
   ```
   13:00 น. = 1:00 น.  (13 mod 12 = 1)
   14:00 น. = 2:00 น.  (14 mod 12 = 2)
   25:00 น. = 1:00 น.  (25 mod 12 = 1)
   ```

2. **วันในสัปดาห์**
   ```
   วันที่ 8 ของสัปดาห์ = วันที่ 1 (จันทร์)  (8 mod 7 = 1)
   ```

3. **เกมกระดาน**
   ```
   กระดาน 10 ช่อง: เดิน 12 ช่อง = อยู่ที่ช่อง 2  (12 mod 10 = 2)
   ```

### 📐 สูตรพื้นฐาน

```
a mod n = เศษเหลือจากการหาร a ด้วย n
```

**ตัวอย่าง:**
- `7 mod 5 = 2` (เพราะ 7 = 1×5 + **2**)
- `12 mod 5 = 2` (เพราะ 12 = 2×5 + **2**)
- `54 mod 5 = 4` (เพราะ 54 = 10×5 + **4**)

### 🗺️ การใช้ Modular กับ Grid/Maze

ในโจทย์นี้ เราใช้ตาราง 5x5:

```
    COL: 0   1   2   3   4
ROW:   +---+---+---+---+---+
  0    | A | B | C | D | E |
       +---+---+---+---+---+
  1    | F | G | H | I | J |
       +---+---+---+---+---+
  2    | K | L | M | N | O |
       +---+---+---+---+---+
  3    | P | Q | R | S | T |
       +---+---+---+---+---+
  4    | U | V | W | X | Y |
       +---+---+---+---+---+
```

เมื่อพิกัด (row, col) มีค่าเกิน 4 เราต้อง "wrap" ให้อยู่ในขอบเขต 0-4 โดยใช้:

```
actual_row = given_row mod 5
actual_col = given_col mod 5
```

---

## 🔍 วิธีแก้โจทย์ทีละขั้นตอน

### ขั้นตอนที่ 1: ทำความเข้าใจข้อมูลที่ให้มา

```
พิกัดที่เข้ารหัส:
1. (54, 27)
2. (18, 47)
3. (35, 25)
4. (53, 35)
5. (18, 30)
6. (45, 39)
7. (30, 53)
```

### ขั้นตอนที่ 2: คำนวณพิกัดจริงโดยใช้ mod 5

**ตัวอักษรที่ 1: (54, 27)**
```
row = 54 mod 5 = 4  (54 ÷ 5 = 10 เศษ 4)
col = 27 mod 5 = 2  (27 ÷ 5 = 5 เศษ 2)
ตำแหน่ง: (4, 2) → ตัวอักษร: W
```

**ตัวอักษรที่ 2: (18, 47)**
```
row = 18 mod 5 = 3  (18 ÷ 5 = 3 เศษ 3)
col = 47 mod 5 = 2  (47 ÷ 5 = 9 เศษ 2)
ตำแหน่ง: (3, 2) → ตัวอักษร: R
```

**ตัวอักษรที่ 3: (35, 25)**
```
row = 35 mod 5 = 0  (35 ÷ 5 = 7 เศษ 0)
col = 25 mod 5 = 0  (25 ÷ 5 = 5 เศษ 0)
ตำแหน่ง: (0, 0) → ตัวอักษร: A
```

**ตัวอักษรที่ 4: (53, 35)**
```
row = 53 mod 5 = 3  (53 ÷ 5 = 10 เศษ 3)
col = 35 mod 5 = 0  (35 ÷ 5 = 7 เศษ 0)
ตำแหน่ง: (3, 0) → ตัวอักษร: P
```

**ตัวอักษรที่ 5: (18, 30)**
```
row = 18 mod 5 = 3
col = 30 mod 5 = 0
ตำแหน่ง: (3, 0) → ตัวอักษร: P
```

**ตัวอักษรที่ 6: (45, 39)**
```
row = 45 mod 5 = 0  (45 ÷ 5 = 9 เศษ 0)
col = 39 mod 5 = 4  (39 ÷ 5 = 7 เศษ 4)
ตำแหน่ง: (0, 4) → ตัวอักษร: E
```

**ตัวอักษรที่ 7: (30, 53)**
```
row = 30 mod 5 = 0  (30 ÷ 5 = 6 เศษ 0)
col = 53 mod 5 = 3  (53 ÷ 5 = 10 เศษ 3)
ตำแหน่ง: (0, 3) → ตัวอักษร: D
```

### ขั้นตอนที่ 3: รวมตัวอักษร

```
W + R + A + P + P + E + D = "WRAPPED"
```

### ขั้นตอนที่ 4: สร้าง Flag

```
ข้อความ: WRAPPED (แปลงเป็นตัวพิมพ์เล็ก) = wrapped
MD5 hash: d6abaebf6f398d52a8b336bb018af0b8
Flag: flag{d6abaebf6f398d52a8b336bb018af0b8}
```

---

## 💻 วิธีแก้หลายแบบ

### วิธีที่ 1: คำนวณด้วยมือ (Manual)

ใช้เครื่องคิดเลขหรือคำนวณในใจ:
```
54 ÷ 5 = 10.8 → เศษ = 54 - (10 × 5) = 4
27 ÷ 5 = 5.4 → เศษ = 27 - (5 × 5) = 2
...และทำต่อไปทุกพิกัด
```

### วิธีที่ 2: Python Script

```python
# สร้างตาราง
grid = [
    ['A', 'B', 'C', 'D', 'E'],
    ['F', 'G', 'H', 'I', 'J'],
    ['K', 'L', 'M', 'N', 'O'],
    ['P', 'Q', 'R', 'S', 'T'],
    ['U', 'V', 'W', 'X', 'Y'],
]

# พิกัดที่เข้ารหัส
coordinates = [
    (54, 27), (18, 47), (35, 25), (53, 35),
    (18, 30), (45, 39), (30, 53)
]

# ถอดรหัส
result = ""
for row, col in coordinates:
    actual_row = row % 5
    actual_col = col % 5
    result += grid[actual_row][actual_col]

print(result)  # Output: WRAPPED
```

### วิธีที่ 3: One-liner Python

```python
# ใช้ ASCII: A=65, index = row*5 + col
coords = [(54,27),(18,47),(35,25),(53,35),(18,30),(45,39),(30,53)]
print(''.join(chr(65 + (r%5)*5 + (c%5)) for r,c in coords))
# Output: WRAPPED
```

### วิธีที่ 4: Google Sheets / Excel

1. สร้างตาราง lookup A-Y
2. ใช้สูตร `=MOD(row, 5)` และ `=MOD(col, 5)`
3. ใช้ `=INDEX(grid, row+1, col+1)` เพื่อหาตัวอักษร

### วิธีที่ 5: Online Tools

- **Modular Calculator**: https://www.calculator.net/modulo-calculator.html
- **Python Online**: https://www.python.org/shell/
- **CyberChef**: ใช้ "From Decimal" และคำนวณ mod

---

## 🎓 สิ่งที่ได้เรียนรู้

### 1. Modular Arithmetic Basics
- เข้าใจการทำงานของ mod operator
- รู้วิธี "wrap around" ค่าให้อยู่ในขอบเขต

### 2. Grid-based Cipher
- การแปลง coordinates เป็นตัวอักษร
- การใช้ตาราง 2 มิติในการเข้ารหัส

### 3. Pattern Recognition
- สังเกตเห็นว่าตัวเลขเกินขอบเขตตาราง
- เชื่อมโยงกับหลักการ "วนกลับ" เหมือนนาฬิกา

---

## 🔐 Key Takeaways

1. **Modular = วนรอบ**: เมื่อค่าเกินขอบเขต มันจะวนกลับมาเริ่มใหม่
2. **mod n**: หาเศษเหลือจากการหารด้วย n
3. **ขนาด Grid = Modulus**: Grid 5x5 ใช้ mod 5
4. **สังเกต Hints**: คำใบ้เกี่ยวกับ "wrap around", "clock", "boundaries" บอกให้ใช้ modular arithmetic

---

## 📚 Further Learning

### เครื่องมือและแหล่งเรียนรู้

1. **Khan Academy - Modular Arithmetic**
   - https://www.khanacademy.org/computing/computer-science/cryptography

2. **Wikipedia - Modular Arithmetic**
   - https://en.wikipedia.org/wiki/Modular_arithmetic

3. **Crypto101 - Cryptography Fundamentals**
   - https://www.crypto101.io/

### Ciphers ที่ใช้ Modular Arithmetic

1. **Caesar Cipher**: shift mod 26
2. **Vigenère Cipher**: multiple shifts mod 26
3. **Affine Cipher**: (ax + b) mod 26
4. **RSA**: (m^e) mod n

### CTF Resources

1. **PicoCTF**: https://picoctf.org/
2. **CryptoHack**: https://cryptohack.org/
3. **CTFtime**: https://ctftime.org/

---

## 🚩 Final Answer

```
Decoded Message: WRAPPED
Flag: flag{d6abaebf6f398d52a8b336bb018af0b8}
```

**ความหมาย**: "WRAPPED" สื่อถึงหลักการ "wrap around" ของ modular arithmetic ที่ใช้ในการแก้โจทย์นี้!

# The Grid of Secrets - Writeup

## 📚 พื้นฐานที่ต้องรู้ (สอนตั้งแต่ 0)

### Playfair Cipher คืออะไร?

Playfair Cipher เป็นเทคนิคการเข้ารหัสแบบ **polygraphic substitution cipher** ที่เข้ารหัสตัวอักษรทีละคู่ (digraphs) แทนที่จะเข้ารหัสทีละตัวเหมือน Caesar cipher

#### ประวัติโดยย่อ
- ถูกประดิษฐ์โดย **Charles Wheatstone** ในปี 1854
- แต่ถูกตั้งชื่อตาม **Lord Playfair** ที่ช่วยเผยแพร่
- ใช้งานจริงในสงครามโลกครั้งที่ 1 โดยกองทัพอังกฤษ

#### หลักการทำงาน

1. **สร้างตาราง 5x5** จาก keyword
2. **แบ่งข้อความเป็นคู่** (ถ้าตัวซ้ำหรือเลขคี่ ใส่ X คั่น)
3. **เข้ารหัสตามตำแหน่งในตาราง**

---

## 🔍 วิธีแก้โจทย์ทีละขั้นตอน

### ขั้นตอนที่ 1: อ่านโจทย์และหา Hints

จากโจทย์เราได้ข้อมูล:
- **Ciphertext**: `GATLMZCLRQXA`
- **Key**: `MONARCHY`
- Hints บอกว่า:
  - ตาราง 5x5
  - I และ J อยู่ด้วยกัน
  - ตัวอักษรจับคู่กัน
  - "playing fair" → **Playfair cipher**

### ขั้นตอนที่ 2: สร้างตาราง Playfair

สร้างตารางจาก key "MONARCHY":

1. เขียน key ก่อน: M O N A R C H Y
2. เติมตัวอักษรที่เหลือตามลำดับ (ไม่รวม J):

```
M O N A R
C H Y B D
E F G I K
L P Q S T
U V W X Z
```

### ขั้นตอนที่ 3: แบ่ง Ciphertext เป็นคู่

```
GATLMZCLRQXA → GA TL MZ CL RQ XA
```

### ขั้นตอนที่ 4: ถอดรหัสแต่ละคู่

กฎการถอดรหัส:
- **แถวเดียวกัน**: เลื่อนซ้าย 1 ช่อง
- **คอลัมน์เดียวกัน**: เลื่อนขึ้น 1 ช่อง
- **ต่างแถวต่างคอลัมน์**: วาดสี่เหลี่ยม แล้วสลับมุม

| คู่ | ตำแหน่ง | กฎ | ผลลัพธ์ |
|-----|---------|-----|---------|
| GA | G(2,2) A(0,3) | Rectangle | IN |
| TL | T(3,4) L(3,0) | Same Row | ST |
| MZ | M(0,0) Z(4,4) | Rectangle | RU |
| CL | C(1,0) L(3,0) | Same Column | ME |
| RQ | R(0,4) Q(3,2) | Rectangle | NT |
| XA | X(4,3) A(0,3) | Same Column | SX |

### ขั้นตอนที่ 5: รวมผลลัพธ์

```
IN + ST + RU + ME + NT + SX = INSTRUMENTSX
```

ลบ X ที่เป็น padding:
```
INSTRUMENTS
```

### ขั้นตอนที่ 6: สร้าง Flag

```
flag{instruments}
```

---

## 💻 วิธีแก้หลายแบบ

### วิธีที่ 1: ทำด้วยมือ (Manual)

1. วาดตาราง 5x5 บนกระดาษ
2. แบ่ง ciphertext เป็นคู่
3. หาตำแหน่งแต่ละคู่ในตาราง
4. ใช้กฎถอดรหัส
5. รวมผลลัพธ์

### วิธีที่ 2: ใช้ Python Script

```python
def create_playfair_matrix(key):
    key = key.upper().replace('J', 'I')
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    
    matrix = []
    used = set()
    
    for char in key:
        if char not in used and char in alphabet:
            matrix.append(char)
            used.add(char)
    
    for char in alphabet:
        if char not in used:
            matrix.append(char)
    
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    char = char.upper().replace('J', 'I')
    for i, row in enumerate(matrix):
        for j, c in enumerate(row):
            if c == char:
                return (i, j)
    return None

def decrypt_playfair(ciphertext, key):
    matrix = create_playfair_matrix(key)
    ciphertext = ''.join(c for c in ciphertext.upper() if c.isalpha())
    
    plaintext = ''
    for i in range(0, len(ciphertext), 2):
        c1, c2 = ciphertext[i], ciphertext[i+1]
        r1, col1 = find_position(matrix, c1)
        r2, col2 = find_position(matrix, c2)
        
        if r1 == r2:
            plaintext += matrix[r1][(col1-1)%5] + matrix[r2][(col2-1)%5]
        elif col1 == col2:
            plaintext += matrix[(r1-1)%5][col1] + matrix[(r2-1)%5][col2]
        else:
            plaintext += matrix[r1][col2] + matrix[r2][col1]
    
    return plaintext

# ใช้งาน
result = decrypt_playfair("GATLMZCLRQXA", "MONARCHY")
print(result)  # INSTRUMENTSX
print(f"flag{{{result.replace('X','').lower()}}}")  # flag{instruments}
```

### วิธีที่ 3: ใช้เครื่องมือออนไลน์

**CyberChef:**
1. ไปที่ https://gchq.github.io/CyberChef/
2. ค้นหา "Playfair" ใน Operations
3. ลาก Playfair มาที่ Recipe
4. ใส่ Key: `MONARCHY`
5. ใส่ Input: `GATLMZCLRQXA`
6. ดูผลลัพธ์

**dCode:**
1. ไปที่ https://www.dcode.fr/playfair-cipher
2. ใส่ ciphertext และ key
3. กด Decrypt

---

## 🎓 สิ่งที่ได้เรียนรู้

1. **Playfair Cipher** เป็น polygraphic cipher ที่เข้ารหัสทีละคู่
2. การสร้าง **5x5 Matrix** จาก keyword
3. กฎการเข้ารหัส/ถอดรหัส 3 แบบ:
   - Same Row → Shift Right/Left
   - Same Column → Shift Down/Up
   - Rectangle → Swap Columns
4. **I และ J** ใช้ช่องเดียวกันใน Playfair
5. **X** ใช้เป็น padding สำหรับตัวซ้ำหรือเลขคี่

---

## 🔐 Key Takeaways

| หัวข้อ | รายละเอียด |
|--------|------------|
| ประเภท Cipher | Polygraphic Substitution |
| ขนาดตาราง | 5x5 (25 ตัวอักษร) |
| การจัดการ J | รวมกับ I |
| การจับคู่ | ทีละ 2 ตัวอักษร |
| Padding | ใช้ X |

---

## 📚 Further Learning

1. **Playfair Variants:**
   - Two-square cipher
   - Four-square cipher
   
2. **Breaking Playfair:**
   - Frequency analysis ของ digraphs
   - Known-plaintext attack
   
3. **Modern Applications:**
   - เรียนรู้ AES ที่ใช้ matrix operations คล้ายกัน
   - ศึกษา Hill cipher (ใช้ matrix multiplication)

---

## 🚩 Flag

```
flag{instruments}
```

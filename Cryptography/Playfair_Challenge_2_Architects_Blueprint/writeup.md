# The Architect's Blueprint - Writeup

## 📚 พื้นฐานที่ต้องรู้ (สอนตั้งแต่ 0)

### Playfair Cipher คืออะไร?

Playfair Cipher เป็นเทคนิคการเข้ารหัสแบบ **polygraphic substitution cipher** ที่เข้ารหัสตัวอักษรทีละคู่ (digraphs)

#### สิ่งที่ Challenge นี้เพิ่มเติมจาก Challenge 1
- **ต้องค้นหา Key เอง** จาก hints ใน story
- **การวิเคราะห์ข้อมูล** จากบริบทของเรื่องราว
- ทักษะการ **สกัดข้อมูล** จากข้อความ

---

## 🔍 วิธีแก้โจทย์ทีละขั้นตอน

### ขั้นตอนที่ 1: อ่านและวิเคราะห์ Story

จาก Story เราพบข้อมูลสำคัญ:

1. **"Sir Charles W."** → อาจหมายถึง Charles Wheatstone ผู้ประดิษฐ์ Playfair cipher
2. **"รากฐาน 5x5"** → ตาราง 5 แถว 5 คอลัมน์
3. **"กุญแจอยู่ในชื่ออาคาร"** → Key มาจากชื่ออาคาร
4. **"KINGDOM HALL"** → ชื่ออาคารที่เขารักที่สุด
5. **"เล่นให้ยุติธรรม"** → Play Fair = Playfair cipher

### ขั้นตอนที่ 2: สกัด Key จากชื่ออาคาร

```
KINGDOM HALL
↓ ลบช่องว่าง
KINGDOMHALL
↓ ลบตัวซ้ำ (L ซ้ำ)
KINGDOMHAL
```

**Key = KINGDOMHAL**

### ขั้นตอนที่ 3: สร้างตาราง Playfair

สร้างตารางจาก key "KINGDOMHAL":

1. เขียน key ก่อน: K I N G D O M H A L
2. เติมตัวอักษรที่เหลือตามลำดับ (ไม่รวม J):

```
K I N G D
O M H A L
B C E F P
Q R S T U
V W X Y Z
```

### ขั้นตอนที่ 4: แบ่ง Ciphertext เป็นคู่

```
MNNZNPGSSQSA → MN NZ NP GS SQ SA
```

### ขั้นตอนที่ 5: ถอดรหัสแต่ละคู่

กฎการถอดรหัส:
- **แถวเดียวกัน**: เลื่อนซ้าย 1 ช่อง
- **คอลัมน์เดียวกัน**: เลื่อนขึ้น 1 ช่อง
- **ต่างแถวต่างคอลัมน์**: วาดสี่เหลี่ยม แล้วสลับมุม

| คู่ | ตำแหน่ง | กฎ | ผลลัพธ์ |
|-----|---------|-----|---------|
| MN | M(1,1) N(0,2) | Rectangle | HI |
| NZ | N(0,2) Z(4,4) | Rectangle | DX |
| NP | N(0,2) P(2,4) | Rectangle | DE |
| GS | G(0,3) S(3,2) | Rectangle | NT |
| SQ | S(3,2) Q(3,0) | Same Row | RU |
| SA | S(3,2) A(1,3) | Rectangle | TH |

### ขั้นตอนที่ 6: รวมผลลัพธ์

```
HI + DX + DE + NT + RU + TH = HIDXDENTRUTH
```

ลบ X ที่เป็น padding:
```
HIDDENTRUTH
```

### ขั้นตอนที่ 7: สร้าง Flag

```
flag{hiddentruth}
```

---

## 💻 วิธีแก้หลายแบบ

### วิธีที่ 1: ทำด้วยมือ (Manual)

1. อ่าน story หา hints เกี่ยวกับ key
2. สกัด key จากชื่ออาคาร "KINGDOM HALL"
3. วาดตาราง 5x5 บนกระดาษ
4. แบ่ง ciphertext เป็นคู่
5. หาตำแหน่งแต่ละคู่ในตาราง
6. ใช้กฎถอดรหัส
7. รวมผลลัพธ์และลบ X

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

def extract_key(building_name):
    name = building_name.upper().replace(' ', '').replace('J', 'I')
    key = ''
    used = set()
    for char in name:
        if char.isalpha() and char not in used:
            key += char
            used.add(char)
    return key

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
key = extract_key("KINGDOM HALL")  # -> KINGDOMHAL
result = decrypt_playfair("MNNZNPGSSQSA", key)
print(result)  # HIDXDENTRUTH
print(f"flag{{{result.replace('X','').lower()}}}")  # flag{hiddentruth}
```

### วิธีที่ 3: ใช้เครื่องมือออนไลน์

**CyberChef:**
1. ไปที่ https://gchq.github.io/CyberChef/
2. ค้นหา "Playfair" ใน Operations
3. ลาก Playfair มาที่ Recipe
4. ใส่ Key: `KINGDOMHAL`
5. ใส่ Input: `MNNZNPGSSQSA`
6. ดูผลลัพธ์

**dCode:**
1. ไปที่ https://www.dcode.fr/playfair-cipher
2. ใส่ ciphertext: `MNNZNPGSSQSA`
3. ใส่ key: `KINGDOMHAL`
4. กด Decrypt

---

## 🎓 สิ่งที่ได้เรียนรู้

1. **การวิเคราะห์ Story** เพื่อหา hints
2. **การสกัด Key** จากข้อมูลที่ให้มา
3. **การจัดการกับตัวอักษรซ้ำ** ใน key
4. **ความเข้าใจลึกซึ้งขึ้น** เกี่ยวกับ Playfair cipher
5. **ทักษะการตีความ** คำใบ้แบบอ้อม

---

## 🔐 Key Takeaways

| หัวข้อ | รายละเอียด |
|--------|------------|
| Key Discovery | สกัดจาก "KINGDOM HALL" → KINGDOMHAL |
| ลบตัวซ้ำ | L ซ้ำใน HALL → เหลือ L ตัวเดียว |
| Hint สำคัญ | "Play Fair" = Playfair cipher |
| Charles W. | Charles Wheatstone - ผู้ประดิษฐ์ |

---

## 📊 เปรียบเทียบกับ Challenge 1

| หัวข้อ | Challenge 1 | Challenge 2 |
|--------|-------------|-------------|
| Key | ให้มาตรงๆ | ต้องหาเอง |
| ความซับซ้อน | ถอดรหัสอย่างเดียว | หา key + ถอดรหัส |
| Theme | สายลับ | สถาปนิก |
| Answer | INSTRUMENTS | HIDDENTRUTH |
| Flag | flag{instruments} | flag{hiddentruth} |

---

## 📚 Further Learning

1. **Key Management:**
   - วิธีการซ่อน key ในรูปแบบต่างๆ
   - ความปลอดภัยของ key
   
2. **Advanced Cryptanalysis:**
   - การโจมตี Playfair โดยไม่รู้ key
   - Frequency analysis ของ digraphs
   
3. **Historical Context:**
   - การใช้งานจริงในสงคราม
   - วิวัฒนาการของ cipher

---

## 🚩 Flag

```
flag{hiddentruth}
```

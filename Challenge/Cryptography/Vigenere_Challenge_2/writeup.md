# The Composer's Code - Writeup
# รหัสของนักประพันธ์เพลง - คำเฉลยละเอียด

---

## 📚 พื้นฐานที่ต้องรู้ (สอนตั้งแต่ 0)

### Vigenère Cipher คืออะไร?

**Vigenère Cipher** เป็นวิธีการเข้ารหัสที่ใช้ "คีย์" เป็นคำ โดยแต่ละตัวอักษรในคีย์จะกำหนดว่าต้องเลื่อนตัวอักษร plaintext ไปเท่าไหร่

#### หลักการง่ายๆ

```
A = 0, B = 1, C = 2, ... Z = 25

การเข้ารหัส: (ตัวอักษร plaintext + ตัวอักษร key) mod 26
การถอดรหัส: (ตัวอักษร ciphertext - ตัวอักษร key) mod 26
```

#### ตัวอย่าง

ถ้า Key = `MAMMAMIA`:
- M = 12, A = 0, M = 12, M = 12, A = 0, M = 12, I = 8, A = 0

```
Plaintext:  T  H  E  M  U  S  I  C
Key:        M  A  M  M  A  M  I  A
Shift:      12 0  12 12 0  12 8  0
Ciphertext: F  H  Q  Y  U  E  Q  C
```

---

## 🔍 วิเคราะห์โจทย์

### ข้อสังเกตจากโจทย์

1. **"Key" และ "เปียโน"** - บอกใบ้ว่าใช้ "คีย์" ในการเข้ารหัส
2. **"คำที่วนซ้ำเหมือน motif"** - Key เป็นคำที่ถูกใช้ซ้ำ
3. **"C, D, E, F, G, A, B"** - โน้ตดนตรี ≈ ตัวอักษร A-Z
4. **"ABBA's greatest hit"** - hint สำหรับ key

### หา Key

จาก hint "เพลงดังของ ABBA":
- "Mamma Mia!" เป็นหนึ่งในเพลงดังที่สุดของ ABBA ✅
- Key = **MAMMAMIA** (ตัวพิมพ์ใหญ่ ไม่มีเว้นวรรคหรือเครื่องหมาย)

---

## 💻 วิธีแก้โจทย์ทีละขั้นตอน

### ขั้นตอนที่ 1: อ่านข้อมูล

```
FHQ YUEQC EPQMKE EHQN IARPA FMIX. QVQZY ZOFQ HMA A BUDBOEM. LUSFQN OIRQFGXLK BO FHQ YEXWDK. fxmg{b0ty4xpt4n3t1o_u4sf3r}
```

### ขั้นตอนที่ 2: ระบุประเภทการเข้ารหัส

จาก story เราสังเกตได้ว่า:
- มีการพูดถึง "key" ที่เป็นคำ
- มีการพูดถึง "คำที่วนซ้ำ"
- ตัวอักษรแต่ละตัวถูกเลื่อนต่างกัน

**สรุป:** น่าจะเป็น **Vigenère Cipher**

### ขั้นตอนที่ 3: หา Key

ลองเพลงดังของ ABBA:
- "Dancing Queen" → DANCINGQUEEN ❌
- "Mamma Mia!" → MAMMAMIA ✅
- "Fernando" → FERNANDO ❌
- "Waterloo" → WATERLOO ❌

### ขั้นตอนที่ 4: ถอดรหัส

#### วิธี A: ใช้ CyberChef

1. ไปที่ https://gchq.github.io/CyberChef/
2. ค้นหา "Vigenère Decode"
3. ใส่ Key: `MAMMAMIA`
4. วาง ciphertext
5. ดูผลลัพธ์

#### วิธี B: ใช้ Python

```python
def vigenere_decrypt(ciphertext, key):
    result = []
    key = key.upper()
    key_index = 0
    
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            if char.isupper():
                decrypted = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            result.append(decrypted)
            key_index += 1
        else:
            result.append(char)
    
    return ''.join(result)

ciphertext = "FHQ YUEQC EPQMKE EHQN IARPA FMIX. QVQZY ZOFQ HMA A BUDBOEM. LUSFQN OIRQFGXLK BO FHQ YEXWDK. fxmg{b0ty4xpt4n3t1o_u4sf3r}"
key = "MAMMAMIA"
print(vigenere_decrypt(ciphertext, key))
```

### ขั้นตอนที่ 5: อ่านผลลัพธ์

```
THE MUSIC SPEAKS WHEN WORDS FAIL. EVERY NOTE HAS A PURPOSE. LISTEN CAREFULLY TO THE MELODY. flag{p0ly4lph4b3t1c_m4st3r}
```

---

## 🚩 Flag

```
flag{p0ly4lph4b3t1c_m4st3r}
```

---

## 🎓 สิ่งที่ได้เรียนรู้

1. **Vigenère Cipher** ใช้ key เป็นคำที่วนซ้ำ
2. **Metaphor** ใน story ช่วยบอกใบ้ประเภท cipher (key ในดนตรี = key ใน crypto)
3. **Pop culture references** อาจเป็น hint สำหรับ key (เพลง ABBA)
4. การ **brute force** ด้วยคำที่เป็นไปได้สามารถใช้เมื่อรู้ context

---

## 🔐 Key Takeaways

- **สังเกต metaphor** - นักออกแบบโจทย์มักใช้ metaphor เพื่อบอกใบ้
- **รู้จัก pop culture** - ชื่อเพลง, หนัง, หนังสือ อาจเป็น key
- **ลองหลายๆ ตัว** - ถ้ารู้ว่า key มาจากกลุ่มคำไหน ให้ลองทีละตัว

---

## 📚 Further Learning

### แหล่งเรียนรู้เพิ่มเติม

1. **Wikipedia:** [Vigenère cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)
2. **CyberChef:** [Online Tool](https://gchq.github.io/CyberChef/)
3. **dCode:** [Vigenère Decoder](https://www.dcode.fr/vigenere-cipher)

### เทคนิคเพิ่มเติม

- ถ้าไม่รู้ key เลย ลองใช้ **Kasiski Examination** หาความยาว key
- ใช้ **Index of Coincidence** เพื่อยืนยันความยาว key
- dCode.fr มี **auto-decode** ที่ลองหา key ให้อัตโนมัติ

---

## 🧩 เปรียบเทียบกับ Challenge 1

| Challenge 1 | Challenge 2 |
|-------------|-------------|
| ธีม: ทูตฝรั่งเศส (Historical) | ธีม: นักประพันธ์เพลง (Music) |
| Key: BOURBON (ราชวงศ์) | Key: MAMMAMIA (ชื่อเพลง) |
| Hint: ชื่อ Blaise + ฝรั่งเศส | Hint: Key + motif + ABBA |
| เหมาะกับคนชอบประวัติศาสตร์ | เหมาะกับคนชอบ pop culture |

ทั้งสองข้อใช้ **Vigenère Cipher** แต่มี approach ในการหา key ต่างกัน!

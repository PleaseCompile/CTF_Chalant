# The Diplomat's Secret - Writeup
# ความลับของทูต - คำเฉลยละเอียด

---

## 📚 พื้นฐานที่ต้องรู้ (สอนตั้งแต่ 0)

### Vigenère Cipher คืออะไร?

**Vigenère Cipher** เป็นวิธีการเข้ารหัสแบบ **Polyalphabetic Substitution** ซึ่งหมายความว่าตัวอักษรเดียวกันอาจถูกเข้ารหัสเป็นตัวอักษรต่างกันได้ ขึ้นอยู่กับตำแหน่งของมัน

#### เปรียบเทียบกับ Caesar Cipher

| Caesar Cipher | Vigenère Cipher |
|---------------|-----------------|
| เลื่อนทุกตัวอักษรเท่ากัน | เลื่อนแต่ละตัวอักษรต่างกัน |
| ใช้ตัวเลขเป็น key (เช่น 3) | ใช้คำเป็น key (เช่น "KEY") |
| ง่ายต่อการ crack | ยากกว่า แต่ยังไม่ปลอดภัย |

#### หลักการทำงาน

1. **เลือก Key:** เช่น `BOURBON`
2. **วน Key ซ้ำ:** ให้มีความยาวเท่ากับข้อความ
3. **เข้ารหัส:** แต่ละตัวอักษรถูกเลื่อนตามค่าของ key

```
Plaintext:  T  R  U  S  T  N  O  O  N  E
Key:        B  O  U  R  B  O  N  B  O  U
Shift:      1  14 20 17 1  14 13 1  14 20
Ciphertext: U  F  O  J  U  B  B  P  B  Y
```

#### ตาราง Vigenère

```
    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
A   A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
B   B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
C   C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
...
```

---

## 🔍 วิเคราะห์โจทย์

### ข้อสังเกตจากโจทย์

1. **ชื่อ "Blaise"** - นักเข้ารหัสชื่อดังชาวฝรั่งเศสคือ **Blaise de Vigenère**
2. **"le chiffre indéchiffrable"** - ชื่อเล่นของ Vigenère cipher
3. **"คำสำคัญที่ถูกใช้ซ้ำ"** - บ่งบอกว่าใช้ key แบบวนซ้ำ
4. **"แต่ละตัวอักษรถูกเลื่อนไปตามค่าของกุญแจ"** - หลักการของ Vigenère
5. **"ราชวงศ์ที่ยิ่งใหญ่ในยุโรป"** - hint สำหรับ key

### หา Key

จาก hint "ราชวงศ์ที่ยิ่งใหญ่ในยุโรป" + บริบทฝรั่งเศส:
- **BOURBON** - ราชวงศ์บูร์บงของฝรั่งเศส ✅
- HABSBURG - ราชวงศ์ออสเตรีย
- TUDOR - ราชวงศ์อังกฤษ

---

## 💻 วิธีแก้โจทย์ทีละขั้นตอน

### ขั้นตอนที่ 1: อ่านข้อมูล

```
UFOJU BB PBY ZO HUF DUCBQR UCHZHVG. UVY JFQEFH GLTH FUOS ZO TEBBWV. UVR GZUX JG EFJYRMSQ. gzux{w1u3a3s3_q1jy3s_1g_pm4gm1t}
```

### ขั้นตอนที่ 2: ระบุประเภทการเข้ารหัส

จาก story เราสังเกตได้ว่า:
- มีการกล่าวถึง Blaise (ผู้คิดค้น Vigenère)
- มีการพูดถึง "key ที่วนซ้ำ"
- เป็น polyalphabetic (ไม่ใช่ Caesar ธรรมดา)

**สรุป:** น่าจะเป็น **Vigenère Cipher**

### ขั้นตอนที่ 3: หา Key

จาก hint:
- "ราชวงศ์ที่ยิ่งใหญ่ในยุโรป" + บริบทฝรั่งเศส
- ลอง: **BOURBON**

### ขั้นตอนที่ 4: ถอดรหัส

#### วิธี A: ใช้ CyberChef

1. ไปที่ https://gchq.github.io/CyberChef/
2. ค้นหา "Vigenère Decode"
3. ใส่ Key: `BOURBON`
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

ciphertext = "UFOJU BB PBY ZO HUF DUCBQR UCHZHVG. UVY JFQEFH GLTH FUOS ZO TEBBWV. UVR GZUX JG EFJYRMSQ. gzux{w1u3a3s3_q1jy3s_1g_pm4gm1t}"
key = "BOURBON"
print(vigenere_decrypt(ciphertext, key))
```

### ขั้นตอนที่ 5: อ่านผลลัพธ์

```
TRUST NO ONE IN THE PALACE TONIGHT. THE SECRET MUST STAY IN FRANCE. THE FLAG IS REVEALED. flag{v1g3n3r3_c1ph3r_1s_cl4ss1c}
```

---

## 🚩 Flag

```
flag{v1g3n3r3_c1ph3r_1s_cl4ss1c}
```

---

## 🎓 สิ่งที่ได้เรียนรู้

1. **Vigenère Cipher** เป็น polyalphabetic substitution cipher
2. ใช้ **key แบบวนซ้ำ** เพื่อเข้ารหัส
3. **Context clues** ใน story ช่วยระบุประเภท cipher
4. สามารถใช้เครื่องมือออนไลน์เช่น **CyberChef** ถอดรหัสได้ง่าย

---

## 🔐 Key Takeaways

- **อ่าน story อย่างละเอียด** - มักมี hint ซ่อนอยู่
- **รู้จักประวัติการเข้ารหัส** - ช่วยให้จับ pattern ได้เร็วขึ้น
- **ลอง key หลายๆ ตัว** - บางทีต้องเดาจาก context

---

## 📚 Further Learning

### แหล่งเรียนรู้เพิ่มเติม

1. **Wikipedia:** [Vigenère cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)
2. **Crypto Corner:** [Vigenère Analysis](http://crypto.interactive-maths.com/vigenere-cipher.html)
3. **Practical Cryptography:** [Attacking the Vigenère Cipher](http://practicalcryptography.com/cryptanalysis/stochastic-searching/cryptanalysis-vigenere-cipher/)

### เทคนิคการโจมตี Vigenère

- **Kasiski Examination** - หาความยาว key จาก repeated sequences
- **Index of Coincidence** - วิเคราะห์ทางสถิติ
- **Frequency Analysis** - หลังจากรู้ความยาว key

---

## 🧩 Challenge ที่เกี่ยวข้อง

หลังจากทำข้อนี้ได้แล้ว ลองทำข้อเหล่านี้:
- Vigenère Challenge 2 (ข้อถัดไป)
- Autokey Cipher
- Running Key Cipher

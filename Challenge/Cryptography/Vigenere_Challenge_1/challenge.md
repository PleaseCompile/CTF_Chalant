# 📜 The Diplomat's Secret (ความลับของทูต)

## 🎯 Concept
โจทย์นี้จะสอนเกี่ยวกับการถอดรหัสที่ใช้ในศตวรรษที่ 16 โดยนักการทูตชาวฝรั่งเศส ซึ่งเป็นการพัฒนาต่อยอดจาก Caesar cipher แบบธรรมดา

**Difficulty:** ⭐⭐☆☆☆ (Medium)

---

## 📖 Story

### 🇹🇭 ภาษาไทย
ในปี ค.ศ. 1586 ราชสำนักฝรั่งเศสกำลังเผชิญกับภัยคุกคามจากสปาย ทูตคนหนึ่งชื่อ **Blaise** ได้คิดค้นวิธีการเข้ารหัสแบบใหม่ที่เขาเรียกว่า "รหัสที่ไม่มีวันถูกถอด" (*le chiffre indéchiffrable*)

เขาเขียนจดหมายลับถึงกษัตริย์ โดยใช้ **คำสำคัญที่ถูกใช้ซ้ำ** เพื่อเข้ารหัสข้อความทุกตัวอักษร แต่ละตัวอักษรในข้อความจะถูกเลื่อนไปตามค่าของตัวอักษรใน "กุญแจ" ที่วนซ้ำไปเรื่อยๆ

ปัจจุบัน เราพบจดหมายเก่าแก่ฉบับนี้ พร้อมกับโน้ตที่เขียนไว้ข้างกระดาษว่า:
> *"กุญแจคือชื่อของราชวงศ์ที่ยิ่งใหญ่ที่สุดในยุโรป"*

### 🇬🇧 English
In 1586, the French royal court faced threats from spies. A diplomat named **Blaise** invented a new encryption method he called "the unbreakable cipher" (*le chiffre indéchiffrable*).

He wrote secret letters to the king using a **keyword that repeats** to encrypt every character. Each letter in the plaintext is shifted according to the corresponding letter in a "key" that cycles continuously.

Today, we discovered this ancient letter with a note written on the margin:
> *"The key is the name of the greatest dynasty in Europe"*

---

## 💡 Hints

### 🇹🇭 Hint ภาษาไทย
1. **Hint 1:** ชื่อ Blaise นี้มีความสำคัญ... ลองค้นหาว่านักเข้ารหัสชาวฝรั่งเศสในศตวรรษที่ 16 ชื่อ Blaise มีนามสกุลว่าอะไร
2. **Hint 2:** "กุญแจที่วนซ้ำ" หมายความว่าถ้ากุญแจคือ "ABC" และข้อความยาว 6 ตัว กุญแจจะกลายเป็น "ABCABC"
3. **Hint 3:** ราชวงศ์ที่ยิ่งใหญ่ในยุโรป... บูร์บง? ฮับส์เบิร์ก? ทิวดอร์? (ลองทีละตัว ตัวพิมพ์ใหญ่ทั้งหมด)

### 🇬🇧 English Hints
1. **Hint 1:** The name Blaise is significant... Search for a French cryptographer from the 16th century named Blaise and find his surname
2. **Hint 2:** "Repeating key" means if the key is "ABC" and the message is 6 characters, the key becomes "ABCABC"
3. **Hint 3:** The greatest dynasty in Europe... Bourbon? Habsburg? Tudor? (Try each one, all uppercase)

---

## 📦 Data File
ไฟล์: `encrypted_letter.txt`

---

## 🎮 Challenge
ถอดรหัสจดหมายลับของทูต Blaise แล้วหา flag ที่ซ่อนอยู่ในข้อความ

Decrypt the secret letter from diplomat Blaise and find the hidden flag in the message.

---

## 🚩 Flag Format
```
flag{...}
```

---

## 📝 Additional Notes
- การเข้ารหัสแบบนี้ไม่ใช่ Caesar cipher ธรรมดา เพราะแต่ละตัวอักษรถูกเลื่อนด้วยค่าที่ต่างกัน
- This cipher is NOT a simple Caesar cipher because each letter is shifted by a different amount
- ลองหาเครื่องมือออนไลน์ที่รองรับการถอดรหัสแบบ "polyalphabetic substitution"
- Try finding an online tool that supports "polyalphabetic substitution" decryption

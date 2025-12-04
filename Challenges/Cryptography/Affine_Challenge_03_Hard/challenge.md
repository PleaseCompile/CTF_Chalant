# 🔮 รหัสลึกลับแห่งนักเล่นแร่แปรธาตุ (The Alchemist's Mystery)

## 🎯 Concept
นักเล่นแร่แปรธาตุโบราณใช้สูตรลับในการซ่อนความรู้ 
พวกเขาใช้ **การแปลงเชิงเส้น** แต่ไม่เคยบันทึกสูตรไว้ที่ใดเลย...

Ancient alchemists used secret formulas to hide their knowledge.
They used **linear transformation** but never recorded the formula anywhere...

---

## ⭐ Difficulty: Hard (⭐⭐⭐⭐☆)

**ความท้าทาย:** ไม่มีเบาะแสเกี่ยวกับค่า key โดยตรง ต้องใช้:
- Frequency Analysis
- Brute Force Attack
- หรือ Known Plaintext Attack

---

## 📖 Story

คุณคือนักประวัติศาสตร์ที่กำลังศึกษาต้นฉบับโบราณของนักเล่นแร่แปรธาตุในยุคกลาง

ในห้องสมุดลับแห่งหนึ่ง คุณค้นพบหนังสือเก่าแก่ที่มีข้อความถูกเข้ารหัส หน้าที่ฉีกขาดมีเศษข้อความที่พอจะอ่านได้:

> "สูตรนี้ใช้หลักการ **แปลงเชิงเส้น** เช่นเดียวกับที่นักคณิตศาสตร์กรีกใช้
> ตัวคูณและตัวบวกเป็นความลับที่ต้องค้นหาเอง
> แต่จำไว้ว่า... ตัวอักษรทุกตัวถูกแทนที่ด้วยตัวเดียวกันเสมอ"

**ไม่มีค่า key ให้!** คุณต้องหาวิธีถอดรหัสเอง

---

## 💡 Hints

### 🇹🇭 คำใบ้ภาษาไทย
1. นี่คือ **monoalphabetic substitution** - ตัวอักษรเดียวกันถูกแทนที่ด้วยตัวเดียวกันเสมอ
2. ลองใช้ **Frequency Analysis** - ในภาษาอังกฤษ E, T, A, O, I พบบ่อยที่สุด
3. ถ้ารู้ว่าข้อความเริ่มด้วย "THEFLAG" ลองทำ **Known Plaintext Attack**
4. หรือ **Brute Force** ทุก key ที่เป็นไปได้ (312 keys)
5. เครื่องมือ dCode มีโหมด "Automatic" สำหรับ cipher ประเภทนี้

### 🇬🇧 English Hints
1. This is a **monoalphabetic substitution** - same letter always maps to same letter
2. Try **Frequency Analysis** - in English, E, T, A, O, I are most common
3. If you know the message starts with "THEFLAG", try **Known Plaintext Attack**
4. Or **Brute Force** all possible keys (312 keys total)
5. dCode has "Automatic" mode for this type of cipher

---

## 📦 Data

ไฟล์ข้อมูล: `data.txt`

ข้อความที่เข้ารหัสจากหนังสือโบราณ:
```
SQJUIRFBHNWVASPFWRAQVTRHSJW
```

**หมายเหตุ:** ไม่มี key ให้ ต้องหาเอง!

---

## 🎮 Challenge

1. วิเคราะห์ ciphertext และหาวิธีถอดรหัส
2. ค้นหาค่า a และ b ที่ถูกต้อง
3. ถอดรหัสข้อความเพื่อหา flag

**หมายเหตุ:** ข้อความที่ถอดรหัสได้จะบอกคุณว่า flag คืออะไร รูปแบบจะเป็น `THEFLAGIS...`

---

## 🚩 Flag Format

```
flag{md5_hash}
```

**คำแนะนำ:** เมื่อถอดรหัสได้ข้อความแล้ว ให้นำส่วนที่อยู่หลัง "THEFLAGIS" มาทำเป็น MD5 hash (เพิ่ม underscore ระหว่างคำ)

---

## 📚 ความรู้ที่จะได้

- Frequency Analysis
- Brute Force Attack
- Known Plaintext Attack
- การวิเคราะห์ Cipher โดยไม่มี key
- ความเข้าใจลึกซึ้งเกี่ยวกับ Substitution Cipher

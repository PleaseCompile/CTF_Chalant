# 📜 สูตรลับแห่งปิทาโกรัส (The Secret Formula)

## 🎯 Concept
ในโลกแห่งคณิตศาสตร์โบราณ นักปราชญ์ใช้สูตรเชิงเส้นเพื่อซ่อนความลับ 
พวกเขาเชื่อว่าการ**คูณ**และการ**บวก**คือกุญแจสู่ทุกสิ่ง

In the ancient world of mathematics, scholars used linear formulas to hide secrets.
They believed that **multiplication** and **addition** were the keys to everything.

---

## 📖 Story

ในห้องใต้ดินของพิพิธภัณฑ์คณิตศาสตร์โบราณ คุณค้นพบแผ่นหินจารึกที่มีอายุกว่า 2,000 ปี 

บนแผ่นหินมีข้อความที่ถูกเข้ารหัส พร้อมกับสัญลักษณ์ที่ดูเหมือน **ตัวเลข 5** และ **ตัวเลข 8** สลักอยู่ที่มุมบนขวา

นักโบราณคดีบันทึกไว้ว่า:
> "นักปราชญ์กรีกใช้สูตรพิเศษในการแปลงตัวอักษร สูตรนี้มีรูปแบบ **y = ax + b** โดยที่ a ต้องเป็นจำนวนที่ 'ไม่มีตัวหารร่วม' กับจำนวนตัวอักษรในตารางแอลฟาเบต"

คุณสังเกตเห็นว่าตัวเลข 5 และ 8 บนแผ่นหินอาจเป็น**ค่าคงที่**ในสูตรนั้น...

---

## 💡 Hints

### 🇹🇭 คำใบ้ภาษาไทย
1. มองหา "ความสัมพันธ์เชิงเส้น" - รูปแบบ ax + b mod 26
2. ตัวเลขบนแผ่นหินบอกค่า a และ b
3. เครื่องมือออนไลน์หลายตัวรองรับการถอดรหัสแบบ "เชิงเส้น" นี้
4. GCD(5, 26) = 1 หมายความว่าอะไร?

### 🇬🇧 English Hints
1. Look for "linear relationship" - the form ax + b mod 26
2. The numbers on the stone tablet indicate the values of a and b
3. Many online tools support decryption of this "linear" type
4. What does GCD(5, 26) = 1 mean for the cipher?

---

## 📦 Data

ไฟล์ข้อมูล: `data.txt`

ข้อความที่พบบนแผ่นหินจารึก:
```
ZRCHLIMWUIVSWCVZQIZRUCSPCZ
```

ตัวเลขที่สลักบนมุมแผ่นหิน: **5, 8**

---

## 🎮 Challenge

ถอดรหัสข้อความบนแผ่นหินจารึก และค้นหา flag

**หมายเหตุ:** ข้อความที่ถอดรหัสได้จะบอกคุณว่า flag คืออะไร รูปแบบจะเป็น `THEFLAGIS...`

---

## 🚩 Flag Format

```
flag{md5_hash}
```

ตัวอย่าง: `flag{d41d8cd98f00b204e9800998ecf8427e}`

**คำแนะนำ:** เมื่อถอดรหัสได้ข้อความแล้ว ให้นำส่วนที่อยู่หลัง "THEFLAGIS" มาทำเป็น MD5 hash

---

## 📚 ความรู้ที่จะได้

- การเข้ารหัสแบบแทนที่ (Substitution Cipher)
- ความสัมพันธ์เชิงเส้นในการเข้ารหัส
- Modular Arithmetic
- Greatest Common Divisor (GCD)

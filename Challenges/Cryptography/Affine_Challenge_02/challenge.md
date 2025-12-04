# 🕵️ รหัสแห่งสมาคมลับ (The Shadow Society's Code)

## 🎯 Concept
องค์กรลึกลับใช้รหัสที่ผสมผสาน **การคูณ** กับ **การเลื่อน** 
พวกเขาเชื่อว่าตัวเลขที่ **"ไม่มีตัวหารร่วม"** คือกุญแจสู่ความปลอดภัย

A mysterious organization uses a cipher combining **multiplication** and **shifting**.
They believe that numbers with **"no common factors"** are the key to security.

---

## 📖 Story

คุณคือนักสืบไซเบอร์ที่กำลังสืบสวนองค์กรลึกลับที่เรียกตัวเองว่า "Shadow Society"

ในการบุกค้นสำนักงานใต้ดินของพวกเขา คุณพบเอกสารลับที่มีข้อความถูกเข้ารหัส พร้อมกับบันทึกช่วยจำของสมาชิกคนหนึ่ง:

> "จำไว้! รหัสของเราใช้หลักการ **'เจ็ดคูณ สามบวก'** 
> แล้วหารเอาเศษด้วย **จำนวนตัวอักษรในภาษาอังกฤษ**
> 
> ทำไมต้องเจ็ด? เพราะ **7 กับ 26 ไม่มีตัวหารร่วมกันนอกจาก 1**
> นี่คือความงดงามของคณิตศาสตร์!"

นอกจากนี้ยังมีสมการลึกลับเขียนไว้:
```
E(x) ≡ 7x + 3 (mod 26)
```

แต่คุณต้องถอดรหัสด้วยตัวเอง...

---

## 💡 Hints

### 🇹🇭 คำใบ้ภาษาไทย
1. "เจ็ดคูณ สามบวก" บอกอะไรคุณเกี่ยวกับสูตร?
2. การถอดรหัสต้องหา **ตัวผกผันของ 7** ใน mod 26
3. ค้นหาเครื่องมือออนไลน์ที่ใช้ **สูตรเชิงเส้น** ในการถอดรหัส
4. ลองคิดว่า: ถ้า 7 × ? ≡ 1 (mod 26) แล้ว ? = ?

### 🇬🇧 English Hints
1. "Seven multiply, three add" - what does this tell you about the formula?
2. To decrypt, you need to find the **multiplicative inverse of 7** mod 26
3. Search for online tools that use **linear formula** for decryption
4. Think: if 7 × ? ≡ 1 (mod 26), then ? = ?

---

## 📦 Data

ไฟล์ข้อมูล: `data.txt`

เอกสารลับที่พบ:
```
====== TOP SECRET ======
GAFMCDTHZCHQFDSRHEAFSJDZGFS
========================

Formula Note: 7x + 3 (mod 26)
```

---

## 🎮 Challenge

ถอดรหัสข้อความลับขององค์กร Shadow Society และค้นหา flag

**หมายเหตุ:** ข้อความที่ถอดรหัสได้จะบอกคุณว่า flag คืออะไร รูปแบบจะเป็น `THEFLAGIS...`

---

## 🚩 Flag Format

```
flag{md5_hash}
```

ตัวอย่าง: `flag{d41d8cd98f00b204e9800998ecf8427e}`

**คำแนะนำ:** เมื่อถอดรหัสได้ข้อความแล้ว ให้นำส่วนที่อยู่หลัง "THEFLAGIS" มาทำเป็น MD5 hash (เพิ่ม underscore ระหว่างคำ)

---

## 📚 ความรู้ที่จะได้

- การเข้ารหัสแบบ Substitution ที่ใช้สูตรทางคณิตศาสตร์
- Modular Multiplicative Inverse
- ความสำคัญของ Coprime Numbers ในการเข้ารหัส
- Extended Euclidean Algorithm (สำหรับหา inverse)

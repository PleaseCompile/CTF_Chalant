# 🕵️ Corporate Espionage

## 📌 Category: Steganography
## ⭐ Difficulty: ⭐⭐⭐☆☆ (3/5)
## 🎯 Concept: PDF Hidden Layers

---

## 🎯 Concept (แนวคิด)

ในโลกธุรกิจ ข้อมูลบางอย่างถูกซ่อนไว้ต่อหน้าต่อตา ใครจะรู้ว่ารายงานประจำปีธรรมดาๆ อาจมีความลับซ่อนอยู่? บางทีสิ่งที่คุณมองหาอาจอยู่ตรงหน้า... แค่ยังไม่ได้ "เปิด" ให้เห็น

---

## 📖 Story (เรื่องราว)

คุณคือนักวิเคราะห์ความปลอดภัยไซเบอร์ของบริษัท TechSecure Corp. วันหนึ่งคุณได้รับแจ้งว่า มีการรั่วไหลของข้อมูลลับจากภายในบริษัท

ทีมตรวจสอบพบว่าพนักงานคนหนึ่งส่งไฟล์ PDF "รายงานประจำไตรมาส" ออกไปยังอีเมลภายนอก แม้จะดูเหมือนเป็นรายงานการเงินปกติ แต่ทีมสืบสวนสงสัยว่าอาจมี "ข้อมูลพิเศษ" แฝงอยู่

พนักงานคนนั้นเคยพูดกับเพื่อนร่วมงานว่า:

> "เอกสารที่ดีต้องมีหลายมิติ เหมือนหัวหอมที่มีหลายชั้น ยิ่งลอกยิ่งเจอ..."

หน้าที่ของคุณคือวิเคราะห์ไฟล์ PDF นี้และค้นหาว่าข้อมูลอะไรถูกส่งออกไป

---

## 💡 Hints (คำใบ้)

### 🇹🇭 ภาษาไทย
1. **Hint 1:** "หลายชั้นเหมือนหัวหอม" - เอกสารบางชนิดก็มีชั้นได้เหมือนกัน
2. **Hint 2:** โปรแกรมออกแบบกราฟิกมักทำงานกับ "layers" แล้ว PDF ที่ออกมาจากโปรแกรมเหล่านั้นล่ะ?
3. **Hint 3:** Adobe Reader มีแผงควบคุมพิเศษที่ให้คุณจัดการกับ "Optional Content" ได้
4. **Hint 4:** ลอง convert PDF เป็นไฟล์ SVG ดู... คุณอาจเห็นสิ่งที่ PDF ซ่อนไว้

### 🇬🇧 English
1. **Hint 1:** "Multiple layers like an onion" - some documents can have layers too
2. **Hint 2:** Graphic design software works with "layers"... what about PDFs exported from them?
3. **Hint 3:** Adobe Reader has a special panel for managing "Optional Content"
4. **Hint 4:** Try converting PDF to SVG... you might see what the PDF hides

---

## 📦 Files (ไฟล์ที่ให้)

- `quarterly_report_Q3_2024.pdf` - รายงานประจำไตรมาสที่ต้องสงสัย

---

## 🎮 Challenge (โจทย์)

ค้นหาข้อมูลลับที่ถูกซ่อนอยู่ในรายงานนี้ และรายงานผลเป็น flag

---

## 🚩 Flag Format

```
flag{md5_hash}
```

**ตัวอย่าง:** `flag{a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6}`

---

## 🔧 Tools ที่อาจช่วยได้

- PDF readers ที่รองรับการดู Optional Content
- โปรแกรมแก้ไขกราฟิกเวกเตอร์
- เครื่องมือแปลงไฟล์ออนไลน์
- Python libraries สำหรับอ่าน PDF
- Command line tools สำหรับวิเคราะห์เอกสาร

---

## 📝 Note สำหรับผู้ออกโจทย์

**Flag สำหรับข้อนี้:** `flag{c0rp0r4t3_s3cr3ts_3xp0s3d}`

**วิธีสร้างไฟล์ PDF:**
1. สร้างเอกสารใน Adobe Illustrator หรือ Adobe InDesign
2. สร้าง layer สำหรับเนื้อหาปกติ (รายงานการเงิน)
3. สร้าง layer ที่ 2 ซ่อนไว้ ใส่ข้อมูลลับ: "CLASSIFIED: flag{c0rp0r4t3_s3cr3ts_3xp0s3d}"
4. Export เป็น PDF โดยเลือก "Create Acrobat Layers from Top-Level Layers"
5. ตั้งค่า default visibility ของ layer ลับเป็น OFF

**ความแตกต่างจาก Challenge 1:**
- Theme: Corporate/Spy vs Art/Cultural
- Story: Investigation scenario vs Mystery inheritance
- Context: Business document vs Art brochure
- Approach: Security analysis vs Artistic exploration

# 🎨 The Art Gallery's Secret

## 📌 Category: Steganography
## ⭐ Difficulty: ⭐⭐⭐☆☆ (3/5)
## 🎯 Concept: PDF Hidden Layers

---

## 🎯 Concept (แนวคิด)

บางครั้งเอกสารก็ไม่ได้เรียบง่ายอย่างที่เห็น... เหมือนกับภาพวาดที่ศิลปินสร้างสรรค์ไว้หลายชั้น แต่ละชั้นมีความหมายในตัวเอง คุณจะมองทะลุได้ไหม?

---

## 📖 Story (เรื่องราว)

คุณได้รับจดหมายลึกลับจากนักสะสมงานศิลปะผู้ล่วงลับไปแล้ว ในจดหมายมีแค่โบรชัวร์ของหอศิลป์และข้อความสั้นๆ:

> "ศิลปะไม่ได้มีแค่สิ่งที่ตาเห็น ศิลปินที่แท้จริงจะซ่อนความลับไว้ใต้ทุกฝีแปรง ทุกชั้นสี... จงมองให้ลึกกว่าพื้นผิว"

โบรชัวร์ดูเหมือนเป็นแค่เอกสารแนะนำงานศิลปะทั่วไป แต่เมื่อคุณพิจารณาคำพูดสุดท้ายของเขา... บางทีเอกสารนี้อาจมีมากกว่าที่เห็น?

---

## 💡 Hints (คำใบ้)

### 🇹🇭 ภาษาไทย
1. **Hint 1:** ศิลปินวาดภาพโดยการซ้อนสีหลายชั้น... เอกสารก็ทำได้เช่นกัน
2. **Hint 2:** Photoshop มี Layers, Illustrator มี Layers... แล้ว PDF ล่ะ?
3. **Hint 3:** ลองเปิดด้วยโปรแกรมที่มองเห็นโครงสร้างภายในของเอกสาร หรือใช้ตัวเลือก "Layer" ใน Adobe Reader
4. **Hint 4:** เครื่องมือออนไลน์บางตัวสามารถ "แกะ" โครงสร้างของ PDF ได้

### 🇬🇧 English
1. **Hint 1:** Artists paint by stacking multiple layers of color... documents can do that too
2. **Hint 2:** Photoshop has Layers, Illustrator has Layers... what about PDF?
3. **Hint 3:** Try opening with software that can see the internal structure, or use "Layer" options in Adobe Reader
4. **Hint 4:** Some online tools can "deconstruct" the PDF structure

---

## 📦 Files (ไฟล์ที่ให้)

- `art_gallery_brochure.pdf` - โบรชัวร์หอศิลป์ที่ได้รับมา

---

## 🎮 Challenge (โจทย์)

ค้นหา flag ที่ซ่อนอยู่ในโบรชัวร์นี้

---

## 🚩 Flag Format

```
flag{md5_hash}
```

**ตัวอย่าง:** `flag{a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6}`

---

## 🔧 Tools ที่อาจช่วยได้

- Adobe Acrobat Reader (View → Navigation Panels → Layers)
- PDF-XChange Editor
- Inkscape (Import PDF with layers)
- Online PDF Layer extractors
- pdftotext, pdftk, mutool
- Python: PyMuPDF (fitz), PyPDF2

---

## 📝 Note สำหรับผู้ออกโจทย์

**Flag สำหรับข้อนี้:** `flag{h1dd3n_4rt_l4y3rs_r3v34l3d}`

**วิธีสร้างไฟล์ PDF:**
1. ใช้ Adobe Illustrator หรือ Inkscape สร้างเอกสารหลายชั้น
2. ชั้นล่างสุดใส่ flag
3. ชั้นบนซ้อนทับด้วยภาพหรือข้อความอื่น
4. Export เป็น PDF โดยเก็บ layers ไว้

# 🎨 The Art Gallery's Secret - Writeup

## 📚 พื้นฐานที่ต้องรู้ (สอนตั้งแต่ 0)

### PDF คืออะไร?

PDF (Portable Document Format) เป็นรูปแบบไฟล์ที่พัฒนาโดย Adobe ออกแบบมาให้แสดงผลเหมือนกันในทุกอุปกรณ์ ไฟล์ PDF ประกอบด้วย:

- **Text** - ข้อความ
- **Images** - รูปภาพ
- **Vectors** - กราฟิกเวกเตอร์
- **Fonts** - แบบอักษรที่ embed ไว้
- **Metadata** - ข้อมูลเกี่ยวกับเอกสาร
- **Layers (Optional Content)** - ชั้นข้อมูลที่สามารถซ่อน/แสดงได้

### PDF Layers คืออะไร?

PDF Layers หรือ **Optional Content Groups (OCGs)** เป็นฟีเจอร์ที่อนุญาตให้:

1. แบ่งเนื้อหาออกเป็นชั้นๆ
2. ซ่อน/แสดง layers ตามต้องการ
3. กำหนด visibility เริ่มต้นของแต่ละ layer

**ตัวอย่างการใช้งานปกติ:**
- แผนที่หลายชั้น (ถนน, สถานที่สำคัญ, topography)
- แบบแปลน CAD ที่มีหลายระบบ (ไฟฟ้า, ประปา, โครงสร้าง)
- เอกสารหลายภาษา
- ฟอร์มที่มีหลายเวอร์ชัน

### Steganography ใน PDF Layers

**Steganography** = ศาสตร์แห่งการซ่อนข้อมูล

ใน PDF เราสามารถซ่อนข้อมูลได้โดย:
1. สร้าง layer ที่ถูกซ่อนโดย default
2. ใส่ข้อมูลลับลงไปใน hidden layer
3. ผู้รับต้องรู้ว่ามี layers และเปิดดู

---

## 🔍 วิธีแก้โจทย์ทีละขั้นตอน

### ขั้นตอนที่ 1: วิเคราะห์โจทย์

อ่านโจทย์ดีๆ:
> "ศิลปะไม่ได้มีแค่สิ่งที่ตาเห็น ศิลปินที่แท้จริงจะซ่อนความลับไว้ใต้ทุกฝีแปรง **ทุกชั้นสี**... จงมองให้ลึกกว่าพื้นผิว"

**Keywords ที่น่าสนใจ:**
- "ทุกชั้นสี" → Layers!
- "ซ่อนความลับ" → Hidden content
- "มองให้ลึกกว่าพื้นผิว" → Look beyond what's visible

### ขั้นตอนที่ 2: ตรวจสอบไฟล์

```bash
# ดูประเภทไฟล์
file art_gallery_brochure.pdf

# ดูขนาด
ls -la art_gallery_brochure.pdf

# ดู metadata
exiftool art_gallery_brochure.pdf
```

### ขั้นตอนที่ 3: ค้นหา Layers

#### วิธีที่ 1: Adobe Acrobat Reader (ง่ายที่สุด)

1. เปิดไฟล์ด้วย Adobe Acrobat Reader
2. ไปที่ **View → Navigation Panels → Layers**
3. หรือกด **Ctrl+Shift+L**
4. แผง Layers จะปรากฏทางซ้าย
5. คลิกไอคอน 👁 เพื่อ toggle visibility

```
Layers Panel:
├── 📁 Background (visible)
├── 📁 Main Content (visible)  
└── 📁 Secret Layer (hidden) ← คลิกเปิด!
```

6. เปิด "Secret Layer" จะเห็น flag!

#### วิธีที่ 2: Inkscape

1. เปิด Inkscape
2. **File → Import** → เลือก PDF
3. เลือก "Internal import"
4. **Layer → Layers and Objects** (Ctrl+Shift+L)
5. Toggle visibility ของแต่ละ layer

#### วิธีที่ 3: Python Script

```python
import fitz  # pip install PyMuPDF

doc = fitz.open("art_gallery_brochure.pdf")

# ดู layers
ocgs = doc.get_ocgs()
print(f"Found {len(ocgs)} layers")

# Extract text ทั้งหมด (รวม hidden)
for page in doc:
    text = page.get_text()
    if "flag{" in text:
        print(f"Found flag: {text}")
```

### ขั้นตอนที่ 4: ได้ Flag!

เมื่อเปิด hidden layer จะเห็น:

```
flag{h1dd3n_4rt_l4y3rs_r3v34l3d}
```

---

## 💻 วิธีแก้หลายแบบ

### Method 1: Adobe Reader (Beginner)

```
Time: 1 นาที
Skill: Basic
Tools: Adobe Acrobat Reader (Free)

Steps:
1. Open PDF
2. View → Navigation Panels → Layers
3. Toggle hidden layer
4. Read flag
```

### Method 2: Inkscape (Intermediate)

```
Time: 2 นาที
Skill: Basic graphic software knowledge
Tools: Inkscape (Free, Open Source)

Steps:
1. Import PDF to Inkscape
2. Open Layers panel
3. Show all layers
4. Read flag
```

### Method 3: PyMuPDF Script (Advanced)

```python
#!/usr/bin/env python3
"""Extract hidden layers from PDF"""

import fitz
import re

def extract_hidden_content(pdf_path):
    doc = fitz.open(pdf_path)
    
    # Get all OCGs (layers)
    ocgs = doc.get_ocgs()
    print(f"[*] Found {len(ocgs)} layers")
    
    for xref, info in ocgs.items():
        print(f"    Layer {xref}: {info.get('name', 'unnamed')}")
        print(f"    State: {'ON' if info.get('on') else 'OFF'}")
    
    # Extract ALL text (including hidden)
    all_text = ""
    for page in doc:
        all_text += page.get_text()
    
    # Find flags
    flags = re.findall(r'flag\{[^}]+\}', all_text)
    if flags:
        print(f"\n[+] Found flags: {flags}")
    
    return flags

if __name__ == "__main__":
    extract_hidden_content("art_gallery_brochure.pdf")
```

### Method 4: Command Line (Linux/Mac)

```bash
# Extract all text including hidden
pdftotext -layout art_gallery_brochure.pdf -

# Or search directly
strings art_gallery_brochure.pdf | grep -i "flag{"

# Using mutool
mutool draw -F text art_gallery_brochure.pdf
```

### Method 5: Online Tools

1. ไปที่ **convertio.co**
2. Convert PDF → SVG
3. เปิด SVG ด้วย text editor
4. ค้นหา "flag{"

---

## 🎓 สิ่งที่ได้เรียนรู้

### Technical Skills

1. **PDF Structure** - เข้าใจว่า PDF มีโครงสร้างซับซ้อน ไม่ใช่แค่ภาพนิ่ง
2. **PDF Layers (OCG)** - รู้จัก Optional Content Groups
3. **PDF Tools** - ใช้เครื่องมือวิเคราะห์ PDF ได้หลายตัว
4. **Steganography** - เข้าใจเทคนิคการซ่อนข้อมูลในไฟล์

### CTF Skills

1. **Hint Analysis** - อ่าน hint แล้วเชื่อมโยงกับเทคนิค
2. **Tool Selection** - เลือกเครื่องมือที่เหมาะสม
3. **Multi-approach** - ลองหลายวิธีถ้าวิธีแรกไม่ได้ผล

---

## 🔐 Key Takeaways

| Concept | Description |
|---------|-------------|
| PDF Layers | PDF รองรับ multiple layers ที่ซ่อน/แสดงได้ |
| OCG | Optional Content Groups - ชื่อทางเทคนิคของ PDF layers |
| Default Visibility | Layers สามารถตั้งค่าเริ่มต้นเป็น hidden |
| Extraction | Text ใน hidden layers ยังคง extract ได้ด้วย tools |

---

## 📚 Further Learning

### เครื่องมือที่ควรรู้จัก

| Tool | Type | Usage |
|------|------|-------|
| Adobe Acrobat Reader | GUI | View layers |
| Inkscape | GUI | Edit PDF as vector |
| PyMuPDF | Python | Programmatic analysis |
| pdftk | CLI | PDF manipulation |
| mutool | CLI | MuPDF toolkit |
| pdftotext | CLI | Text extraction |

### แหล่งเรียนรู้เพิ่มเติม

1. **PDF Reference** - Adobe's official PDF specification
2. **ISO 32000** - PDF international standard
3. **CTF Steganography challenges** - ฝึกทำโจทย์อื่นๆ
4. **PyMuPDF Documentation** - https://pymupdf.readthedocs.io/

### โจทย์ที่คล้ายกัน

- PDF with hidden annotations
- PDF with invisible text (white on white)
- PDF with off-page content
- PDF with embedded files in layers

---

## 🏁 Summary

```
Challenge: The Art Gallery's Secret
Category: Steganography  
Technique: PDF Hidden Layers
Difficulty: ⭐⭐⭐☆☆

Flag: flag{h1dd3n_4rt_l4y3rs_r3v34l3d}

Key Insight: PDF documents can contain multiple layers (OCG)
             that can be hidden by default. Always check for
             layers when analyzing PDF files in CTF.
```

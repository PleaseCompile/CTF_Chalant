# 📄 PDF Layers Steganography

## 📌 Category Information

| Attribute | Value |
|-----------|-------|
| **Category** | Steganography |
| **Technique** | PDF Hidden Layers (Optional Content Groups) |
| **Difficulty** | ⭐⭐⭐☆☆ (3/5) |
| **Skills Required** | PDF analysis, Layer manipulation, Forensics basics |

---

## 📖 Concept Overview

PDF (Portable Document Format) รองรับฟีเจอร์ **Optional Content Groups (OCGs)** หรือที่เรียกว่า **Layers** ซึ่งอนุญาตให้:

- แบ่งเนื้อหาออกเป็นชั้นๆ
- ซ่อน/แสดง layers ตามต้องการ
- กำหนด visibility เริ่มต้นของแต่ละ layer

### การใช้งานปกติ

- แผนที่หลายชั้น (ถนน, สถานที่, terrain)
- แบบแปลน CAD (ไฟฟ้า, ประปา, โครงสร้าง)
- เอกสารหลายภาษา
- ฟอร์มที่มีหลายเวอร์ชัน

### การใช้ในทางที่ผิด (Steganography)

- ซ่อนข้อมูลลับใน hidden layers
- ซ่อนข้อความใน layers ที่ถูกปิดโดย default
- Data exfiltration ผ่านเอกสารที่ดูธรรมดา

---

## 🎯 Challenges ในหมวดนี้

### Challenge 1: The Art Gallery's Secret
- **Theme:** Artistic/Cultural
- **Story:** ได้รับโบรชัวร์หอศิลป์จากนักสะสมผู้ล่วงลับ
- **Flag:** `flag{h1dd3n_4rt_l4y3rs_r3v34l3d}`
- **Files:** `challenge.md`, `solution.py`, `writeup.md`

### Challenge 2: Corporate Espionage
- **Theme:** Corporate/Investigation
- **Story:** สืบสวนการรั่วไหลข้อมูลผ่านรายงานการเงิน
- **Flag:** `flag{c0rp0r4t3_s3cr3ts_3xp0s3d}`
- **Files:** `challenge.md`, `solution.py`, `writeup.md`

---

## 🛠 Recommended Tools

### GUI Tools
| Tool | Platform | Description |
|------|----------|-------------|
| Adobe Acrobat Reader | All | View layers (free) |
| Adobe Acrobat Pro | All | Full layer control |
| Inkscape | All | Import PDF as editable vector |
| PDF-XChange Editor | Windows | Advanced PDF editing |

### Command Line Tools
| Tool | Installation | Usage |
|------|--------------|-------|
| `pdftotext` | `apt install poppler-utils` | Extract text from all layers |
| `pdftk` | `apt install pdftk` | PDF manipulation |
| `mutool` | `apt install mupdf-tools` | PDF structure analysis |
| `strings` | Built-in | Quick text search |

### Python Libraries
| Library | Installation | Usage |
|---------|--------------|-------|
| PyMuPDF (fitz) | `pip install PyMuPDF` | Full PDF manipulation |
| PyPDF2 | `pip install PyPDF2` | Basic PDF reading |
| pikepdf | `pip install pikepdf` | Low-level PDF access |
| pdfplumber | `pip install pdfplumber` | Text & table extraction |

---

## 🔍 Quick Solve Commands

```bash
# Method 1: strings (fastest)
strings document.pdf | grep -i "flag{"

# Method 2: pdftotext
pdftotext document.pdf - | grep -i "flag{"

# Method 3: PyMuPDF
python3 -c "import fitz; doc=fitz.open('document.pdf'); print([p.get_text() for p in doc])"
```

---

## 📚 Learning Resources

- [PDF Reference 1.7](https://www.adobe.com/devnet/pdf.html) - Chapter 4.10: Optional Content
- [ISO 32000-1:2008](https://www.iso.org/standard/51502.html) - PDF Standard
- [PyMuPDF Documentation](https://pymupdf.readthedocs.io/)
- [Didier Stevens PDF Tools](https://blog.didierstevens.com/programs/pdf-tools/)

---

## 📁 Directory Structure

```
PDF_Layers_Stego/
├── README.md                          # This file
├── Challenge_1_Art_Gallery_Secret/
│   ├── challenge.md                   # Challenge description
│   ├── solution.py                    # Multiple solution methods
│   └── writeup.md                     # Detailed walkthrough
└── Challenge_2_Corporate_Espionage/
    ├── challenge.md                   # Challenge description
    ├── solution.py                    # Multiple solution methods
    └── writeup.md                     # Detailed walkthrough
```

---

## ⚠️ Note for Challenge Creators

เมื่อสร้าง PDF ที่มี hidden layers:

1. **สร้างใน Adobe Illustrator/InDesign:**
   - สร้าง layers ตามต้องการ
   - ตั้งค่า layer visibility
   - Export as PDF with "Create Acrobat Layers"

2. **หรือใช้ Inkscape:**
   - สร้าง SVG ที่มีหลาย layers
   - Save as PDF
   - Layers จะถูกเก็บรักษาไว้

3. **ใช้ Python (PyMuPDF):**
   ```python
   import fitz
   # สร้าง PDF with OCG programmatically
   doc = fitz.open()
   page = doc.new_page()
   # Add content with layer assignment
   ```

4. **Test PDF:**
   - ตรวจสอบว่า layers ทำงานถูกต้อง
   - ทดสอบ flag extraction ด้วยหลายวิธี

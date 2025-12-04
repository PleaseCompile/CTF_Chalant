# 🕵️ Corporate Espionage - Writeup

## 📚 พื้นฐานที่ต้องรู้ (สอนตั้งแต่ 0)

### PDF Layers ในบริบท Corporate

ในองค์กรขนาดใหญ่ PDF เป็นรูปแบบมาตรฐานสำหรับเอกสารทางการ เช่น:
- รายงานการเงิน
- แบบแปลนอาคาร
- เอกสารทางกฎหมาย
- แผนธุรกิจ

PDF Layers ถูกนำมาใช้อย่างแพร่หลายเพื่อ:
- แยกเนื้อหาตามประเภท (ข้อความ, กราฟ, ตาราง)
- แสดงเวอร์ชันต่างๆ ในไฟล์เดียว
- ซ่อนข้อมูลที่ไม่ต้องการให้เห็นในการพิมพ์

### ความเสี่ยงด้านความปลอดภัย

**Data Leakage ผ่าน PDF Layers:**

1. **Metadata ที่ถูกลืม** - ข้อมูลผู้สร้าง, วันที่แก้ไข
2. **Hidden Layers** - Layers ที่ถูกซ่อนแต่ยังมีข้อมูลอยู่
3. **Previous Versions** - เวอร์ชันเก่าที่ยังอยู่ใน PDF
4. **Comments & Annotations** - ความเห็นที่ซ่อนไว้

ในโลกจริง มีหลายกรณีที่ข้อมูลรั่วไหลผ่าน PDF:
- เอกสารรัฐบาลที่ redact ไม่ดี
- สัญญาที่มี hidden text
- แบบแปลนอาคารที่มี security flaws ซ่อนอยู่

---

## 🔍 วิธีแก้โจทย์ทีละขั้นตอน

### ขั้นตอนที่ 1: วิเคราะห์บริบท

อ่าน story:
> พนักงานคนนั้นเคยพูดว่า: "เอกสารที่ดีต้องมีหลายมิติ เหมือนหัวหอมที่มี**หลายชั้น** ยิ่งลอกยิ่งเจอ..."

**Keywords:**
- "หลายชั้น" = Layers
- "ยิ่งลอกยิ่งเจอ" = Hidden content underneath
- Context: Corporate espionage = Sensitive data hidden in documents

### ขั้นตอนที่ 2: Initial Analysis

```bash
# ตรวจสอบไฟล์
$ file quarterly_report_Q3_2024.pdf
quarterly_report_Q3_2024.pdf: PDF document, version 1.7

# ดูขนาด (ไฟล์ที่มี hidden content มักใหญ่กว่าปกติ)
$ ls -lh quarterly_report_Q3_2024.pdf
-rw-r--r-- 1 user user 2.3M Jan 1 12:00 quarterly_report_Q3_2024.pdf

# Quick search
$ strings quarterly_report_Q3_2024.pdf | grep -i "flag\|classified\|secret"
CLASSIFIED: flag{c0rp0r4t3_s3cr3ts_3xp0s3d}
```

### ขั้นตอนที่ 3: Layer Analysis

#### วิธี A: Adobe Reader/Pro

1. เปิดไฟล์ด้วย Adobe Acrobat
2. **View → Navigation Panels → Layers**
3. ดู Layer Panel:

```
📄 Document Layers
├── 📁 Report Header (✓ visible)
├── 📁 Financial Tables (✓ visible)
├── 📁 Charts (✓ visible)
└── 📁 ??? (hidden)  ← ต้องสงสัย!
```

4. เปิด hidden layer โดยคลิก checkbox
5. พบข้อความ: `CLASSIFIED: flag{c0rp0r4t3_s3cr3ts_3xp0s3d}`

#### วิธี B: Python Script

```python
#!/usr/bin/env python3
import fitz  # PyMuPDF

def investigate_pdf(path):
    doc = fitz.open(path)
    
    # 1. List all layers
    ocgs = doc.get_ocgs()
    print(f"Layers found: {len(ocgs)}")
    
    for xref, info in ocgs.items():
        status = "VISIBLE" if info.get('on') else "HIDDEN"
        print(f"  [{status}] {info.get('name', 'unnamed')}")
    
    # 2. Extract ALL text (including hidden)
    for page in doc:
        text = page.get_text()
        if "flag{" in text.lower() or "classified" in text.lower():
            print(f"\n[!] Sensitive data found:")
            print(text)
    
    doc.close()

investigate_pdf("quarterly_report_Q3_2024.pdf")
```

### ขั้นตอนที่ 4: Flag Recovery

```
CLASSIFIED: flag{c0rp0r4t3_s3cr3ts_3xp0s3d}
```

**Flag:** `flag{c0rp0r4t3_s3cr3ts_3xp0s3d}`

---

## 💻 วิธีแก้หลายแบบ

### Method 1: strings (1 นาที)

```bash
strings quarterly_report_Q3_2024.pdf | grep -i flag
# Output: flag{c0rp0r4t3_s3cr3ts_3xp0s3d}
```

**ทำไมได้ผล:** Text ใน PDF layers ยังคงอยู่ใน file แม้จะถูกซ่อน

### Method 2: pdftotext (1 นาที)

```bash
pdftotext quarterly_report_Q3_2024.pdf - | grep flag
```

**ทำไมได้ผล:** pdftotext extract text จากทุก layers

### Method 3: GUI with Adobe (2 นาที)

1. Open PDF
2. View → Layers Panel
3. Toggle hidden layer
4. Copy flag

### Method 4: Convert to SVG (3 นาที)

```bash
# แปลงเป็น SVG
inkscape --export-type=svg quarterly_report_Q3_2024.pdf

# ค้นหาใน SVG
grep -i flag quarterly_report_Q3_2024.svg
```

### Method 5: PyMuPDF Analysis (5 นาที)

```python
import fitz
import re

doc = fitz.open("quarterly_report_Q3_2024.pdf")

# วิเคราะห์ OCGs
print("=== Layer Analysis ===")
for xref, info in doc.get_ocgs().items():
    print(f"{info['name']}: {'ON' if info['on'] else 'OFF'}")

# Extract all content
all_text = ""
for page in doc:
    all_text += page.get_text()

# Find sensitive data
flags = re.findall(r'flag\{[^}]+\}', all_text)
print(f"\n=== Flags Found ===\n{flags}")
```

---

## 🎓 สิ่งที่ได้เรียนรู้

### Technical Knowledge

1. **PDF Optional Content Groups (OCGs)**
   - PDF รองรับ multiple layers
   - Layers สามารถตั้ง default visibility
   - Hidden layers ยังมี content อยู่

2. **PDF Security Implications**
   - Hidden layers ไม่ได้ "ลบ" ข้อมูล
   - Sensitive data ต้อง redact อย่างถูกวิธี
   - ต้องใช้ proper sanitization tools

3. **Forensic Analysis**
   - หลายเครื่องมือสามารถ reveal hidden content
   - Text extraction ได้ทุก layers
   - Binary analysis reveal raw strings

### Real-World Applications

1. **Document Security**
   - ต้องลบ metadata ก่อนแชร์
   - ใช้ proper redaction tools
   - Flatten layers ก่อน publish

2. **Forensic Investigation**
   - ตรวจสอบ PDFs สำหรับ hidden content
   - วิเคราะห์ documents ที่ต้องสงสัย
   - Recover "deleted" information

---

## 🔐 Key Takeaways

| Topic | Lesson |
|-------|--------|
| PDF Layers | ซ่อนได้แต่ไม่ได้หายไป |
| strings command | วิธีง่ายที่สุดในการหา hidden text |
| Document Security | Hidden ≠ Removed |
| Forensics | หลายเครื่องมือ reveal hidden content |

---

## 📚 Further Learning

### เครื่องมือ Forensic สำหรับ PDF

| Tool | Purpose |
|------|---------|
| pdf-parser | Deep structure analysis |
| peepdf | Security analysis |
| qpdf | PDF transformation |
| Didier Stevens tools | Forensic toolkit |

### การป้องกัน (สำหรับ Blue Team)

1. **Document Sanitization**
   - ใช้ Adobe Acrobat Pro → Sanitize Document
   - หรือ third-party tools เช่น pdf-redact-tools

2. **Before Publishing**
   - Remove metadata
   - Flatten layers
   - Remove hidden content
   - Test with multiple tools

3. **Policy & Training**
   - สอนพนักงานเรื่อง document security
   - ใช้ approved tools เท่านั้น
   - Review process ก่อน publish

### แหล่งข้อมูลเพิ่มเติม

- NSA's PDF Redaction Guide
- SANS Digital Forensics courses
- Adobe PDF Reference Manual
- OWASP Document Security guidelines

---

## 🏁 Summary

```
Challenge: Corporate Espionage
Category: Steganography
Technique: PDF Hidden Layers
Difficulty: ⭐⭐⭐☆☆

Flag: flag{c0rp0r4t3_s3cr3ts_3xp0s3d}

Scenario: Corporate investigation for data exfiltration
Method: Hidden PDF layers containing classified information
Lesson: PDF hidden layers don't truly hide data - 
        proper document sanitization is essential

Key Tools: strings, pdftotext, PyMuPDF, Adobe Acrobat
```

---

## 🆚 เปรียบเทียบกับ Challenge 1

| Aspect | Challenge 1 | Challenge 2 |
|--------|-------------|-------------|
| Theme | Art Gallery | Corporate Espionage |
| Story | Mystery inheritance | Security investigation |
| Context | Cultural/Artistic | Business/Security |
| Motivation | Curiosity | Forensic duty |
| Tone | Mysterious | Professional |
| Same Technique | ✓ PDF Layers | ✓ PDF Layers |

"""
🎨 The Art Gallery's Secret - Solution
PDF Layers Steganography Challenge

Multiple methods to extract hidden layers from PDF
"""

# ============================================
# Method 1: Using PyMuPDF (fitz) - Recommended
# ============================================
def method1_pymupdf():
    """
    วิธีที่ 1: ใช้ PyMuPDF (fitz) library
    
    ติดตั้ง: pip install PyMuPDF
    """
    import fitz  # PyMuPDF
    
    # เปิดไฟล์ PDF
    pdf_path = "art_gallery_brochure.pdf"
    doc = fitz.open(pdf_path)
    
    # ดู Optional Content Groups (Layers)
    print("=== PDF Layers Analysis ===")
    
    # วิธีที่ 1.1: ดู OCGs (Optional Content Groups)
    ocgs = doc.get_ocgs()
    if ocgs:
        print(f"\n[+] Found {len(ocgs)} layers:")
        for xref, info in ocgs.items():
            print(f"  - Layer {xref}: {info}")
    
    # วิธีที่ 1.2: Extract text from all layers
    print("\n=== Text from each page ===")
    for page_num in range(len(doc)):
        page = doc[page_num]
        
        # รับ text blocks ทั้งหมด
        blocks = page.get_text("dict")["blocks"]
        
        print(f"\n[Page {page_num + 1}]")
        for block in blocks:
            if "lines" in block:
                for line in block["lines"]:
                    for span in line["spans"]:
                        text = span["text"].strip()
                        if text:
                            # ตรวจสอบว่าเป็น flag หรือไม่
                            if "flag{" in text.lower():
                                print(f"  [FLAG FOUND!] {text}")
                            else:
                                print(f"  {text}")
    
    # วิธีที่ 1.3: Toggle layers visibility
    print("\n=== Toggling Layer Visibility ===")
    if ocgs:
        for xref in ocgs.keys():
            # ซ่อน layer อื่นๆ แล้วแสดง layer นี้เท่านั้น
            doc.set_layer_ui_config(doc.get_layer_ui_config())
            
    doc.close()
    
    print("\n[+] Flag: flag{h1dd3n_4rt_l4y3rs_r3v34l3d}")


# ============================================
# Method 2: Using pdftk (Command Line)
# ============================================
def method2_pdftk():
    """
    วิธีที่ 2: ใช้ pdftk และ command line tools
    
    ติดตั้ง: 
    - Ubuntu/Debian: sudo apt install pdftk poppler-utils
    - macOS: brew install pdftk-java poppler
    """
    import subprocess
    import os
    
    pdf_path = "art_gallery_brochure.pdf"
    
    print("=== Using pdftk to analyze PDF ===\n")
    
    # 1. Dump PDF metadata and structure
    print("[1] Dumping PDF structure...")
    # Use list of arguments instead of shell=True for security
    commands = [
        # Dump all PDF data
        (["pdftk", pdf_path, "dump_data"], "pdftk dump_data"),
        
        # Extract text with pdftotext
        (["pdftotext", "-layout", pdf_path, "-"], "pdftotext -layout"),
        
        # Use mutool to show PDF structure
        (["mutool", "show", pdf_path, "trailer"], "mutool show trailer"),
        
        # List all objects
        (["mutool", "show", pdf_path, "grep"], "mutool show grep"),
    ]
    
    for cmd_args, cmd_desc in commands:
        print(f"\n[Command] {cmd_desc}")
        try:
            result = subprocess.run(cmd_args, capture_output=True, text=True)
            print(result.stdout[:1000] if result.stdout else "No output")
        except FileNotFoundError:
            print("Tool not found. Install required tools.")
    
    # 2. Extract images which might contain hidden data
    print("\n[2] Extracting embedded images...")
    os.makedirs("extracted_images", exist_ok=True)
    try:
        subprocess.run([
            "pdfimages", "-all", pdf_path, "extracted_images/img"
        ])
        print("Images extracted to extracted_images/")
    except FileNotFoundError:
        print("pdfimages not found. Install poppler-utils.")
    
    print("\n[+] Flag: flag{h1dd3n_4rt_l4y3rs_r3v34l3d}")


# ============================================
# Method 3: Using Inkscape (GUI Method)
# ============================================
def method3_inkscape_gui():
    """
    วิธีที่ 3: ใช้ Inkscape เปิด PDF เพื่อดู layers
    
    ขั้นตอน:
    1. เปิด Inkscape
    2. File → Import → เลือก PDF file
    3. เลือก "Import pages as: Internal import"
    4. คลิก OK
    5. ไปที่ Layer → Layers and Objects (Ctrl+Shift+L)
    6. จะเห็น layers ทั้งหมดของ PDF
    7. Toggle visibility ของแต่ละ layer เพื่อหา hidden content
    
    หรือใช้ command line:
    inkscape --export-type=svg art_gallery_brochure.pdf
    แล้วเปิด SVG ด้วย text editor เพื่อดู layers
    """
    
    print("""
    === Inkscape Method (GUI) ===
    
    ขั้นตอนการใช้ Inkscape:
    
    1. เปิด Inkscape
    2. File → Import → เลือก "art_gallery_brochure.pdf"
    3. ในหน้าต่าง import เลือก:
       - Import pages as: Internal import
       - คลิก OK
    4. เมื่อเปิดแล้ว ไปที่ Layer → Layers and Objects (Ctrl+Shift+L)
    5. ในแผง Layers จะเห็น layers ทั้งหมด
    6. คลิกไอคอนรูปตาเพื่อ toggle visibility
    7. ซ่อน layer บนสุด จะเห็น flag ที่ซ่อนไว้ด้านล่าง
    
    [+] Flag: flag{h1dd3n_4rt_l4y3rs_r3v34l3d}
    """)


# ============================================
# Method 4: Adobe Acrobat Reader (GUI)
# ============================================
def method4_adobe_reader():
    """
    วิธีที่ 4: ใช้ Adobe Acrobat Reader ดู layers
    
    ขั้นตอน:
    1. เปิดไฟล์ PDF ด้วย Adobe Acrobat Reader
    2. ไปที่ View → Navigation Panels → Layers
    3. แผง Layers จะปรากฏทางซ้าย
    4. คลิกไอคอนรูปตาเพื่อ toggle visibility ของแต่ละ layer
    5. flag จะซ่อนอยู่ใน layer ที่ถูกซ่อนไว้
    """
    
    print("""
    === Adobe Acrobat Reader Method ===
    
    ขั้นตอน:
    
    1. เปิดไฟล์ "art_gallery_brochure.pdf" ด้วย Adobe Acrobat Reader
    
    2. ไปที่เมนู: View → Navigation Panels → Layers
       (หรือกด Ctrl+Shift+L บน Windows)
    
    3. แผง "Layers" จะปรากฏทางด้านซ้ายของหน้าจอ
    
    4. จะเห็นรายการ layers ทั้งหมดในเอกสาร เช่น:
       - Background
       - Main Content  
       - Hidden Layer (ถูกซ่อนไว้)
    
    5. คลิกที่ไอคอนรูปตา 👁 หน้า layer เพื่อ toggle visibility
    
    6. เปิด layer ที่ถูกซ่อน จะเห็น flag
    
    [+] Flag: flag{h1dd3n_4rt_l4y3rs_r3v34l3d}
    """)


# ============================================
# Method 5: Online Tools
# ============================================
def method5_online_tools():
    """
    วิธีที่ 5: ใช้เครื่องมือออนไลน์
    """
    
    print("""
    === Online Tools Method ===
    
    เครื่องมือออนไลน์ที่สามารถใช้ได้:
    
    1. PDF24 Tools (https://tools.pdf24.org/en/extract-pdf-content)
       - สามารถ extract content และดู structure ได้
    
    2. Smallpdf (https://smallpdf.com)
       - มี PDF tools หลายตัว
    
    3. ILovePDF (https://www.ilovepdf.com)
       - สามารถแปลง PDF เป็น format อื่นเพื่อดู layers
    
    4. PDF2GO (https://www.pdf2go.com)
       - มีตัวเลือก edit PDF online
    
    5. Convertio (https://convertio.co)
       - แปลง PDF → SVG จะเห็น layers
    
    วิธีการ:
    1. Upload PDF ไปยังเว็บไซต์
    2. เลือก convert เป็น SVG หรือ AI format
    3. Download แล้วเปิดดู จะเห็น layers แยกกัน
    4. หรือใช้ PDF editor online เพื่อดู hidden layers
    
    [+] Flag: flag{h1dd3n_4rt_l4y3rs_r3v34l3d}
    """)


# ============================================
# Method 6: Raw PDF Analysis
# ============================================
def method6_raw_analysis():
    """
    วิธีที่ 6: วิเคราะห์ PDF โดยตรง (Advanced)
    
    PDF file structure มี Optional Content Groups (OCGs)
    ที่เก็บข้อมูล layers
    """
    
    print("""
    === Raw PDF Analysis ===
    
    PDF structure สำหรับ layers:
    
    1. OCG (Optional Content Group) คือวิธีที่ PDF เก็บ layers
    
    2. ใน PDF file จะมี objects แบบนี้:
    
       /Type /OCG
       /Name (Hidden Layer)
       
    3. วิธีค้นหา:
       - เปิด PDF ด้วย text editor (เช่น Notepad++, VS Code)
       - ค้นหา "/OCG" หรือ "/OC"
       - ค้นหา "flag{" โดยตรง
       
    4. ใช้ Python:
    """)
    
    pdf_path = "art_gallery_brochure.pdf"
    
    try:
        with open(pdf_path, 'rb') as f:
            content = f.read()
            
            # ค้นหา flag pattern
            import re
            flags = re.findall(b'flag\\{[^}]+\\}', content)
            if flags:
                print(f"\n[FOUND] Flags in raw PDF:")
                for flag in flags:
                    print(f"  {flag.decode()}")
            
            # ค้นหา OCG references
            ocg_refs = re.findall(b'/OCG\\s*\\[([^\\]]+)\\]', content)
            print(f"\n[INFO] Found {len(ocg_refs)} OCG references")
            
    except FileNotFoundError:
        print("[!] PDF file not found. This is a demonstration.")
    
    print("\n[+] Flag: flag{h1dd3n_4rt_l4y3rs_r3v34l3d}")


# ============================================
# BONUS: Theory & Background
# ============================================
def bonus_theory():
    """
    ทฤษฎีเบื้องหลัง PDF Layers
    """
    
    print("""
    ╔══════════════════════════════════════════════════════════╗
    ║           PDF LAYERS STEGANOGRAPHY - THEORY              ║
    ╚══════════════════════════════════════════════════════════╝
    
    📚 PDF Layers คืออะไร?
    ═══════════════════════
    
    PDF รองรับ "Optional Content Groups" (OCGs) หรือที่เรียกว่า Layers
    ซึ่งเป็นฟีเจอร์ที่อนุญาตให้ซ่อน/แสดงเนื้อหาบางส่วนได้
    
    ตัวอย่างการใช้งานปกติ:
    - แผนที่ที่มีหลาย layers (ถนน, สถานที่, ฯลฯ)
    - เอกสาร CAD ที่มีรายละเอียดหลายระดับ
    - ฟอร์มที่มีหลายภาษา
    
    
    🔐 Steganography ใน PDF Layers
    ═══════════════════════════════
    
    เทคนิคการซ่อนข้อมูล:
    
    1. Hidden Layers: สร้าง layer ที่ถูกซ่อนโดย default
       - ข้อมูลอยู่ใน PDF แต่ไม่แสดงผล
       - ต้องเปิด layer panel เพื่อดู
    
    2. Transparent Layers: Layer ที่มี opacity = 0
       - มองไม่เห็นแต่ยังอ่าน text ได้
    
    3. Off-page Content: Content ที่อยู่นอกขอบหน้า
       - Print ไม่เห็น แต่อยู่ใน PDF structure
    
    4. White on White: Text สีขาวบนพื้นขาว
       - เปิดให้เห็นโดยเปลี่ยนสีพื้น
    
    
    🛠 Tools สำหรับ Analysis
    ═══════════════════════
    
    GUI Tools:
    • Adobe Acrobat Pro - Full layer control
    • Adobe Acrobat Reader - Basic layer viewing
    • Inkscape - Import PDF as editable
    • PDF-XChange Editor - Layer manipulation
    
    Command Line:
    • pdftk - PDF manipulation
    • mutool - MuPDF toolkit
    • qpdf - PDF transformation
    • pdftotext - Text extraction
    
    Python Libraries:
    • PyMuPDF (fitz) - Powerful PDF manipulation
    • PyPDF2 - Basic PDF reading
    • pdfplumber - Text and table extraction
    • pikepdf - Low-level PDF access
    
    
    🔍 Detection Techniques
    ═══════════════════════
    
    1. Check file size - Hidden content เพิ่มขนาดไฟล์
    2. Extract all text - รวมถึง hidden text
    3. Check for OCG objects ใน PDF structure
    4. Convert to SVG/AI - Layers จะแยกออกมา
    5. Use PDF analyzer tools
    
    
    📖 Further Reading
    ═══════════════════
    
    • PDF Reference 1.7 - Chapter 4.10 (Optional Content)
    • ISO 32000-1:2008 - PDF Standard
    • https://www.adobe.com/devnet/pdf.html
    """)


# ============================================
# Main
# ============================================
if __name__ == "__main__":
    print("=" * 60)
    print("🎨 The Art Gallery's Secret - Solution")
    print("=" * 60)
    
    print("\n[*] Available methods:")
    print("1. PyMuPDF (Python library)")
    print("2. pdftk (Command line)")
    print("3. Inkscape (GUI)")
    print("4. Adobe Acrobat Reader (GUI)")
    print("5. Online Tools")
    print("6. Raw PDF Analysis")
    print("7. Theory & Background")
    
    choice = input("\nSelect method (1-7): ").strip()
    
    methods = {
        "1": method1_pymupdf,
        "2": method2_pdftk,
        "3": method3_inkscape_gui,
        "4": method4_adobe_reader,
        "5": method5_online_tools,
        "6": method6_raw_analysis,
        "7": bonus_theory,
    }
    
    if choice in methods:
        methods[choice]()
    else:
        print("\n[!] Invalid choice. Running method 1...")
        method1_pymupdf()

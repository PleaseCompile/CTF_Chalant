"""
🕵️ Corporate Espionage - Solution
PDF Layers Steganography Challenge

Multiple methods to extract classified data from corporate PDF
"""

# ============================================
# Method 1: Quick & Dirty - Search Raw PDF
# ============================================
def method1_raw_search():
    """
    วิธีที่ 1: ค้นหา flag ตรงๆ จาก raw PDF content
    
    วิธีนี้ใช้ได้เพราะ text ใน PDF layers ยังคงอ่านได้
    แม้จะถูกซ่อนไว้
    """
    import re
    
    pdf_path = "quarterly_report_Q3_2024.pdf"
    
    print("=== Raw PDF Search ===\n")
    
    try:
        with open(pdf_path, 'rb') as f:
            content = f.read()
            
            # ค้นหา flag pattern
            flags = re.findall(b'flag\\{[^}]+\\}', content)
            
            if flags:
                print("[+] Found flags:")
                for flag in flags:
                    print(f"    {flag.decode()}")
            else:
                print("[-] No flags found in raw search")
                
            # ค้นหา CLASSIFIED keyword
            if b'CLASSIFIED' in content:
                print("[+] Found CLASSIFIED content!")
                
    except FileNotFoundError:
        print("[!] PDF file not found (demo mode)")
        print("[+] Expected flag: flag{c0rp0r4t3_s3cr3ts_3xp0s3d}")


# ============================================
# Method 2: PyMuPDF Full Analysis
# ============================================
def method2_pymupdf_full():
    """
    วิธีที่ 2: ใช้ PyMuPDF วิเคราะห์แบบเต็มรูปแบบ
    
    ติดตั้ง: pip install PyMuPDF
    """
    try:
        import fitz
    except ImportError:
        print("[!] PyMuPDF not installed. Run: pip install PyMuPDF")
        return
    
    pdf_path = "quarterly_report_Q3_2024.pdf"
    
    print("=== PyMuPDF Full Analysis ===\n")
    
    try:
        doc = fitz.open(pdf_path)
    except:
        print("[!] Cannot open PDF file (demo mode)")
        print("[+] Expected flag: flag{c0rp0r4t3_s3cr3ts_3xp0s3d}")
        return
    
    # 1. ดู Document Info
    print("[1] Document Information:")
    print(f"    Pages: {len(doc)}")
    print(f"    Metadata: {doc.metadata}")
    
    # 2. วิเคราะห์ Layers (OCGs)
    print("\n[2] Layers Analysis:")
    ocgs = doc.get_ocgs()
    
    if ocgs:
        print(f"    Found {len(ocgs)} layers:")
        for xref, info in ocgs.items():
            name = info.get('name', 'Unnamed')
            state = 'Visible' if info.get('on', True) else 'HIDDEN'
            print(f"    - {name} [{state}] (xref: {xref})")
    else:
        print("    No layers found")
    
    # 3. Extract all text (including hidden)
    print("\n[3] Text Extraction:")
    all_text = ""
    for page_num, page in enumerate(doc):
        text = page.get_text()
        all_text += text
        
        # แสดงตัวอย่าง
        if page_num == 0:
            print(f"    Page 1 preview: {text[:200]}...")
    
    # 4. ค้นหา flag
    print("\n[4] Flag Search:")
    import re
    flags = re.findall(r'flag\{[^}]+\}', all_text)
    classified = re.findall(r'CLASSIFIED[:\s]*(.+)', all_text, re.IGNORECASE)
    
    if flags:
        print(f"    [FLAG FOUND!] {flags}")
    if classified:
        print(f"    [CLASSIFIED DATA!] {classified}")
    
    doc.close()
    
    print("\n[+] Flag: flag{c0rp0r4t3_s3cr3ts_3xp0s3d}")


# ============================================
# Method 3: Forensic Analysis Script
# ============================================
def method3_forensic():
    """
    วิธีที่ 3: วิเคราะห์แบบ Forensic
    
    ตรวจสอบทุกส่วนของ PDF อย่างละเอียด
    """
    import subprocess
    import os
    import tempfile
    
    pdf_path = "quarterly_report_Q3_2024.pdf"
    
    print("=== Forensic Analysis ===\n")
    
    # รายการ commands ที่จะใช้ (as argument lists for security)
    analysis_commands = [
        # ดูข้อมูลไฟล์
        ("File Info", ["file", pdf_path]),
        ("File Size", ["ls", "-la", pdf_path]),
        
        # Extract metadata
        ("Metadata", ["exiftool", pdf_path]),
        
        # Extract text
        ("All Text", ["pdftotext", pdf_path, "-"]),
        
        # PDF structure
        ("PDF Objects", ["mutool", "show", pdf_path, "trailer"]),
        
        # Search for strings (two-step process for piped commands)
        ("Strings Extract", ["strings", pdf_path]),
    ]
    
    for name, cmd_args in analysis_commands:
        print(f"[{name}]")
        print(f"Command: {' '.join(cmd_args)}")
        try:
            result = subprocess.run(
                cmd_args, 
                capture_output=True, 
                text=True,
                timeout=10
            )
            output = result.stdout
            
            # For strings command, filter for flag/classified locally
            if name == "Strings Extract" and output:
                lines = output.split('\n')
                filtered = [l for l in lines if 'flag' in l.lower() or 'classified' in l.lower()]
                if filtered:
                    print(f"Output (filtered):\n" + '\n'.join(filtered[:20]))
                else:
                    print("No flag/classified strings found")
            elif output:
                print(f"Output:\n{output[:500]}")
                
            if result.stderr and 'error' in result.stderr.lower():
                print(f"Error: {result.stderr[:200]}")
        except subprocess.TimeoutExpired:
            print("Command timed out")
        except FileNotFoundError:
            print("Tool not found. Install required tools.")
        except Exception as e:
            print(f"Error: {e}")
        print()
    
    print("[+] Flag: flag{c0rp0r4t3_s3cr3ts_3xp0s3d}")


# ============================================
# Method 4: Convert to SVG
# ============================================
def method4_convert_svg():
    """
    วิธีที่ 4: แปลง PDF เป็น SVG เพื่อดู layers
    
    SVG จะแสดง layers แยกกันเป็น groups
    """
    
    print("""
    === Convert to SVG Method ===
    
    วิธีการ:
    
    1. ใช้ Inkscape command line:
       inkscape --export-type=svg quarterly_report_Q3_2024.pdf
    
    2. หรือใช้ pdf2svg:
       pdf2svg quarterly_report_Q3_2024.pdf output.svg
    
    3. เปิดไฟล์ SVG ด้วย text editor:
       - VSCode, Notepad++, หรือ vim
       
    4. ค้นหาใน SVG:
       - ค้นหา "flag{"
       - ค้นหา "CLASSIFIED"
       - ค้นหา <g> tags ที่มี visibility:hidden
       
    5. ตัวอย่างโครงสร้าง SVG:
    
       <svg>
         <g id="layer1" style="display:inline">
           <!-- Visible content -->
         </g>
         <g id="layer2" style="display:none">
           <!-- HIDDEN CONTENT WITH FLAG -->
           <text>CLASSIFIED: flag{...}</text>
         </g>
       </svg>
    
    6. เปลี่ยน style="display:none" เป็น "display:inline"
       แล้วเปิดใน browser จะเห็น flag
    
    [+] Flag: flag{c0rp0r4t3_s3cr3ts_3xp0s3d}
    """)


# ============================================
# Method 5: PDF-Parser (Didier Stevens Tools)
# ============================================
def method5_pdf_parser():
    """
    วิธีที่ 5: ใช้ pdf-parser.py ของ Didier Stevens
    
    เครื่องมือวิเคราะห์ PDF ระดับ forensic
    """
    
    print("""
    === PDF-Parser Method (Advanced) ===
    
    ติดตั้ง:
    pip install pdf-parser
    
    หรือ download จาก:
    https://blog.didierstevens.com/programs/pdf-tools/
    
    Commands:
    
    1. ดูโครงสร้าง PDF:
       python pdf-parser.py quarterly_report_Q3_2024.pdf
    
    2. ค้นหา OCG (layers):
       python pdf-parser.py --search=/OCG quarterly_report_Q3_2024.pdf
    
    3. ดู object ที่น่าสนใจ:
       python pdf-parser.py --object=<id> quarterly_report_Q3_2024.pdf
    
    4. Extract streams:
       python pdf-parser.py --filter quarterly_report_Q3_2024.pdf
    
    5. ค้นหา text:
       python pdf-parser.py --search=flag quarterly_report_Q3_2024.pdf
       python pdf-parser.py --search=CLASSIFIED quarterly_report_Q3_2024.pdf
    
    [+] Flag: flag{c0rp0r4t3_s3cr3ts_3xp0s3d}
    """)


# ============================================
# Method 6: Python pikepdf (Low-level)
# ============================================
def method6_pikepdf():
    """
    วิธีที่ 6: ใช้ pikepdf สำหรับ low-level PDF access
    
    ติดตั้ง: pip install pikepdf
    """
    
    print("=== pikepdf Low-level Analysis ===\n")
    
    try:
        import pikepdf
    except ImportError:
        print("[!] pikepdf not installed. Run: pip install pikepdf")
        print("[+] Expected flag: flag{c0rp0r4t3_s3cr3ts_3xp0s3d}")
        return
    
    pdf_path = "quarterly_report_Q3_2024.pdf"
    
    try:
        pdf = pikepdf.open(pdf_path)
    except:
        print("[!] Cannot open PDF file (demo mode)")
        print("[+] Expected flag: flag{c0rp0r4t3_s3cr3ts_3xp0s3d}")
        return
    
    # ตรวจสอบ OCProperties (layers config)
    print("[1] Checking Optional Content Properties...")
    
    if '/OCProperties' in pdf.Root:
        oc_props = pdf.Root['/OCProperties']
        print(f"    OCProperties found!")
        print(f"    {oc_props}")
        
        # ดู OCGs
        if '/OCGs' in oc_props:
            ocgs = oc_props['/OCGs']
            print(f"\n    Found {len(ocgs)} layers:")
            for ocg in ocgs:
                print(f"      - {ocg}")
    else:
        print("    No OCProperties found")
    
    # วิเคราะห์แต่ละหน้า
    print("\n[2] Analyzing pages...")
    for i, page in enumerate(pdf.pages):
        print(f"    Page {i+1}: {page.keys()}")
    
    pdf.close()
    
    print("\n[+] Flag: flag{c0rp0r4t3_s3cr3ts_3xp0s3d}")


# ============================================
# Method 7: Adobe Acrobat Pro (GUI - Best)
# ============================================
def method7_acrobat_pro():
    """
    วิธีที่ 7: ใช้ Adobe Acrobat Pro (Full Version)
    
    วิธีที่ง่ายและมีประสิทธิภาพที่สุดสำหรับ GUI
    """
    
    print("""
    === Adobe Acrobat Pro Method (Recommended) ===
    
    Adobe Acrobat Pro มีฟีเจอร์จัดการ layers ที่ครบถ้วนที่สุด
    
    ขั้นตอน:
    
    1. เปิดไฟล์ PDF ด้วย Adobe Acrobat Pro
    
    2. ไปที่ View → Show/Hide → Navigation Panes → Layers
       หรือคลิกไอคอน Layers ในแถบด้านซ้าย
    
    3. จะเห็น Layer Panel แสดง layers ทั้งหมด:
    
       📄 quarterly_report_Q3_2024.pdf
       ├── 📁 Financial Data (👁 visible)
       ├── 📁 Charts (👁 visible)
       └── 📁 Confidential (🚫 hidden)
    
    4. คลิกที่ช่อง checkbox หรือไอคอนตาหน้า "Confidential"
       เพื่อแสดง hidden layer
    
    5. จะเห็นข้อความ:
       "CLASSIFIED: flag{c0rp0r4t3_s3cr3ts_3xp0s3d}"
    
    ฟีเจอร์เพิ่มเติมใน Acrobat Pro:
    - Flatten Layers (รวม layers เข้าด้วยกัน)
    - Export Layers (แยก layers ออกเป็นไฟล์)
    - Layer Properties (ดูและแก้ไข settings)
    
    [+] Flag: flag{c0rp0r4t3_s3cr3ts_3xp0s3d}
    """)


# ============================================
# BONUS: Automated Flag Extractor
# ============================================
def bonus_auto_extract():
    """
    สคริปต์อัตโนมัติสำหรับ extract flags จาก PDF
    ลองทุกวิธีที่เป็นไปได้
    """
    import re
    import subprocess
    
    pdf_path = "quarterly_report_Q3_2024.pdf"
    found_flags = set()
    
    print("=== Automated Flag Extractor ===\n")
    
    # Method A: Raw binary search
    print("[A] Searching raw binary...")
    try:
        with open(pdf_path, 'rb') as f:
            content = f.read()
            flags = re.findall(b'flag\\{[^}]+\\}', content)
            for flag in flags:
                found_flags.add(flag.decode())
    except:
        pass
    
    # Method B: pdftotext
    print("[B] Trying pdftotext...")
    try:
        result = subprocess.run(
            ["pdftotext", pdf_path, "-"],
            capture_output=True, text=True
        )
        flags = re.findall(r'flag\{[^}]+\}', result.stdout)
        found_flags.update(flags)
    except:
        pass
    
    # Method C: PyMuPDF
    print("[C] Trying PyMuPDF...")
    try:
        import fitz
        doc = fitz.open(pdf_path)
        for page in doc:
            text = page.get_text()
            flags = re.findall(r'flag\{[^}]+\}', text)
            found_flags.update(flags)
        doc.close()
    except:
        pass
    
    # Method D: strings command
    print("[D] Trying strings...")
    try:
        result = subprocess.run(
            ["strings", pdf_path],
            capture_output=True, text=True
        )
        flags = re.findall(r'flag\{[^}]+\}', result.stdout)
        found_flags.update(flags)
    except:
        pass
    
    # แสดงผลลัพธ์
    print("\n" + "=" * 40)
    if found_flags:
        print("[SUCCESS] Flags found:")
        for flag in found_flags:
            print(f"  🚩 {flag}")
    else:
        print("[INFO] No flags found automatically")
        print("[+] Expected flag: flag{c0rp0r4t3_s3cr3ts_3xp0s3d}")


# ============================================
# Main
# ============================================
if __name__ == "__main__":
    print("=" * 60)
    print("🕵️ Corporate Espionage - Solution")
    print("=" * 60)
    
    print("\n[*] Available methods:")
    print("1. Raw PDF Search (Quick)")
    print("2. PyMuPDF Full Analysis")
    print("3. Forensic Analysis")
    print("4. Convert to SVG")
    print("5. PDF-Parser (Advanced)")
    print("6. pikepdf Low-level")
    print("7. Adobe Acrobat Pro (GUI)")
    print("8. Automated Flag Extractor")
    
    choice = input("\nSelect method (1-8): ").strip()
    
    methods = {
        "1": method1_raw_search,
        "2": method2_pymupdf_full,
        "3": method3_forensic,
        "4": method4_convert_svg,
        "5": method5_pdf_parser,
        "6": method6_pikepdf,
        "7": method7_acrobat_pro,
        "8": bonus_auto_extract,
    }
    
    if choice in methods:
        methods[choice]()
    else:
        print("\n[!] Invalid choice. Running automated extractor...")
        bonus_auto_extract()

"""
The Clock Tower's Secret - Solution
ความลับของหอนาฬิกา - เฉลย

Challenge: Decode bell chimes using modular arithmetic on a 26-letter alphabet
Concept: Modular Maze / Modular Arithmetic Cipher (Clock-based)

Multiple Methods:
1. Manual calculation (pen & paper)
2. Python script (automated)
3. Online tools (modular calculator)
"""

import hashlib


def method1_manual():
    """
    วิธีที่ 1: Manual Calculation (คำนวณด้วยมือ)
    
    หลักการ: ใช้ modulo (%) เพื่อ wrap ค่าให้อยู่ในขอบเขต 0-25
    
    สูตร: 
    - position = value % 26
    - letter = chr(65 + position)  # 65 = ASCII code of 'A'
    
    สำหรับตัวเลขติดลบ:
    - ถ้า value < 0: position = (value % 26 + 26) % 26
    - หรือง่ายๆ: value + 26 (ถ้า value อยู่ระหว่าง -26 ถึง 0)
    
    ตัวอย่าง:
    28 → 28 % 26 = 2 → ตัวอักษร C
    -18 → -18 % 26 = 8 → ตัวอักษร I (Python handles this correctly)
    """
    print("=" * 50)
    print("METHOD 1: Manual Calculation")
    print("=" * 50)
    
    # Encoded bell chimes
    chimes = [28, 50, 54, 37, -18, 80]
    
    print(f"\nAlphabet Size (Modulus): 26")
    print(f"Formula: value % 26")
    print("-" * 50)
    
    result = ""
    
    for i, value in enumerate(chimes, 1):
        position = value % 26
        letter = chr(65 + position)  # A=65 in ASCII
        result += letter
        
        # Show calculation
        if value < 0:
            print(f"Step {i}: {value}")
            print(f"        → Negative! Think: {value} + 26 = {value + 26}")
            print(f"        → Or: {value} % 26 = {position}")
        else:
            quotient = value // 26
            remainder = value % 26
            print(f"Step {i}: {value}")
            print(f"        → {value} = {quotient} × 26 + {remainder}")
            print(f"        → {value} % 26 = {position}")
        
        print(f"        → Position {position} = '{letter}'")
        print()
    
    print(f"Decoded Message: {result}")
    return result


def method2_script():
    """
    วิธีที่ 2: Python Script (Automated)
    
    ใช้ list comprehension และ modulo operation
    """
    print("=" * 50)
    print("METHOD 2: Python Script (Automated)")
    print("=" * 50)
    
    def decode_value(value):
        """Convert encoded value to letter using mod 26"""
        position = value % 26
        return chr(65 + position)
    
    chimes = [28, 50, 54, 37, -18, 80]
    
    # One-liner solution
    result = ''.join(decode_value(v) for v in chimes)
    
    # Alternative one-liner
    result_alt = ''.join(chr(65 + (v % 26)) for v in chimes)
    
    print(f"\nOne-liner solution:")
    print(f"result = ''.join(chr(65 + (v % 26)) for v in chimes)")
    print(f"\nDecoded Message: {result}")
    
    return result


def method3_online_tools():
    """
    วิธีที่ 3: ใช้เครื่องมือออนไลน์
    
    1. Modular Calculator:
       - https://www.calculator.net/modulo-calculator.html
       - คำนวณ value % 26 ทีละตัว
    
    2. Python Online (repl.it, python.org):
       - รัน: print(28 % 26)  # ได้ 2
       - รัน: print(-18 % 26)  # ได้ 8 (Python handles negative mod correctly)
    
    3. Spreadsheet (Excel/Google Sheets):
       - ใช้ =MOD(28, 26) เพื่อหาเศษ
       - ใช้ =CHAR(65 + MOD(value, 26)) เพื่อแปลงเป็นตัวอักษร
    """
    print("=" * 50)
    print("METHOD 3: Online Tools")
    print("=" * 50)
    
    instructions = """
    🔧 เครื่องมือที่แนะนำ:
    
    1. 🧮 Modular Calculator
       URL: https://www.calculator.net/modulo-calculator.html
       วิธีใช้: ใส่ตัวเลข, เลือก mod 26
       
       ⚠️ หมายเหตุ: บาง calculator ไม่รองรับ negative mod
       ถ้า -18 mod 26 ให้ค่าผิด ให้ใช้: -18 + 26 = 8
    
    2. 🐍 Python Online
       URL: https://www.python.org/shell/
       พิมพ์: 
         >>> 28 % 26
         2
         >>> -18 % 26
         8
    
    3. 📊 Google Sheets Formula
       =MOD(A1, 26)  → คำนวณ A1 mod 26
       
       ตัวอย่างตาราง:
       | Value | Value%26 | Letter |
       |-------|----------|--------|
       |  28   |    2     |   C    |
       |  50   |   24     |   Y    |
       |  54   |    2     |   C    |
       |  37   |   11     |   L    |
       | -18   |    8     |   I    |
       |  80   |    2     |   C    |
    
    4. 🔤 ASCII Conversion
       Position = value % 26
       Letter = chr(65 + Position)
       
       Example: 28 % 26 = 2, chr(65+2) = chr(67) = 'C'
    """
    print(instructions)
    
    # Still calculate the answer
    chimes = [28, 50, 54, 37, -18, 80]
    result = ''.join(chr(65 + (v % 26)) for v in chimes)
    
    print(f"Decoded Message: {result}")
    return result


def bonus_theory():
    """
    Bonus: ทฤษฎี Modular Arithmetic และ Negative Numbers
    
    การจัดการกับตัวเลขติดลบใน modular arithmetic:
    
    1. Python: -18 % 26 = 8 (ถูกต้องตามนิยามทางคณิตศาสตร์)
    2. C/Java: -18 % 26 = -18 (truncated toward zero)
    
    นิยามทางคณิตศาสตร์:
    a mod n = a - n * floor(a/n)
    
    -18 mod 26:
    floor(-18/26) = floor(-0.69) = -1
    -18 - 26 * (-1) = -18 + 26 = 8
    
    ใช้ในการเข้ารหัส:
    - ทำให้ค่าอยู่ในช่วงที่กำหนดเสมอ
    - สะดวกสำหรับ "wrap around" ทั้งซ้ายและขวา
    """
    print("=" * 50)
    print("BONUS: Modular Arithmetic Theory")
    print("=" * 50)
    
    theory = """
    📚 ทฤษฎี Modular Arithmetic (เลขคณิตมอดุลาร์)
    
    🔄 การจัดการตัวเลขติดลบ:
    
    Python (ถูกต้องตามคณิตศาสตร์):
    - -18 % 26 = 8
    - ผลลัพธ์มีเครื่องหมายเดียวกับ divisor (26 เป็นบวก → ผลลัพธ์เป็นบวก)
    
    C/Java (truncated):
    - -18 % 26 = -18
    - ต้องปรับด้วย: ((-18 % 26) + 26) % 26 = 8
    
    📐 สูตร Universal (ใช้ได้กับทุกภาษา):
    def safe_mod(a, n):
        return ((a % n) + n) % n
    
    🕐 Clock Analogy:
    - นาฬิกา 26 ชั่วโมง
    - เดินหน้า 28 ก้าว = อยู่ที่ตำแหน่ง 2
    - ถอยหลัง 18 ก้าว = อยู่ที่ตำแหน่ง 8 (26 - 18 = 8)
    
    🎯 ใช้ในโจทย์นี้:
    - Alphabet = 26 ตัวอักษร (A=0 ถึง Z=25)
    - ตัวเลขใดๆ % 26 = ตำแหน่งบน "หน้าปัดตัวอักษร"
    """
    print(theory)


def generate_flag(message):
    """สร้าง flag จาก decoded message"""
    # Convert to lowercase, remove spaces
    clean_message = message.lower().replace(" ", "")
    
    # Generate MD5 hash
    md5_hash = hashlib.md5(clean_message.encode()).hexdigest()
    
    flag = f"flag{{{md5_hash}}}"
    return flag


def main():
    """รันทุก method และแสดง flag"""
    print("\n" + "🕰️" * 25)
    print(" THE CLOCK TOWER'S SECRET - SOLUTION ")
    print("🕰️" * 25 + "\n")
    
    # Run all methods
    result1 = method1_manual()
    print("\n")
    result2 = method2_script()
    print("\n")
    result3 = method3_online_tools()
    print("\n")
    bonus_theory()
    
    # Verify all methods give same result
    print("\n" + "=" * 50)
    print("VERIFICATION & FLAG")
    print("=" * 50)
    
    if result1 == result2 == result3:
        print(f"✅ All methods agree!")
        print(f"   Decoded message: {result1}")
        
        flag = generate_flag(result1)
        print(f"\n🚩 FLAG: {flag}")
        
        print(f"\n💡 ความหมาย: '{result1}' หมายถึง 'เป็นวงกลม/หมุนเวียน'")
        print(f"   สื่อถึงธรรมชาติของ modular arithmetic ที่ 'วนกลับ' เสมอ!")
    else:
        print("❌ Methods disagree! Check the solution.")
        print(f"   Method 1: {result1}")
        print(f"   Method 2: {result2}")
        print(f"   Method 3: {result3}")


if __name__ == "__main__":
    main()

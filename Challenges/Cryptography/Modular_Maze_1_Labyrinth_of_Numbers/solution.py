"""
The Labyrinth of Numbers - Solution
เขาวงกตแห่งตัวเลข - เฉลย

Challenge: Decode coordinates using modular arithmetic on a 5x5 grid
Concept: Modular Maze / Modular Arithmetic Cipher

Multiple Methods:
1. Manual calculation (pen & paper)
2. Python script (automated)
3. Online tools (modular calculator)
"""

import hashlib


def create_grid():
    """สร้างตาราง 5x5 ที่แมปตัวอักษร A-Y"""
    grid = {}
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXY'  # 25 letters (Z is special case)
    index = 0
    for row in range(5):
        for col in range(5):
            grid[(row, col)] = alphabet[index]
            index += 1
    return grid


def method1_manual():
    """
    วิธีที่ 1: Manual Calculation (คำนวณด้วยมือ)
    
    หลักการ: ใช้ modulo (%) เพื่อ wrap coordinates ให้อยู่ในขอบเขต 0-4
    
    สูตร: 
    - new_row = original_row % 5
    - new_col = original_col % 5
    
    ตัวอย่าง:
    (7, 3) → (7 % 5, 3 % 5) = (2, 3) → ตาราง[2][3] = N
    """
    print("=" * 50)
    print("METHOD 1: Manual Calculation")
    print("=" * 50)
    
    # Grid mapping
    grid = [
        ['A', 'B', 'C', 'D', 'E'],  # row 0
        ['F', 'G', 'H', 'I', 'J'],  # row 1
        ['H', 'I', 'J', 'K', 'L'],  # row 2
        ['P', 'Q', 'R', 'S', 'T'],  # row 3
        ['U', 'V', 'W', 'X', 'Y'],  # row 4
    ]
    
    # Correct grid
    grid = [
        ['A', 'B', 'C', 'D', 'E'],  # row 0
        ['F', 'G', 'H', 'I', 'J'],  # row 1
        ['K', 'L', 'M', 'N', 'O'],  # row 2
        ['P', 'Q', 'R', 'S', 'T'],  # row 3
        ['U', 'V', 'W', 'X', 'Y'],  # row 4
    ]
    
    coordinates = [
        (54, 27),  # 1: W
        (18, 47),  # 2: R
        (35, 25),  # 3: A
        (53, 35),  # 4: P
        (18, 30),  # 5: P
        (45, 39),  # 6: E
        (30, 53),  # 7: D
    ]
    
    grid_size = 5
    result = ""
    
    print(f"\nGrid Size: {grid_size}")
    print(f"Formula: (row % {grid_size}, col % {grid_size})")
    print("-" * 50)
    
    for i, (row, col) in enumerate(coordinates, 1):
        new_row = row % grid_size
        new_col = col % grid_size
        letter = grid[new_row][new_col]
        result += letter
        
        print(f"Step {i}: ({row}, {col})")
        print(f"        → ({row} % 5, {col} % 5)")
        print(f"        → ({new_row}, {new_col})")
        print(f"        → Letter: {letter}")
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
    
    # Create alphabet grid using formula: letter = chr(65 + row*5 + col)
    def get_letter(row, col, grid_size=5):
        actual_row = row % grid_size
        actual_col = col % grid_size
        index = actual_row * grid_size + actual_col
        return chr(65 + index)  # A=65 in ASCII
    
    coordinates = [
        (54, 27), (18, 47), (35, 25), (53, 35),
        (18, 30), (45, 39), (30, 53)
    ]
    
    # One-liner solution
    result = ''.join(get_letter(r, c) for r, c in coordinates)
    
    print(f"\nOne-liner solution:")
    print(f"result = ''.join(chr(65 + (r%5)*5 + (c%5)) for r,c in coordinates)")
    print(f"\nDecoded Message: {result}")
    
    return result


def method3_online_tools():
    """
    วิธีที่ 3: ใช้เครื่องมือออนไลน์
    
    1. Modular Calculator:
       - https://www.calculator.net/modulo-calculator.html
       - คำนวณ row % 5 และ col % 5 ทีละคู่
    
    2. Python Online (repl.it, python.org):
       - รัน: print(7 % 5)  # ได้ 2
       - รัน: print(3 % 5)  # ได้ 3
    
    3. Spreadsheet (Excel/Google Sheets):
       - ใช้ =MOD(7, 5) เพื่อหาเศษ
       - สร้างตาราง lookup สำหรับตัวอักษร
    """
    print("=" * 50)
    print("METHOD 3: Online Tools")
    print("=" * 50)
    
    instructions = """
    🔧 เครื่องมือที่แนะนำ:
    
    1. 🧮 Modular Calculator
       URL: https://www.calculator.net/modulo-calculator.html
       วิธีใช้: ใส่ตัวเลข, เลือก mod 5
    
    2. 🐍 Python Online
       URL: https://www.python.org/shell/
       พิมพ์: 7 % 5  → ได้ 2
    
    3. 📊 Google Sheets Formula
       =MOD(A1, 5)  → คำนวณ A1 mod 5
       
       ตัวอย่างตาราง:
       | Row | Col | Row%5 | Col%5 | Index | Letter |
       |-----|-----|-------|-------|-------|--------|
       |  7  |  3  |   2   |   3   |  13   |   N    |
       | 12  |  9  |   2   |   4   |  14   |   O    |
       | ... | ... |  ...  |  ...  | ...   |  ...   |
    
    4. 🔤 ASCII Calculation
       Index = (row % 5) * 5 + (col % 5)
       Letter = chr(65 + Index)
       
       Example: row=7, col=3
       Index = (7%5)*5 + (3%5) = 2*5 + 3 = 13
       Letter = chr(65+13) = chr(78) = 'N'
    """
    print(instructions)
    
    # Still calculate the answer
    coordinates = [(54, 27), (18, 47), (35, 25), (53, 35),
                   (18, 30), (45, 39), (30, 53)]
    result = ''.join(chr(65 + (r%5)*5 + (c%5)) for r, c in coordinates)
    
    print(f"Decoded Message: {result}")
    return result


def bonus_theory():
    """
    Bonus: ทฤษฎี Modular Arithmetic
    
    Modular Arithmetic คือการคำนวณที่ "วน" เมื่อถึงค่าสูงสุด
    
    ตัวอย่างในชีวิตจริง:
    - นาฬิกา: 13:00 = 1:00 (mod 12)
    - วันในสัปดาห์: วันที่ 8 = วันที่ 1 (mod 7)
    - เกมกระดาน: วนกลับช่องแรกเมื่อเดินเกินกระดาน
    
    ในโจทย์นี้:
    - Grid size = 5 (Modulus)
    - Position (7, 3) → (7 mod 5, 3 mod 5) = (2, 3)
    - เหมือนเดินบนกระดานที่ "ต่อขอบ" กัน
    
    การประยุกต์ใช้ในการเข้ารหัส:
    - Caesar Cipher: shift mod 26
    - RSA: (message^e) mod n
    - Diffie-Hellman: (g^a) mod p
    """
    print("=" * 50)
    print("BONUS: Modular Arithmetic Theory")
    print("=" * 50)
    
    theory = """
    📚 ทฤษฎี Modular Arithmetic (เลขคณิตมอดุลาร์)
    
    สูตรพื้นฐาน: a mod n = เศษเหลือจากการหาร a ด้วย n
    
    ตัวอย่าง:
    - 7 mod 5 = 2  (7 = 1×5 + 2)
    - 12 mod 5 = 2 (12 = 2×5 + 2)
    - 23 mod 5 = 3 (23 = 4×5 + 3)
    
    🔄 คุณสมบัติ "Wrap Around":
    0 → 1 → 2 → 3 → 4 → 0 → 1 → 2 → ...
    
    🎮 การประยุกต์ใช้ใน Modular Maze:
    - ใช้ตาราง NxN (ในโจทย์นี้ N=5)
    - พิกัดที่เกิน N จะ "วน" กลับมา
    - (row % N, col % N) ให้ตำแหน่งจริงบนตาราง
    
    🔐 ใช้ใน Cryptography:
    - Caesar Cipher: (char + shift) % 26
    - Vigenère Cipher: แต่ละตัวอักษร shift ต่างกัน mod 26
    - Modern Encryption: ใช้ modular exponentiation
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
    print("\n" + "🌀" * 25)
    print(" THE LABYRINTH OF NUMBERS - SOLUTION ")
    print("🌀" * 25 + "\n")
    
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
    else:
        print("❌ Methods disagree! Check the solution.")
        print(f"   Method 1: {result1}")
        print(f"   Method 2: {result2}")
        print(f"   Method 3: {result3}")


if __name__ == "__main__":
    main()

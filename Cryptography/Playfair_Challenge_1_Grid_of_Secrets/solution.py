"""
The Grid of Secrets - Solution
Playfair Cipher Decryption Challenge

Multiple methods: Manual, Script, Online Tools
Key: MONARCHY
"""

def create_playfair_matrix(key):
    """สร้างตาราง Playfair 5x5 จาก key"""
    # ลบตัวซ้ำและแทน J ด้วย I
    key = key.upper().replace('J', 'I')
    
    # สร้าง matrix โดยเริ่มจาก key แล้วตามด้วย A-Z (ยกเว้น J)
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # ไม่มี J
    
    matrix = []
    used = set()
    
    # เพิ่มตัวอักษรจาก key
    for char in key:
        if char not in used and char in alphabet:
            matrix.append(char)
            used.add(char)
    
    # เพิ่มตัวอักษรที่เหลือ
    for char in alphabet:
        if char not in used:
            matrix.append(char)
            used.add(char)
    
    # แปลงเป็น 5x5 matrix
    return [matrix[i:i+5] for i in range(0, 25, 5)]


def print_matrix(matrix):
    """แสดงตาราง"""
    print("\n=== Playfair Matrix (Key: MONARCHY) ===")
    for row in matrix:
        print(' '.join(row))
    print()


def find_position(matrix, char):
    """หาตำแหน่งของตัวอักษรในตาราง"""
    char = char.upper()
    if char == 'J':
        char = 'I'
    
    for i, row in enumerate(matrix):
        for j, c in enumerate(row):
            if c == char:
                return (i, j)
    return None


def decrypt_pair(matrix, char1, char2):
    """ถอดรหัสคู่ตัวอักษร"""
    row1, col1 = find_position(matrix, char1)
    row2, col2 = find_position(matrix, char2)
    
    if row1 == row2:
        # แถวเดียวกัน: เลื่อนซ้าย
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:
        # คอลัมน์เดียวกัน: เลื่อนขึ้น
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:
        # ต่างแถวต่างคอลัมน์: สลับคอลัมน์ (rectangle rule)
        return matrix[row1][col2] + matrix[row2][col1]


def decrypt_playfair(ciphertext, key):
    """ถอดรหัส Playfair cipher"""
    matrix = create_playfair_matrix(key)
    
    # ทำความสะอาด ciphertext
    ciphertext = ''.join(c for c in ciphertext.upper() if c.isalpha())
    ciphertext = ciphertext.replace('J', 'I')
    
    # ถอดรหัสทีละคู่
    plaintext = ''
    for i in range(0, len(ciphertext), 2):
        if i + 1 < len(ciphertext):
            plaintext += decrypt_pair(matrix, ciphertext[i], ciphertext[i+1])
        else:
            plaintext += ciphertext[i]
    
    return plaintext


def encrypt_playfair(plaintext, key):
    """เข้ารหัส Playfair cipher (สำหรับตรวจสอบ)"""
    matrix = create_playfair_matrix(key)
    
    # เตรียม plaintext
    plaintext = ''.join(c for c in plaintext.upper() if c.isalpha())
    plaintext = plaintext.replace('J', 'I')
    
    # แทรก X ระหว่างตัวอักษรซ้ำ
    prepared = ''
    i = 0
    while i < len(plaintext):
        prepared += plaintext[i]
        if i + 1 < len(plaintext):
            if plaintext[i] == plaintext[i + 1]:
                prepared += 'X'
            else:
                prepared += plaintext[i + 1]
                i += 1
        i += 1
    
    # เพิ่ม X ถ้าความยาวเป็นเลขคี่
    if len(prepared) % 2 == 1:
        prepared += 'X'
    
    # เข้ารหัสทีละคู่
    ciphertext = ''
    for i in range(0, len(prepared), 2):
        row1, col1 = find_position(matrix, prepared[i])
        row2, col2 = find_position(matrix, prepared[i+1])
        
        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2] + matrix[row2][col1]
    
    return ciphertext


def method1_manual():
    """วิธีที่ 1: ทำด้วยมือ (Manual)"""
    print("=" * 60)
    print("วิธีที่ 1: Manual Decryption")
    print("=" * 60)
    
    key = "MONARCHY"
    ciphertext = "GATLMZCLRQXA"
    
    # ขั้นตอนที่ 1: สร้างตาราง
    print("\n📝 ขั้นตอนที่ 1: สร้างตาราง Playfair จาก key 'MONARCHY'")
    print("   - เริ่มจาก MONARCHY (ไม่มีตัวซ้ำ)")
    print("   - ตามด้วยตัวอักษรที่เหลือ (ไม่รวม J)")
    
    matrix = create_playfair_matrix(key)
    print_matrix(matrix)
    
    # ขั้นตอนที่ 2: แบ่งคู่
    print("📝 ขั้นตอนที่ 2: แบ่ง ciphertext เป็นคู่")
    pairs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
    print(f"   {ciphertext} -> {pairs}")
    
    # ขั้นตอนที่ 3: ถอดรหัสแต่ละคู่
    print("\n📝 ขั้นตอนที่ 3: ถอดรหัสแต่ละคู่")
    
    plaintext = ''
    for pair in pairs:
        char1, char2 = pair[0], pair[1]
        pos1, pos2 = find_position(matrix, char1), find_position(matrix, char2)
        decrypted = decrypt_pair(matrix, char1, char2)
        plaintext += decrypted
        
        print(f"   {pair}: {char1}({pos1}) + {char2}({pos2}) -> {decrypted}")
    
    print(f"\n🔓 Decrypted text: {plaintext}")
    
    # ลบ X ที่เป็น padding
    cleaned = plaintext.replace('X', '')
    print(f"🎯 Cleaned text: {cleaned}")
    print(f"\n🚩 FLAG: flag{{{cleaned.lower()}}}")


def method2_script():
    """วิธีที่ 2: ใช้ Script อัตโนมัติ"""
    print("\n" + "=" * 60)
    print("วิธีที่ 2: Automated Script")
    print("=" * 60)
    
    key = "MONARCHY"
    ciphertext = "GATLMZCLRQXA"
    
    plaintext = decrypt_playfair(ciphertext, key)
    cleaned = plaintext.replace('X', '')
    
    print(f"\n📝 Key: {key}")
    print(f"📝 Ciphertext: {ciphertext}")
    print(f"🔓 Plaintext: {plaintext}")
    print(f"🎯 Cleaned: {cleaned}")
    print(f"\n🚩 FLAG: flag{{{cleaned.lower()}}}")
    
    return cleaned.lower()


def method3_online():
    """วิธีที่ 3: ใช้เครื่องมือออนไลน์"""
    print("\n" + "=" * 60)
    print("วิธีที่ 3: Online Tools")
    print("=" * 60)
    
    print("""
🌐 เว็บไซต์ที่ใช้ถอดรหัส Playfair Cipher:

1. CyberChef:
   URL: https://gchq.github.io/CyberChef/
   - ค้นหา "Playfair" ใน Operations
   - ใส่ Key: MONARCHY
   - ใส่ Ciphertext: GATLMZCLRQXA
   - เลือก Decrypt

2. dCode:
   URL: https://www.dcode.fr/playfair-cipher
   - ใส่ ciphertext
   - ใส่ key
   - กดปุ่ม Decrypt

3. Boxentriq:
   URL: https://www.boxentriq.com/code-breaking/playfair-cipher
   - ใส่ข้อมูลและ key
   - กด Decode

📝 ข้อมูลที่ต้องใส่:
   - Ciphertext: GATLMZCLRQXA
   - Key: MONARCHY
""")


def bonus_theory():
    """Bonus: ทฤษฎีและประวัติของ Playfair Cipher"""
    print("\n" + "=" * 60)
    print("Bonus: Playfair Cipher Theory & History")
    print("=" * 60)
    
    print("""
📚 ประวัติ Playfair Cipher:
   - ถูกประดิษฐ์โดย Charles Wheatstone ในปี 1854
   - แต่ถูกตั้งชื่อตาม Lord Playfair ที่ช่วยเผยแพร่
   - ใช้ในสงครามโลกครั้งที่ 1 โดยกองทัพอังกฤษ

📐 กฎการเข้ารหัส:
   1. สร้างตาราง 5x5 จาก keyword + ตัวอักษรที่เหลือ
   2. I และ J ใช้ช่องเดียวกัน (25 ช่อง = 25 ตัวอักษร)
   3. แบ่งข้อความเป็นคู่ (ถ้าซ้ำใส่ X คั่น)
   4. เข้ารหัสตามตำแหน่ง:
      - แถวเดียวกัน: เลื่อนขวา
      - คอลัมน์เดียวกัน: เลื่อนลง
      - ต่างแถวต่างคอลัมน์: สลับคอลัมน์

🔓 กฎการถอดรหัส:
   - ทำตรงข้ามกับการเข้ารหัส
   - แถวเดียวกัน: เลื่อนซ้าย
   - คอลัมน์เดียวกัน: เลื่อนขึ้น
   - ต่างแถวต่างคอลัมน์: สลับคอลัมน์ (เหมือนเดิม)

🎯 จุดแข็ง:
   - ยากกว่า simple substitution cipher
   - ต้องวิเคราะห์ digraph (คู่ตัวอักษร)

⚠️ จุดอ่อน:
   - ยังคงถูก frequency analysis ได้
   - key สั้นๆ อาจถูก brute force ได้
""")


def verify_solution():
    """ตรวจสอบว่า solution ถูกต้อง"""
    print("\n" + "=" * 60)
    print("Verification")
    print("=" * 60)
    
    key = "MONARCHY"
    expected_plaintext = "SECRETXDATA"  # ตัวอักษรที่คาดหวัง
    
    # เข้ารหัส expected plaintext
    encrypted = encrypt_playfair(expected_plaintext, key)
    print(f"📝 Plaintext: {expected_plaintext}")
    print(f"🔒 Encrypted: {encrypted}")
    
    # ถอดรหัสกลับ
    decrypted = decrypt_playfair(encrypted, key)
    print(f"🔓 Decrypted: {decrypted}")
    
    print(f"\n✅ Verification: {'PASS' if decrypted == expected_plaintext else 'FAIL'}")


if __name__ == "__main__":
    print("🔐 The Grid of Secrets - Solution")
    print("=" * 60)
    
    method1_manual()
    method2_script()
    method3_online()
    bonus_theory()
    verify_solution()
    
    print("\n" + "=" * 60)
    print("🎉 FINAL ANSWER")
    print("=" * 60)
    print("🚩 flag{instruments}")

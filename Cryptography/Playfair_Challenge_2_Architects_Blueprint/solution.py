"""
The Architect's Blueprint - Solution
Playfair Cipher Decryption Challenge (Advanced)

Multiple methods: Manual, Script, Online Tools
Key: KINGDOMHAL (derived from "KINGDOM HALL")
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
    print("\n=== Playfair Matrix ===")
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
    """เข้ารหัส Playfair cipher (สำหรับสร้างโจทย์)"""
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


def extract_key_from_name(building_name):
    """สกัด key จากชื่ออาคาร"""
    name = building_name.upper().replace(' ', '').replace('J', 'I')
    
    key = ''
    used = set()
    for char in name:
        if char.isalpha() and char not in used:
            key += char
            used.add(char)
    
    return key


def method1_step_by_step():
    """วิธีที่ 1: ทำทีละขั้นตอน (Manual)"""
    print("=" * 60)
    print("วิธีที่ 1: Step-by-Step Manual Decryption")
    print("=" * 60)
    
    building_name = "KINGDOM HALL"
    ciphertext = "MNNZNPGSSQSA"
    
    # ขั้นตอนที่ 1: สกัด Key
    print("\n📝 ขั้นตอนที่ 1: สกัด Key จากชื่ออาคาร")
    print(f"   ชื่ออาคาร: {building_name}")
    print(f"   ลบช่องว่าง: KINGDOMHALL")
    print(f"   ลบตัวซ้ำ (L ซ้ำ): KINGDOMHAL")
    
    key = extract_key_from_name(building_name)
    print(f"   Key: {key}")
    
    # ขั้นตอนที่ 2: สร้างตาราง
    print("\n📝 ขั้นตอนที่ 2: สร้างตาราง Playfair 5x5")
    print(f"   เริ่มจาก key: {key}")
    print("   ตามด้วยตัวอักษรที่เหลือ (ไม่รวม J)")
    
    matrix = create_playfair_matrix(key)
    print_matrix(matrix)
    
    # ขั้นตอนที่ 3: แบ่งคู่
    print("📝 ขั้นตอนที่ 3: แบ่ง ciphertext เป็นคู่")
    pairs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
    print(f"   {ciphertext} -> {pairs}")
    
    # ขั้นตอนที่ 4: ถอดรหัส
    print("\n📝 ขั้นตอนที่ 4: ถอดรหัสแต่ละคู่")
    
    plaintext = ''
    for pair in pairs:
        char1, char2 = pair[0], pair[1]
        pos1, pos2 = find_position(matrix, char1), find_position(matrix, char2)
        decrypted = decrypt_pair(matrix, char1, char2)
        plaintext += decrypted
        
        # แสดงกฎที่ใช้
        rule = ""
        if pos1[0] == pos2[0]:
            rule = "Same Row → Shift Left"
        elif pos1[1] == pos2[1]:
            rule = "Same Column → Shift Up"
        else:
            rule = "Rectangle → Swap Columns"
        
        print(f"   {pair}: {char1}{pos1} + {char2}{pos2} [{rule}] -> {decrypted}")
    
    print(f"\n🔓 Decrypted text: {plaintext}")
    
    # ลบ X ที่เป็น padding
    cleaned = plaintext.replace('X', '')
    print(f"🎯 Cleaned text: {cleaned}")
    print(f"\n🚩 FLAG: flag{{{cleaned.lower()}}}")
    
    return cleaned.lower()


def method2_script():
    """วิธีที่ 2: ใช้ Script อัตโนมัติ"""
    print("\n" + "=" * 60)
    print("วิธีที่ 2: Automated Script")
    print("=" * 60)
    
    building_name = "KINGDOM HALL"
    ciphertext = "MNNZNPGSSQSA"
    
    key = extract_key_from_name(building_name)
    plaintext = decrypt_playfair(ciphertext, key)
    cleaned = plaintext.replace('X', '')
    
    print(f"\n📝 Building Name: {building_name}")
    print(f"📝 Extracted Key: {key}")
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
   - ใส่ Key: KINGDOMHAL
   - ใส่ Ciphertext: MNNZNPGSSQSA
   - เลือก Decrypt

2. dCode:
   URL: https://www.dcode.fr/playfair-cipher
   - ใส่ ciphertext: MNNZNPGSSQSA
   - ใส่ key: KINGDOMHAL
   - กดปุ่ม Decrypt

3. Boxentriq:
   URL: https://www.boxentriq.com/code-breaking/playfair-cipher
   - ใส่ข้อมูลและ key
   - กด Decode

📝 ข้อมูลที่ต้องใส่:
   - Ciphertext: MNNZNPGSSQSA
   - Key: KINGDOMHAL (สกัดจาก "KINGDOM HALL")
""")


def method4_key_discovery():
    """วิธีที่ 4: การค้นหา Key (สำหรับ Advanced Players)"""
    print("\n" + "=" * 60)
    print("วิธีที่ 4: Key Discovery Process")
    print("=" * 60)
    
    print("""
🔍 ขั้นตอนการค้นหา Key จาก Hints:

1. อ่าน Story:
   - "กุญแจสู่ความลับอยู่ในชื่ออาคารที่ฉันรักที่สุด"
   - อาคารที่รัก = "KINGDOM HALL"

2. สกัด Key:
   - ลบช่องว่าง: KINGDOMHALL
   - ลบตัวอักษรซ้ำ: KINGDOMHAL
   - J แทนด้วย I (ไม่มี J ในชื่อนี้)

3. ตรวจสอบ:
   - Key = KINGDOMHAL (10 ตัวอักษร)
   - ใช้สร้างตาราง 5x5

💡 Tips:
   - ชื่อ "Sir Charles W." อาจหมายถึง Charles Wheatstone
   - ผู้ประดิษฐ์ Playfair cipher!
""")


def bonus_theory():
    """Bonus: เปรียบเทียบกับ Challenge 1"""
    print("\n" + "=" * 60)
    print("Bonus: Challenge Comparison")
    print("=" * 60)
    
    print("""
📊 เปรียบเทียบ Challenge 1 vs Challenge 2:

┌─────────────────┬───────────────────────┬───────────────────────┐
│ หัวข้อ          │ Grid of Secrets       │ Architect's Blueprint │
├─────────────────┼───────────────────────┼───────────────────────┤
│ Key             │ MONARCHY (ให้มา)      │ KINGDOMHAL (ต้องหา)   │
│ ความยาก        │ ⭐⭐⭐⭐               │ ⭐⭐⭐⭐              │
│ Theme           │ สายลับสงครามโลก       │ สถาปนิกยุควิคตอเรียน  │
│ Skill Focus     │ การถอดรหัส            │ การหา Key + ถอดรหัส   │
│ Answer          │ INSTRUMENTS           │ HIDDENTRUTH           │
└─────────────────┴───────────────────────┴───────────────────────┘

🎯 ทักษะที่ได้รับ:
   - Challenge 1: พื้นฐาน Playfair decryption
   - Challenge 2: Key extraction + advanced analysis
""")


def verify_solution():
    """ตรวจสอบว่า solution ถูกต้อง"""
    print("\n" + "=" * 60)
    print("Verification")
    print("=" * 60)
    
    key = "KINGDOMHAL"
    plaintext = "HIDDENTRUTH"
    
    # เข้ารหัส
    encrypted = encrypt_playfair(plaintext, key)
    print(f"📝 Original Plaintext: {plaintext}")
    print(f"🔒 Encrypted: {encrypted}")
    
    # ถอดรหัส
    decrypted = decrypt_playfair(encrypted, key)
    cleaned = decrypted.replace('X', '')
    print(f"🔓 Decrypted: {decrypted}")
    print(f"🎯 Cleaned: {cleaned}")
    
    # ตรวจสอบ
    match = cleaned == plaintext
    print(f"\n✅ Verification: {'PASS' if match else 'FAIL'}")
    
    if match:
        print(f"\n📋 Summary:")
        print(f"   Ciphertext for data.txt: {encrypted}")
        print(f"   Expected Answer: {plaintext}")
        print(f"   Flag: flag{{{plaintext.lower()}}}")


if __name__ == "__main__":
    print("🏛️ The Architect's Blueprint - Solution")
    print("=" * 60)
    
    method1_step_by_step()
    method2_script()
    method3_online()
    method4_key_discovery()
    bonus_theory()
    verify_solution()
    
    print("\n" + "=" * 60)
    print("🎉 FINAL ANSWER")
    print("=" * 60)
    print("🚩 flag{hiddentruth}")

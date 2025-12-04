"""
The Composer's Code - Solution
รหัสของนักประพันธ์เพลง - วิธีแก้

Concept: Vigenère Cipher
Key: MAMMAMIA (ชื่อเพลงดังของ ABBA - Mamma Mia!)

Multiple methods: Manual, Script, Online Tools
"""


# ==============================================================================
# วิธีที่ 1: ทำมือ (Manual Method)
# ==============================================================================
def method1_manual():
    """
    วิธีที่ 1: ทำมือโดยใช้ตาราง Vigenère
    
    ขั้นตอน:
    1. หา key จาก hint - เพลงดังของ ABBA คือ "Mamma Mia!"
    2. Key = MAMMAMIA (ตัวพิมพ์ใหญ่ ไม่มีเว้นวรรค)
    3. วนซ้ำ key ตามความยาวข้อความ
    4. ถอดรหัสทีละตัวอักษร
    
    ตัวอย่าง:
    Ciphertext: F H Q  Y U E Q C ...
    Key:        M A M  M A M I A ...
    
    F - M = T (F=5, M=12, 5-12=-7, -7+26=19, 19=T)
    H - A = H (H=7, A=0, 7-0=7, 7=H)
    Q - M = E (Q=16, M=12, 16-12=4, 4=E)
    
    ...และทำต่อไปเรื่อยๆ
    """
    print("=== Method 1: Manual with Vigenère Table ===")
    print("""
    ขั้นตอนทำมือ:
    1. หา key: เพลงดังของ ABBA → "Mamma Mia!" → MAMMAMIA
    2. Key: MAMMAMIA → วนซ้ำ: MAMMAMIAMAMMAMIAMAMMAMIA...
    3. ถอดทีละตัว:
    
    Ciphertext:  F  H  Q  Y  U  E  Q  C  ...
    Key:         M  A  M  M  A  M  I  A  ...
    Shift:       12 0  12 12 0  12 8  0  ...
    Plaintext:   T  H  E  M  U  S  I  C  ...
    
    4. อ่านข้อความที่ได้และหา flag
    """)


# ==============================================================================
# วิธีที่ 2: ใช้ Script (Python Method)
# ==============================================================================
def method2_script():
    """
    วิธีที่ 2: เขียน script ถอดรหัส Vigenère
    """
    print("=== Method 2: Python Script ===")
    
    def vigenere_decrypt(ciphertext, key):
        """ฟังก์ชันถอดรหัส Vigenère"""
        result = []
        key = key.upper()
        key_index = 0
        
        for char in ciphertext:
            if char.isalpha():
                shift = ord(key[key_index % len(key)]) - ord('A')
                if char.isupper():
                    decrypted = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                else:
                    decrypted = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
                result.append(decrypted)
                key_index += 1
            else:
                result.append(char)
        
        return ''.join(result)
    
    # Read the encrypted file
    with open('secret_melody.txt', 'r') as f:
        ciphertext = f.read().strip()
    
    key = "MAMMAMIA"
    plaintext = vigenere_decrypt(ciphertext, key)
    
    print(f"Ciphertext: {ciphertext}")
    print(f"Key: {key}")
    print(f"Plaintext: {plaintext}")
    
    # Extract flag
    import re
    flag_match = re.search(r'flag\{[^}]+\}', plaintext)
    if flag_match:
        print(f"\n🚩 FLAG FOUND: {flag_match.group()}")
    
    return plaintext


# ==============================================================================
# วิธีที่ 3: เครื่องมือออนไลน์ (Online Tools)
# ==============================================================================
def method3_online():
    """
    วิธีที่ 3: ใช้เครื่องมือออนไลน์
    """
    print("=== Method 3: Online Tools ===")
    print("""
    เครื่องมือออนไลน์ที่แนะนำ:
    
    1. CyberChef (แนะนำ!)
       URL: https://gchq.github.io/CyberChef/
       วิธีใช้:
       - ค้นหา "Vigenère Decode" ในเมนูซ้าย
       - ลากมาวางใน Recipe
       - ใส่ Key: MAMMAMIA
       - วาง ciphertext ในช่อง Input
       - ดูผลลัพธ์ในช่อง Output
    
    2. dCode.fr
       URL: https://www.dcode.fr/vigenere-cipher
       วิธีใช้:
       - วาง ciphertext
       - เลือก "Decrypt"
       - ใส่ key: MAMMAMIA
       - กด Decrypt
    
    3. Boxentriq
       URL: https://www.boxentriq.com/code-breaking/vigenere-cipher
       วิธีใช้:
       - วาง ciphertext
       - ใส่ key: MAMMAMIA
       - กด Decode
    """)


# ==============================================================================
# วิธีที่ 4: ลอง Key หลายตัว (Brute Force Song Titles)
# ==============================================================================
def method4_bruteforce_songs():
    """
    วิธีที่ 4: ลองเพลงของ ABBA หลายๆ เพลง
    """
    print("=== Method 4: Try Multiple ABBA Song Titles ===")
    
    def vigenere_decrypt(ciphertext, key):
        """ฟังก์ชันถอดรหัส Vigenère"""
        result = []
        key = key.upper()
        key_index = 0
        
        for char in ciphertext:
            if char.isalpha():
                shift = ord(key[key_index % len(key)]) - ord('A')
                if char.isupper():
                    decrypted = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                else:
                    decrypted = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
                result.append(decrypted)
                key_index += 1
            else:
                result.append(char)
        
        return ''.join(result)
    
    ciphertext = "FHQ YUEQC EPQMKE"  # Just test with first part
    
    abba_songs = [
        "DANCINGQUEEN",
        "MAMMAMIA",
        "FERNANDO",
        "WATERLOO",
        "GIMME",
        "SOSMESSAGE",
        "THANKYOUFORTHEMUSIC",
    ]
    
    print("ลองถอดรหัสด้วยชื่อเพลง ABBA หลายๆ ตัว:")
    print("-" * 50)
    
    for song in abba_songs:
        decrypted = vigenere_decrypt(ciphertext, song)
        is_valid = "MUSIC" in decrypted or "THE" in decrypted
        mark = "✅" if is_valid else "  "
        print(f"{mark} {song:25} -> {decrypted}")
    
    print("-" * 50)
    print("เพลงที่ถอดรหัสแล้วได้ข้อความที่อ่านออกคือ: MAMMAMIA ✅")


# ==============================================================================
# Bonus: ทฤษฎี Vigenère Cipher
# ==============================================================================
def bonus_theory():
    """
    Bonus: ทฤษฎีเพิ่มเติมเกี่ยวกับ Vigenère Cipher
    """
    print("=== Bonus: Musical Metaphor for Vigenère ===")
    print("""
    🎵 เปรียบเทียบกับดนตรี:
    
    ในโจทย์นี้ใช้ metaphor ดนตรีเพื่อบอกใบ้:
    
    1. "Key" ในดนตรี = คีย์เพลง (C major, G minor...)
       "Key" ใน Vigenère = คำที่ใช้เข้ารหัส
    
    2. "Transpose" ในดนตรี = เลื่อนโน้ตขึ้น/ลง
       "Shift" ใน Vigenère = เลื่อนตัวอักษรขึ้น/ลง
    
    3. "Motif ที่วนซ้ำ" ในซิมโฟนี = theme ที่กลับมาซ้ำ
       "Key ที่วนซ้ำ" ใน Vigenère = คำ key ถูกใช้ซ้ำ
    
    📊 การเปรียบเทียบ:
    
    ดนตรี:    C  D  E  F  G  A  B
    ค่า:      0  1  2  3  4  5  6
    
    ตัวอักษร: A  B  C  D  E  F  G  ...  Z
    ค่า:      0  1  2  3  4  5  6  ...  25
    
    💡 ทำไมใช้ ABBA?
    - ABBA ย่อมาจากชื่อสมาชิก: Agnetha, Björn, Benny, Anni-Frid
    - เพลง "Mamma Mia!" เป็นหนึ่งในเพลงที่โด่งดังที่สุด
    - ชื่อ "Mamma Mia" มีตัว M และ A ซ้ำกันเยอะ ทำให้น่าสนใจทางคริปโต
    """)


# ==============================================================================
# Main - Run all methods
# ==============================================================================
if __name__ == "__main__":
    print("=" * 60)
    print("THE COMPOSER'S CODE - SOLUTION")
    print("รหัสของนักประพันธ์เพลง - วิธีแก้")
    print("=" * 60)
    print()
    
    # Show theory first
    bonus_theory()
    print("\n" + "=" * 60 + "\n")
    
    # Method 1: Manual
    method1_manual()
    print("\n" + "=" * 60 + "\n")
    
    # Method 2: Script (this actually runs the decryption)
    method2_script()
    print("\n" + "=" * 60 + "\n")
    
    # Method 3: Online tools
    method3_online()
    print("\n" + "=" * 60 + "\n")
    
    # Method 4: Brute force song titles
    method4_bruteforce_songs()
    
    print("\n" + "=" * 60)
    print("🎉 Challenge Completed!")
    print("=" * 60)

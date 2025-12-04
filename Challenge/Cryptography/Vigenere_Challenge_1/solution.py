"""
The Diplomat's Secret - Solution
ความลับของทูต - วิธีแก้

Concept: Vigenère Cipher
Key: BOURBON (ราชวงศ์ที่ยิ่งใหญ่ในยุโรป - ราชวงศ์บูร์บงของฝรั่งเศส)

Multiple methods: Manual, Script, Online Tools
"""


# ==============================================================================
# วิธีที่ 1: ทำมือ (Manual Method)
# ==============================================================================
def method1_manual():
    """
    วิธีที่ 1: ทำมือโดยใช้ตาราง Vigenère
    
    ขั้นตอน:
    1. สร้างตาราง Vigenère (ตาราง 26x26)
    2. ใช้ key = BOURBON วนซ้ำตามความยาวข้อความ
    3. สำหรับแต่ละตัวอักษร:
       - แถว = ตัวอักษรใน key
       - หาตัวอักษรใน ciphertext ในแถวนั้น
       - คอลัมน์ที่พบคือ plaintext
    
    ตัวอย่าง:
    Ciphertext: U F O J U ...
    Key:        B O U R B ...
    
    U (ciphertext) + B (key backwards) = T (plaintext)
    - หาตัว U ในแถว B → อยู่คอลัมน์ T
    
    F (ciphertext) + O (key backwards) = R (plaintext)
    - หาตัว F ในแถว O → อยู่คอลัมน์ R
    
    ...และทำต่อไปเรื่อยๆ
    """
    print("=== Method 1: Manual with Vigenère Table ===")
    print("""
    ขั้นตอนทำมือ:
    1. วาดตาราง Vigenère (26x26)
    2. Key: BOURBON → วนซ้ำ: BOURBONBOURBONBOURBON...
    3. ถอดทีละตัว:
    
    Ciphertext:  U  F  O  J  U  B  B  P  B  Y  ...
    Key:         B  O  U  R  B  O  N  B  O  U  ...
    Plaintext:   T  R  U  S  T  N  O  O  N  E  ...
    
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
    with open('encrypted_letter.txt', 'r') as f:
        ciphertext = f.read().strip()
    
    key = "BOURBON"
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
       - ใส่ Key: BOURBON
       - วาง ciphertext ในช่อง Input
       - ดูผลลัพธ์ในช่อง Output
    
    2. dCode.fr
       URL: https://www.dcode.fr/vigenere-cipher
       วิธีใช้:
       - วาง ciphertext
       - เลือก "Decrypt"
       - ใส่ key: BOURBON
       - กด Decrypt
    
    3. Boxentriq
       URL: https://www.boxentriq.com/code-breaking/vigenere-cipher
       วิธีใช้:
       - วาง ciphertext
       - ใส่ key: BOURBON
       - กด Decode
    """)


# ==============================================================================
# วิธีที่ 4: Brute Force Key (ถ้าไม่รู้ key)
# ==============================================================================
def method4_bruteforce():
    """
    วิธีที่ 4: ถ้าไม่รู้ key ลองใช้ Kasiski examination หรือ Friedman test
    """
    print("=== Method 4: Finding the Key (if unknown) ===")
    print("""
    ถ้าไม่รู้ key สามารถใช้เทคนิคเหล่านี้:
    
    1. Kasiski Examination:
       - หาตัวอักษรที่ซ้ำกันในข้อความ
       - หาระยะห่างระหว่างการซ้ำ
       - หา GCD ของระยะห่าง → ได้ความยาว key
    
    2. Index of Coincidence:
       - วิเคราะห์ความถี่ตัวอักษร
       - ค่า IoC จะช่วยบอกความยาว key
    
    3. Frequency Analysis:
       - หลังจากรู้ความยาว key
       - วิเคราะห์ความถี่แยกแต่ละตำแหน่ง
       - ตัวที่พบบ่อยสุดน่าจะเป็น E
    
    เครื่องมือที่ช่วย:
    - dCode.fr มี "Automatic Decryption" ที่ลองหา key ให้
    - CrypTool มีฟีเจอร์วิเคราะห์ Vigenère
    """)


# ==============================================================================
# Bonus: ทฤษฎี Vigenère Cipher
# ==============================================================================
def bonus_theory():
    """
    Bonus: ทฤษฎีเพิ่มเติมเกี่ยวกับ Vigenère Cipher
    """
    print("=== Bonus: Vigenère Cipher Theory ===")
    print("""
    📚 ประวัติ:
    - คิดค้นโดย Blaise de Vigenère ชาวฝรั่งเศส ในปี 1586
    - เคยถูกเรียกว่า "le chiffre indéchiffrable" (รหัสที่ถอดไม่ได้)
    - ถูกถอดได้ครั้งแรกโดย Charles Babbage ในศตวรรษที่ 19
    
    🔐 หลักการ:
    - เป็น polyalphabetic substitution cipher
    - ใช้ key เพื่อกำหนดการเลื่อนแต่ละตัวอักษร
    - ต่างจาก Caesar ที่เลื่อนทุกตัวเท่ากัน
    
    📐 สูตร:
    - Encryption: Ci = (Pi + Ki) mod 26
    - Decryption: Pi = (Ci - Ki) mod 26
    โดย:
    - Ci = ตัวอักษร ciphertext ตำแหน่ง i
    - Pi = ตัวอักษร plaintext ตำแหน่ง i  
    - Ki = ตัวอักษร key ตำแหน่ง i (วนซ้ำ)
    
    ⚠️ จุดอ่อน:
    - key ที่สั้นทำให้ถูก crack ง่าย
    - Kasiski examination สามารถหาความยาว key
    - Frequency analysis ยังใช้ได้หลังจากรู้ความยาว key
    """)


# ==============================================================================
# Main - Run all methods
# ==============================================================================
if __name__ == "__main__":
    print("=" * 60)
    print("THE DIPLOMAT'S SECRET - SOLUTION")
    print("ความลับของทูต - วิธีแก้")
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
    
    # Method 4: Brute force
    method4_bruteforce()
    
    print("\n" + "=" * 60)
    print("🎉 Challenge Completed!")
    print("=" * 60)

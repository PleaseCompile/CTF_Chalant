"""
XOR Known Plaintext Attack - Solution
======================================
Challenge: SECURECOMM v2.1 Encrypted Message
Concept: Known Plaintext Attack on XOR cipher

Multiple methods:
1. Manual calculation (step by step)
2. Python script (automated)
3. Online tools (CyberChef, etc.)
"""

# ===== DATA =====
ciphertext_hex = "000000071711100a0e1f7f22616b722e03061c08791301191a0b3f1f161369232f33222f2b2a310d2c270c23363c3828160b07"
known_plaintext = "SECURECOMM:v2.1|FROM:"


# ===== QUICK SOLUTION (โค้ดสั้นๆ) =====
def quick_find_key():
    """โค้ดสั้นๆ หา key (3 บรรทัด)"""
    c = bytes.fromhex(ciphertext_hex)
    key = bytes(ord(known_plaintext[i]) ^ c[i] for i in range(len(known_plaintext)))
    print(f"Key: {key}")  # b'SECRETSECRETSECRETSEC' -> "SECRET"


# One-liner หา key:
# print(bytes(ord("SECURECOMM:v2.1|FROM:"[i]) ^ bytes.fromhex("000000071711100a0e1f7f22616b722e03061c08791301191a0b3f1f161369232f33222f2b2a310d2c270c23363c3828160b07")[i] for i in range(21)))


def method1_manual():
    """
    วิธีที่ 1: ทำมือ (Manual Calculation)
    =====================================
    
    หลักการ XOR:
    - Plaintext ⊕ Key = Ciphertext
    - Plaintext ⊕ Ciphertext = Key
    
    ขั้นตอน:
    1. แปลง ciphertext จาก hex เป็น bytes
    2. XOR แต่ละ byte ของ known_plaintext กับ ciphertext
    3. ผลลัพธ์คือ key bytes
    """
    print("=" * 50)
    print("Method 1: Manual Calculation")
    print("=" * 50)
    
    # Step 1: Convert hex to bytes
    ciphertext = bytes.fromhex(ciphertext_hex)
    print(f"Ciphertext (first 21 bytes): {ciphertext[:21].hex()}")
    print(f"Known plaintext: '{known_plaintext}'")
    print()
    
    # Step 2: XOR to find key
    print("XOR calculation (first 21 bytes):")
    key_bytes = []
    for i in range(len(known_plaintext)):
        p = ord(known_plaintext[i])
        c = ciphertext[i]
        k = p ^ c
        key_bytes.append(k)
        print(f"  '{known_plaintext[i]}' ({p:3d}) XOR 0x{c:02x} ({c:3d}) = {chr(k) if 32 <= k < 127 else '?'} ({k:3d})")
    
    key = bytes(key_bytes)
    print(f"\nExtracted key: {key}")
    print(f"Key pattern detected: SECRET (repeating)")
    
    return key


def method2_script():
    """
    วิธีที่ 2: Python Script (Automated)
    =====================================
    
    ใช้ script เพื่อ:
    1. หา key จาก known plaintext
    2. ถอดรหัสข้อความทั้งหมด
    """
    print("=" * 50)
    print("Method 2: Automated Python Script")
    print("=" * 50)
    
    ciphertext = bytes.fromhex(ciphertext_hex)
    
    # Extract key from known plaintext
    key_bytes = []
    for i in range(len(known_plaintext)):
        key_bytes.append(ord(known_plaintext[i]) ^ ciphertext[i])
    
    extracted_key = bytes(key_bytes)
    print(f"Extracted key: {extracted_key}")
    
    # Detect repeating pattern
    key_string = extracted_key.decode('utf-8')
    for key_len in range(1, len(key_string) // 2 + 1):
        pattern = key_string[:key_len]
        if key_string == (pattern * (len(key_string) // key_len + 1))[:len(key_string)]:
            print(f"Detected repeating key: '{pattern}'")
            break
    
    # Decrypt full message using detected key
    key = "SECRET"  # Detected pattern
    decrypted = ""
    for i in range(len(ciphertext)):
        decrypted += chr(ciphertext[i] ^ ord(key[i % len(key)]))
    
    print(f"\nDecrypted message: {decrypted}")
    
    # Extract flag
    import re
    flag_match = re.search(r'flag\{[^}]+\}', decrypted)
    if flag_match:
        print(f"\n🚩 FLAG FOUND: {flag_match.group()}")
    
    return decrypted


def method3_online():
    """
    วิธีที่ 3: Online Tools
    =======================
    
    เครื่องมือออนไลน์ที่ใช้ได้:
    1. CyberChef (https://gchq.github.io/CyberChef/)
    2. dCode (https://www.dcode.fr/xor-cipher)
    3. Boxentriq (https://www.boxentriq.com/code-breaking/xor-encryption)
    """
    print("=" * 50)
    print("Method 3: Online Tools")
    print("=" * 50)
    
    print("""
    🔧 CyberChef Recipe:
    =====================
    1. ไปที่: https://gchq.github.io/CyberChef/
    2. ลาก "From Hex" ไปใน Recipe
    3. ลาก "XOR" ไปใน Recipe
    4. ใส่ Key: SECRET (หรือ SECRETSECRETSECRET...)
    5. วาง ciphertext ใน Input
    6. ดู Output
    
    Recipe URL:
    https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')XOR(%7B'option':'UTF8','string':'SECRET'%7D,'Standard',false)
    
    🔧 dCode:
    ==========
    1. ไปที่: https://www.dcode.fr/xor-cipher
    2. เลือก "Knowing the Key"
    3. ใส่ key: SECRET
    4. ใส่ ciphertext (hex)
    5. กด DECRYPT
    
    🔧 Manual with Known Plaintext:
    ================================
    1. ใช้ known plaintext attack tool
    2. ใส่ known plaintext: SECURECOMM:v2.1|FROM:
    3. ใส่ ciphertext (hex)
    4. Tool จะหา key ให้
    """)


def bonus_theory():
    """
    Bonus: ทฤษฎี XOR และ Known Plaintext Attack
    =============================================
    """
    print("=" * 50)
    print("Bonus: XOR Theory & Known Plaintext Attack")
    print("=" * 50)
    
    print("""
    📚 XOR Properties:
    ==================
    1. A ⊕ 0 = A           (Identity)
    2. A ⊕ A = 0           (Self-inverse)
    3. A ⊕ B = B ⊕ A       (Commutative)
    4. (A ⊕ B) ⊕ C = A ⊕ (B ⊕ C)  (Associative)
    
    📚 Why Known Plaintext Attack Works:
    =====================================
    Encryption:  P ⊕ K = C
    Attack:      P ⊕ C = P ⊕ (P ⊕ K) = (P ⊕ P) ⊕ K = 0 ⊕ K = K
    
    เมื่อเรารู้ Plaintext (P) และ Ciphertext (C)
    เราสามารถหา Key (K) ได้โดยการ XOR!
    
    📚 Repeating Key XOR Vulnerability:
    ====================================
    - ถ้า key สั้นกว่า message, key จะถูกใช้ซ้ำ
    - pattern ของ key จะถูกเปิดเผย
    - สามารถถอดรหัสข้อความที่ยาวกว่า key ได้
    
    📚 Real-world Example:
    ======================
    - WEP (Wireless) ใช้ XOR และถูก crack ด้วยวิธีนี้
    - One-Time Pad ใช้ XOR แต่ปลอดภัยเพราะ key ยาวเท่า message
    """)


def verify_solution():
    """
    Verify the solution is correct
    """
    print("=" * 50)
    print("Solution Verification")
    print("=" * 50)
    
    key = "SECRET"
    ciphertext = bytes.fromhex(ciphertext_hex)
    
    # Decrypt
    decrypted = ""
    for i in range(len(ciphertext)):
        decrypted += chr(ciphertext[i] ^ ord(key[i % len(key)]))
    
    expected = "SECURECOMM:v2.1|FROM:ADMIN|MSG:flag{xor_is_fun}|END"
    
    print(f"Decrypted: {decrypted}")
    print(f"Expected:  {expected}")
    print(f"Match: {decrypted == expected}")
    print(f"\n🚩 FLAG: flag{{xor_is_fun}}")
    
    return decrypted == expected


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print(" XOR Known Plaintext Attack - Solution")
    print("=" * 60 + "\n")
    
    print("=" * 50)
    print("🚀 Quick Solution (โค้ดสั้นๆ)")
    print("=" * 50)
    quick_find_key()
    print("\n")
    
    method1_manual()
    print("\n")
    
    method2_script()
    print("\n")
    
    method3_online()
    print("\n")
    
    bonus_theory()
    print("\n")
    
    verify_solution()

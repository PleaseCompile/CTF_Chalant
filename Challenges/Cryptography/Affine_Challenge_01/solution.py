"""
สูตรลับแห่งปิทาโกรัส (The Secret Formula) - Solution
==============================================

Challenge: Affine Cipher CTF
Concept: การเข้ารหัส Affine (ax + b mod 26)

Multiple methods: Manual, Script, Online Tools
"""

import hashlib

# ===== ข้อมูลโจทย์ =====
CIPHERTEXT = "ZRCHLIMWUIVSWCVZQIZRUCSPCZ"
A = 5  # ค่าคงที่การคูณ
B = 8  # ค่าคงที่การบวก
M = 26  # จำนวนตัวอักษรในตารางแอลฟาเบต


def method1_manual():
    """
    วิธีที่ 1: ทำมือ (Manual Calculation)
    =====================================
    
    การถอดรหัส Affine:
    - สูตรเข้ารหัส: E(x) = (ax + b) mod m
    - สูตรถอดรหัส: D(y) = a^(-1) * (y - b) mod m
    
    ขั้นตอน:
    1. หา modular multiplicative inverse ของ a
    2. ใช้สูตรถอดรหัส
    
    สำหรับ a=5:
    - ต้องหา a^(-1) ที่ทำให้ (5 * a^(-1)) mod 26 = 1
    - 5 * 21 = 105 = 4*26 + 1 = 1 (mod 26)
    - ดังนั้น a^(-1) = 21
    """
    print("=" * 50)
    print("วิธีที่ 1: ทำมือ (Manual)")
    print("=" * 50)
    
    # หา modular inverse ของ a
    a_inv = None
    for i in range(1, M):
        if (A * i) % M == 1:
            a_inv = i
            break
    
    print(f"a = {A}")
    print(f"b = {B}")
    print(f"a^(-1) mod 26 = {a_inv}")
    print(f"\nสูตรถอดรหัส: D(y) = {a_inv} * (y - {B}) mod 26")
    
    # ถอดรหัสทีละตัวอักษร
    print("\nการถอดรหัสทีละตัว:")
    plaintext = ""
    for i, char in enumerate(CIPHERTEXT[:5]):  # แสดง 5 ตัวแรก
        y = ord(char) - ord('A')
        x = (a_inv * (y - B)) % M
        decrypted = chr(x + ord('A'))
        print(f"  {char} (y={y:2d}) → x = {a_inv}*({y}-{B}) mod 26 = {x:2d} → {decrypted}")
        plaintext += decrypted
    
    print(f"  ... (ต่อไปเรื่อยๆ)")
    return a_inv


def method2_script():
    """
    วิธีที่ 2: ใช้ Script Python
    ============================
    """
    print("\n" + "=" * 50)
    print("วิธีที่ 2: ใช้ Script Python")
    print("=" * 50)
    
    def mod_inverse(a, m):
        """หา modular multiplicative inverse"""
        for i in range(1, m):
            if (a * i) % m == 1:
                return i
        return None
    
    def affine_decrypt(ciphertext, a, b):
        """ถอดรหัส Affine cipher"""
        a_inv = mod_inverse(a, M)
        if a_inv is None:
            return None
        
        plaintext = ""
        for char in ciphertext:
            if char.isalpha():
                y = ord(char.upper()) - ord('A')
                x = (a_inv * (y - b)) % M
                plaintext += chr(x + ord('A'))
            else:
                plaintext += char
        return plaintext
    
    plaintext = affine_decrypt(CIPHERTEXT, A, B)
    print(f"Ciphertext: {CIPHERTEXT}")
    print(f"Key: a={A}, b={B}")
    print(f"Plaintext: {plaintext}")
    
    # แยก flag
    if "THEFLAGIS" in plaintext:
        flag_content = plaintext.split("THEFLAGIS")[1]
        # แปลงเป็นรูปแบบที่มี underscore
        flag_content_formatted = "ANCIENT_MATH_SECRET"
        flag_hash = hashlib.md5(flag_content_formatted.encode()).hexdigest()
        print(f"\n🚩 Flag content: {flag_content}")
        print(f"🚩 Formatted: {flag_content_formatted}")
        print(f"🚩 FLAG: flag{{{flag_hash}}}")
    
    return plaintext


def method3_online():
    """
    วิธีที่ 3: ใช้เครื่องมือออนไลน์
    ================================
    """
    print("\n" + "=" * 50)
    print("วิธีที่ 3: ใช้เครื่องมือออนไลน์")
    print("=" * 50)
    
    print("""
    เครื่องมือออนไลน์ที่แนะนำ:
    
    1. CyberChef (https://gchq.github.io/CyberChef/)
       - ค้นหา "Affine Cipher Decode"
       - ใส่ a=5, b=8
       - วาง ciphertext
    
    2. dCode (https://www.dcode.fr/affine-cipher)
       - เลือก "Decrypt"
       - ใส่ค่า A=5, B=8
       - หรือใช้ "Automatic" ให้มัน bruteforce
    
    3. Rumkin.com (http://rumkin.com/tools/cipher/affine.php)
       - ใส่ ciphertext
       - ตั้ง a=5, b=8
       - กด Decode
    
    4. Cryptii (https://cryptii.com/pipes/affine-cipher)
       - เลือก Affine cipher
       - ตั้งค่า slope=5, intercept=8
       - วาง ciphertext
    """)


def method4_bruteforce():
    """
    วิธีที่ 4: Bruteforce ทุกค่า a, b ที่เป็นไปได้
    =============================================
    
    ใช้เมื่อไม่ทราบค่า a และ b
    """
    print("\n" + "=" * 50)
    print("วิธีที่ 4: Bruteforce")
    print("=" * 50)
    
    from math import gcd
    
    def mod_inverse(a, m):
        for i in range(1, m):
            if (a * i) % m == 1:
                return i
        return None
    
    def affine_decrypt(ciphertext, a, b):
        a_inv = mod_inverse(a, M)
        if a_inv is None:
            return None
        plaintext = ""
        for char in ciphertext:
            if char.isalpha():
                y = ord(char.upper()) - ord('A')
                x = (a_inv * (y - b)) % M
                plaintext += chr(x + ord('A'))
            else:
                plaintext += char
        return plaintext
    
    print("ค่า a ที่เป็นไปได้ (coprime กับ 26):", end=" ")
    valid_a = [a for a in range(1, 26) if gcd(a, 26) == 1]
    print(valid_a)
    
    print("\nค้นหาผลลัพธ์ที่อ่านได้...")
    for a in valid_a:
        for b in range(26):
            result = affine_decrypt(CIPHERTEXT, a, b)
            # ตรวจสอบว่ามีคำที่อ่านได้หรือไม่
            if result and ("FLAG" in result or "THE" in result):
                print(f"  Found! a={a}, b={b}: {result}")


def bonus_theory():
    """
    Bonus: ทฤษฎี Affine Cipher
    ==========================
    """
    print("\n" + "=" * 50)
    print("📚 Bonus: ทฤษฎี Affine Cipher")
    print("=" * 50)
    
    print("""
    Affine Cipher คืออะไร?
    ----------------------
    - เป็น monoalphabetic substitution cipher
    - ใช้สูตรเชิงเส้น: E(x) = (ax + b) mod m
    - เป็นการรวม Caesar cipher (เลื่อน b ตำแหน่ง) 
      กับ multiplicative cipher (คูณด้วย a)
    
    เงื่อนไขสำคัญ:
    -------------
    - gcd(a, m) = 1 (a ต้อง coprime กับ m)
    - ถ้า m = 26 → a ∈ {1,3,5,7,9,11,15,17,19,21,23,25}
    - มีทั้งหมด 12 × 26 = 312 keys
    
    การถอดรหัส:
    ----------
    - D(y) = a^(-1) * (y - b) mod m
    - a^(-1) คือ modular multiplicative inverse ของ a
    
    ตัวอย่าง a=5:
    - 5 × 21 ≡ 1 (mod 26)
    - ดังนั้น 5^(-1) = 21
    
    จุดอ่อน:
    -------
    - มี keyspace เล็ก (312 keys) → bruteforce ได้ง่าย
    - ยังคงอ่อนต่อ frequency analysis
    """)


if __name__ == "__main__":
    print("🔐 สูตรลับแห่งปิทาโกรัส - Solution")
    print("=" * 50)
    
    method1_manual()
    plaintext = method2_script()
    method3_online()
    method4_bruteforce()
    bonus_theory()
    
    print("\n" + "=" * 50)
    print("✅ สรุปคำตอบ")
    print("=" * 50)
    print(f"Plaintext: {plaintext}")
    print(f"Flag: flag{{9d37a9d51f3eccaf63c460cf6bb94648}}")

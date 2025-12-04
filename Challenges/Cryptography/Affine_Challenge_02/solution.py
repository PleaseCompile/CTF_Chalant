"""
รหัสแห่งสมาคมลับ (The Shadow Society's Code) - Solution
=======================================================

Challenge: Affine Cipher CTF
Concept: การเข้ารหัส Affine (ax + b mod 26)

Multiple methods: Manual, Script, Online Tools
"""

import hashlib

# ===== ข้อมูลโจทย์ =====
CIPHERTEXT = "GAFMCDTHZCHQFDSRHEAFSJDZGFS"
A = 7   # ค่าคงที่การคูณ
B = 3   # ค่าคงที่การบวก
M = 26  # จำนวนตัวอักษรในตารางแอลฟาเบต


def method1_manual():
    """
    วิธีที่ 1: ทำมือ (Manual Calculation)
    =====================================
    
    การถอดรหัส Affine:
    - สูตรเข้ารหัส: E(x) = (ax + b) mod m
    - สูตรถอดรหัส: D(y) = a^(-1) * (y - b) mod m
    
    สำหรับ a=7:
    - ต้องหา a^(-1) ที่ทำให้ (7 * a^(-1)) mod 26 = 1
    - 7 * 15 = 105 = 4*26 + 1 = 1 (mod 26)
    - ดังนั้น a^(-1) = 15
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
    print(f"\nการหา a^(-1):")
    print(f"  7 × 1 = 7 mod 26 = 7 ❌")
    print(f"  7 × 2 = 14 mod 26 = 14 ❌")
    print(f"  ...")
    print(f"  7 × 15 = 105 mod 26 = 1 ✅")
    print(f"\na^(-1) mod 26 = {a_inv}")
    print(f"\nสูตรถอดรหัส: D(y) = {a_inv} × (y - {B}) mod 26")
    
    # ถอดรหัสทีละตัวอักษร
    print("\nการถอดรหัสตัวอย่าง (5 ตัวแรก):")
    plaintext = ""
    for i, char in enumerate(CIPHERTEXT[:5]):
        y = ord(char) - ord('A')
        x = (a_inv * (y - B)) % M
        decrypted = chr(x + ord('A'))
        print(f"  {char} (y={y:2d}) → x = {a_inv}×({y}-{B}) mod 26 = {x:2d} → {decrypted}")
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
        flag_content_formatted = "LINEAR_CIPHER_MASTER"
        flag_hash = hashlib.md5(flag_content_formatted.encode()).hexdigest()
        print(f"\n🚩 Flag content: {flag_content}")
        print(f"🚩 Formatted: {flag_content_formatted}")
        print(f"🚩 FLAG: flag{{{flag_hash}}}")
    
    return plaintext


def method3_extended_euclidean():
    """
    วิธีที่ 3: ใช้ Extended Euclidean Algorithm
    ==========================================
    
    วิธีที่เป็นทางการในการหา modular inverse
    """
    print("\n" + "=" * 50)
    print("วิธีที่ 3: Extended Euclidean Algorithm")
    print("=" * 50)
    
    def extended_gcd(a, b):
        """คำนวณ GCD และ Bézout coefficients"""
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y
    
    def mod_inverse_egcd(a, m):
        """หา modular inverse ด้วย Extended Euclidean Algorithm"""
        gcd, x, _ = extended_gcd(a % m, m)
        if gcd != 1:
            return None  # inverse ไม่มีอยู่
        return (x % m + m) % m
    
    a_inv = mod_inverse_egcd(A, M)
    print(f"Extended GCD method:")
    print(f"  หา x ที่ {A}x ≡ 1 (mod {M})")
    print(f"  ผลลัพธ์: x = {a_inv}")
    print(f"  ตรวจสอบ: {A} × {a_inv} = {A * a_inv} ≡ {(A * a_inv) % M} (mod 26)")


def method4_online():
    """
    วิธีที่ 4: ใช้เครื่องมือออนไลน์
    ================================
    """
    print("\n" + "=" * 50)
    print("วิธีที่ 4: ใช้เครื่องมือออนไลน์")
    print("=" * 50)
    
    print("""
    เครื่องมือออนไลน์ที่แนะนำ:
    
    1. CyberChef (https://gchq.github.io/CyberChef/)
       - ค้นหา "Affine Cipher Decode"
       - ใส่ a=7, b=3
       - วาง ciphertext
    
    2. dCode (https://www.dcode.fr/affine-cipher)
       - เลือก "Decrypt"
       - ใส่ค่า A=7, B=3
       - หรือใช้ "Brute Force Attack" ให้มัน bruteforce
    
    3. Cryptii (https://cryptii.com/pipes/affine-cipher)
       - เลือก Affine cipher
       - ตั้งค่า slope=7, intercept=3
       - วาง ciphertext
    
    4. Rumkin.com (http://rumkin.com/tools/cipher/affine.php)
       - ใส่ ciphertext
       - ตั้ง a=7, b=3
       - กด Decode
    """)


def method5_known_plaintext():
    """
    วิธีที่ 5: Known Plaintext Attack
    =================================
    
    ถ้าเรารู้ว่าข้อความเริ่มต้นด้วย "THEFLAG"
    """
    print("\n" + "=" * 50)
    print("วิธีที่ 5: Known Plaintext Attack")
    print("=" * 50)
    
    print("""
    สมมติเรารู้ว่าข้อความเริ่มต้นด้วย "THE"
    
    Ciphertext: G A F ...
    Plaintext:  T H E ...
    
    จากสูตร: y = ax + b (mod 26)
    
    สมการที่ 1: T(19) → G(6):  6 = 19a + b (mod 26)
    สมการที่ 2: H(7) → A(0):   0 = 7a + b (mod 26)
    
    ลบกัน: 6 = 12a (mod 26)
    
    หา a: 12a ≡ 6 (mod 26)
           2a ≡ 1 (mod 26)... ไม่ได้ผล (GCD(2,26)≠1)
    
    ลองวิธีอื่น:
    จาก 0 = 7a + b → b = -7a (mod 26)
    แทนใน 6 = 19a + b:
    6 = 19a - 7a = 12a (mod 26)
    
    ลอง a=7: 12×7 = 84 = 3×26 + 6 ≡ 6 ✓
    ดังนั้น a=7, b = -7×7 = -49 ≡ 3 (mod 26)
    """)


def bonus_theory():
    """
    Bonus: ทฤษฎี Affine Cipher แบบลึกซึ้ง
    =====================================
    """
    print("\n" + "=" * 50)
    print("📚 Bonus: ทฤษฎี Affine Cipher แบบลึกซึ้ง")
    print("=" * 50)
    
    print("""
    ทำไม GCD(a, 26) ต้องเท่ากับ 1?
    ------------------------------
    
    ถ้า GCD(a, m) ≠ 1 จะเกิด collision!
    
    ตัวอย่าง a=2, b=0, m=26:
    E(0) = 2×0 = 0  → A
    E(13) = 2×13 = 26 ≡ 0 → A  (collision!)
    
    ทั้ง A และ N จะถูกเข้ารหัสเป็น A เหมือนกัน
    → ไม่สามารถถอดรหัสได้!
    
    
    Affine vs Caesar vs ROT13:
    --------------------------
    - Caesar: E(x) = x + b (mod 26)     → a=1
    - ROT13:  E(x) = x + 13 (mod 26)    → a=1, b=13
    - Affine: E(x) = ax + b (mod 26)    → General form
    
    Caesar เป็น special case ของ Affine ที่ a=1!
    
    
    Affine Cipher Group Theory:
    ---------------------------
    - Affine transformations form a group under composition
    - E₁(E₂(x)) = a₁(a₂x + b₂) + b₁ = a₁a₂x + (a₁b₂ + b₁)
    - ก็ยังเป็น Affine transformation!
    """)


if __name__ == "__main__":
    print("🕵️ รหัสแห่งสมาคมลับ - Solution")
    print("=" * 50)
    
    method1_manual()
    plaintext = method2_script()
    method3_extended_euclidean()
    method4_online()
    method5_known_plaintext()
    bonus_theory()
    
    print("\n" + "=" * 50)
    print("✅ สรุปคำตอบ")
    print("=" * 50)
    print(f"Plaintext: {plaintext}")
    print(f"Flag: flag{{7e64559b22e8adb427347f2f429ff277}}")

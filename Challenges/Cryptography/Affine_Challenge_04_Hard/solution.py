"""
ประตูสองชั้นแห่งเงามืด (The Double-Locked Gate) - Solution
=========================================================

Challenge: Hard Double Affine Cipher CTF
Concept: Double encryption with Affine cipher

Difficulty: ⭐⭐⭐⭐⭐

Multiple methods: Step-by-step, Combined key, Verification
"""

import hashlib
from math import gcd

# ===== ข้อมูลโจทย์ =====
CIPHERTEXT = "WSRACHJBNIDFQCRCHPRERGMREW"
M = 26

# Keys
A1, B1 = 5, 8   # First encryption
A2, B2 = 7, 3   # Second encryption


def mod_inverse(a, m):
    """หา modular multiplicative inverse"""
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None


def affine_encrypt(plaintext, a, b):
    """เข้ารหัส Affine cipher"""
    result = ""
    for char in plaintext:
        if char.isalpha():
            x = ord(char.upper()) - ord('A')
            y = (a * x + b) % M
            result += chr(y + ord('A'))
        else:
            result += char
    return result


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


def method1_step_by_step():
    """
    วิธีที่ 1: ถอดรหัสทีละชั้น (Step-by-Step)
    ==========================================
    
    การเข้ารหัส: Plaintext → [E1] → Intermediate → [E2] → Ciphertext
    การถอดรหัส: Ciphertext → [D2] → Intermediate → [D1] → Plaintext
    
    ต้องถอดย้อนกลับ! Gate 2 ก่อน, แล้ว Gate 1
    """
    print("=" * 60)
    print("วิธีที่ 1: ถอดรหัสทีละชั้น (Step-by-Step)")
    print("=" * 60)
    
    print(f"\nOriginal ciphertext: {CIPHERTEXT}")
    print(f"\nKeys:")
    print(f"  Gate 1: a₁={A1}, b₁={B1}")
    print(f"  Gate 2: a₂={A2}, b₂={B2}")
    
    # Step 1: ถอดรหัส Gate 2 (ชั้นนอก)
    print(f"\n📌 Step 1: Decrypt Gate 2 (outer layer)")
    print(f"   Formula: D₂(y) = {mod_inverse(A2, M)} × (y - {B2}) mod 26")
    
    intermediate = affine_decrypt(CIPHERTEXT, A2, B2)
    print(f"   Ciphertext: {CIPHERTEXT}")
    print(f"   After D₂:   {intermediate}")
    
    # Step 2: ถอดรหัส Gate 1 (ชั้นใน)
    print(f"\n📌 Step 2: Decrypt Gate 1 (inner layer)")
    print(f"   Formula: D₁(y) = {mod_inverse(A1, M)} × (y - {B1}) mod 26")
    
    plaintext = affine_decrypt(intermediate, A1, B1)
    print(f"   Intermediate: {intermediate}")
    print(f"   After D₁:     {plaintext}")
    
    return plaintext


def method2_combined_key():
    """
    วิธีที่ 2: หา Combined Key
    ==========================
    
    Double Affine สามารถลดรูปเป็น Single Affine ได้!
    
    E₂(E₁(x)) = a₂(a₁x + b₁) + b₂
              = (a₂·a₁)x + (a₂·b₁ + b₂)
    
    Combined key:
    - a_combined = (a₂ × a₁) mod 26
    - b_combined = (a₂ × b₁ + b₂) mod 26
    """
    print("\n" + "=" * 60)
    print("วิธีที่ 2: หา Combined Key")
    print("=" * 60)
    
    print(f"\n🔢 Mathematical derivation:")
    print(f"   E₂(E₁(x)) = a₂(a₁x + b₁) + b₂")
    print(f"             = (a₂·a₁)x + (a₂·b₁ + b₂)")
    
    # คำนวณ combined key
    a_combined = (A2 * A1) % M
    b_combined = (A2 * B1 + B2) % M
    
    print(f"\n📊 Calculation:")
    print(f"   a_combined = ({A2} × {A1}) mod 26 = {A2 * A1} mod 26 = {a_combined}")
    print(f"   b_combined = ({A2} × {B1} + {B2}) mod 26 = {A2 * B1 + B2} mod 26 = {b_combined}")
    
    print(f"\n✅ Combined key: a={a_combined}, b={b_combined}")
    
    # ตรวจสอบว่า a_combined coprime กับ 26
    if gcd(a_combined, M) == 1:
        print(f"   GCD({a_combined}, 26) = 1 ✓ (valid key)")
    else:
        print(f"   GCD({a_combined}, 26) ≠ 1 ✗ (invalid key!)")
    
    # ถอดรหัสด้วย combined key
    plaintext = affine_decrypt(CIPHERTEXT, a_combined, b_combined)
    
    print(f"\n📌 Decrypt with combined key:")
    print(f"   D(y) = {mod_inverse(a_combined, M)} × (y - {b_combined}) mod 26")
    print(f"   Ciphertext: {CIPHERTEXT}")
    print(f"   Plaintext:  {plaintext}")
    
    return a_combined, b_combined, plaintext


def method3_verify():
    """
    วิธีที่ 3: ตรวจสอบความถูกต้อง
    =============================
    
    ทดสอบว่าการเข้ารหัส 2 ครั้ง = การเข้ารหัสครั้งเดียวด้วย combined key
    """
    print("\n" + "=" * 60)
    print("วิธีที่ 3: ตรวจสอบความถูกต้อง")
    print("=" * 60)
    
    # ถอดรหัสทีละชั้น
    plaintext_step = affine_decrypt(affine_decrypt(CIPHERTEXT, A2, B2), A1, B1)
    
    # ถอดรหัสด้วย combined key
    a_combined = (A2 * A1) % M
    b_combined = (A2 * B1 + B2) % M
    plaintext_combined = affine_decrypt(CIPHERTEXT, a_combined, b_combined)
    
    print(f"\n🔍 Verification:")
    print(f"   Step-by-step result:  {plaintext_step}")
    print(f"   Combined key result:  {plaintext_combined}")
    print(f"   Match: {plaintext_step == plaintext_combined} ✓")
    
    # ทดสอบการเข้ารหัสกลับ
    print(f"\n🔄 Reverse verification (encrypt plaintext):")
    
    # เข้ารหัสทีละชั้น
    intermediate = affine_encrypt(plaintext_step, A1, B1)
    ciphertext_step = affine_encrypt(intermediate, A2, B2)
    
    # เข้ารหัสด้วย combined key
    ciphertext_combined = affine_encrypt(plaintext_step, a_combined, b_combined)
    
    print(f"   Original ciphertext:  {CIPHERTEXT}")
    print(f"   Re-encrypted (step):  {ciphertext_step}")
    print(f"   Re-encrypted (comb):  {ciphertext_combined}")
    print(f"   All match: {CIPHERTEXT == ciphertext_step == ciphertext_combined} ✓")


def method4_online_tools():
    """
    วิธีที่ 4: ใช้เครื่องมือออนไลน์
    ================================
    """
    print("\n" + "=" * 60)
    print("วิธีที่ 4: ใช้เครื่องมือออนไลน์")
    print("=" * 60)
    
    print("""
    วิธีใช้เครื่องมือออนไลน์:
    
    Option A: ถอดทีละชั้น
    ---------------------
    1. ไปที่ dCode หรือ CyberChef
    2. ถอด Gate 2 ก่อน: a=7, b=3
    3. นำผลลัพธ์ไปถอด Gate 1: a=5, b=8
    
    Option B: ใช้ Combined Key
    --------------------------
    1. คำนวณ: a = (7×5) mod 26 = 9
    2. คำนวณ: b = (7×8+3) mod 26 = 7
    3. ถอดครั้งเดียว: a=9, b=7
    
    เครื่องมือที่แนะนำ:
    - CyberChef: https://gchq.github.io/CyberChef/
    - dCode: https://www.dcode.fr/affine-cipher
    """)


def bonus_math_theory():
    """
    Bonus: ทฤษฎีทางคณิตศาสตร์
    =========================
    """
    print("\n" + "=" * 60)
    print("📚 Bonus: ทฤษฎีทางคณิตศาสตร์")
    print("=" * 60)
    
    print("""
    ทำไม Double Affine = Single Affine?
    ===================================
    
    Affine transformations เป็น GROUP ภายใต้การ composition!
    
    Properties:
    -----------
    1. Closure: E₂ ∘ E₁ ยังคงเป็น Affine transformation
       E₂(E₁(x)) = (a₂·a₁)x + (a₂·b₁ + b₂)
    
    2. Identity: E(x) = 1·x + 0 (a=1, b=0)
    
    3. Inverse: ทุก Affine transformation มี inverse
       D(y) = a⁻¹(y - b)
    
    4. Associativity: (E₃ ∘ E₂) ∘ E₁ = E₃ ∘ (E₂ ∘ E₁)
    
    
    Affine Group Structure:
    -----------------------
    - Affine transformations mod m form the "Affine Group"
    - เรียกว่า Aff(Z/mZ) หรือ GA(1, Z/mZ)
    - ขนาด: φ(m) × m (สำหรับ m=26: 12 × 26 = 312)
    
    
    Security Implication:
    ---------------------
    การเข้ารหัสซ้อนหลายครั้งด้วย Affine cipher
    ไม่ได้เพิ่มความปลอดภัย!
    
    เพราะ:
    - n ครั้งของ Affine = 1 ครั้งของ Affine
    - Key space ยังคงเป็น 312
    - Brute force ยังคงทำได้ง่าย
    
    
    This is NOT True for All Ciphers!
    ---------------------------------
    - DES: 2DES ≠ DES (แต่ก็ไม่ปลอดภัย)
    - AES: การใช้ AES หลายครั้งเพิ่มความปลอดภัย
    - RSA: ไม่เป็น group ภายใต้ composition
    """)


if __name__ == "__main__":
    print("🎭 ประตูสองชั้นแห่งเงามืด - Solution")
    print("=" * 60)
    print("Difficulty: ⭐⭐⭐⭐⭐ (Very Hard)")
    print("=" * 60)
    
    plaintext1 = method1_step_by_step()
    a_comb, b_comb, plaintext2 = method2_combined_key()
    method3_verify()
    method4_online_tools()
    bonus_math_theory()
    
    print("\n" + "=" * 60)
    print("✅ สรุปคำตอบ")
    print("=" * 60)
    
    print(f"\nKeys:")
    print(f"  Gate 1: a₁={A1}, b₁={B1}")
    print(f"  Gate 2: a₂={A2}, b₂={B2}")
    print(f"  Combined: a={a_comb}, b={b_comb}")
    
    print(f"\nPlaintext: {plaintext1}")
    
    # สร้าง flag
    flag_content = "DOUBLE_LAYER_EXPERT"
    flag_hash = hashlib.md5(flag_content.encode()).hexdigest()
    print(f"Flag: flag{{{flag_hash}}}")

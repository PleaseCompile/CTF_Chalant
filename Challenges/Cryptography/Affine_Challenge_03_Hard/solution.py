"""
รหัสลึกลับแห่งนักเล่นแร่แปรธาตุ (The Alchemist's Mystery) - Solution
==================================================================

Challenge: Hard Affine Cipher CTF (No Key Given)
Concept: Brute Force / Frequency Analysis / Known Plaintext Attack

Difficulty: ⭐⭐⭐⭐☆

Multiple methods: Brute Force, Frequency Analysis, Known Plaintext
"""

import hashlib
from math import gcd
from collections import Counter

# ===== ข้อมูลโจทย์ =====
CIPHERTEXT = "SQJUIRFBHNWVASPFWRAQVTRHSJW"
M = 26  # จำนวนตัวอักษรในตารางแอลฟาเบต

# ค่าที่ถูกต้อง (สำหรับตรวจสอบ)
CORRECT_A = 11
CORRECT_B = 17


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


def method1_bruteforce():
    """
    วิธีที่ 1: Brute Force Attack
    =============================
    
    ลองทุก key ที่เป็นไปได้ (312 keys)
    และหาผลลัพธ์ที่อ่านออก
    """
    print("=" * 60)
    print("วิธีที่ 1: Brute Force Attack")
    print("=" * 60)
    
    # ค่า a ที่เป็นไปได้ (coprime กับ 26)
    valid_a = [a for a in range(1, 26) if gcd(a, 26) == 1]
    print(f"Valid 'a' values: {valid_a}")
    print(f"Total possible keys: {len(valid_a)} × 26 = {len(valid_a) * 26}")
    
    print("\n🔍 กำลังค้นหา keys ที่ให้ผลลัพธ์ที่อ่านออก...")
    
    # คำที่มักพบในภาษาอังกฤษ
    common_words = ["THE", "FLAG", "AND", "FOR", "ARE", "BUT", "NOT", "YOU", "ALL", "CAN"]
    
    found_keys = []
    for a in valid_a:
        for b in range(26):
            result = affine_decrypt(CIPHERTEXT, a, b)
            if result:
                # ตรวจสอบว่ามีคำที่อ่านออกหรือไม่
                score = sum(1 for word in common_words if word in result)
                if score >= 2 or "THEFLAG" in result:
                    found_keys.append((a, b, result, score))
                    print(f"  ✓ a={a:2d}, b={b:2d}: {result} (score={score})")
    
    if found_keys:
        best = max(found_keys, key=lambda x: x[3])
        print(f"\n🎯 Best match: a={best[0]}, b={best[1]}")
        print(f"   Plaintext: {best[2]}")
        return best[0], best[1], best[2]
    
    return None, None, None


def method2_frequency_analysis():
    """
    วิธีที่ 2: Frequency Analysis
    =============================
    
    วิเคราะห์ความถี่ตัวอักษรใน ciphertext
    และเปรียบเทียบกับภาษาอังกฤษ
    """
    print("\n" + "=" * 60)
    print("วิธีที่ 2: Frequency Analysis")
    print("=" * 60)
    
    # ความถี่ตัวอักษรในภาษาอังกฤษ (เรียงจากมากไปน้อย)
    english_freq = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
    
    # นับความถี่ใน ciphertext
    freq = Counter(CIPHERTEXT)
    cipher_freq = ''.join([char for char, _ in freq.most_common()])
    
    print(f"English frequency order: {english_freq[:10]}...")
    print(f"Cipher frequency order:  {cipher_freq[:10]}...")
    
    print("\nFrequency count in ciphertext:")
    for char, count in freq.most_common():
        bar = "█" * count
        print(f"  {char}: {count:2d} {bar}")
    
    # สมมติว่าตัวที่พบมากที่สุดใน ciphertext คือ E
    if freq:
        most_common_cipher = freq.most_common(1)[0][0]
        print(f"\n🔍 Most common in ciphertext: '{most_common_cipher}'")
        print(f"   If this maps to 'E', we can derive possible keys...")
        
        # ถ้า E(4) → most_common_cipher
        # (a*4 + b) mod 26 = cipher_pos
        cipher_pos = ord(most_common_cipher) - ord('A')
        print(f"   cipher position: {cipher_pos}")


def method3_known_plaintext():
    """
    วิธีที่ 3: Known Plaintext Attack
    =================================
    
    ถ้าเรารู้ว่าข้อความเริ่มด้วย "THEFLAG"
    เราสามารถคำนวณหา a และ b ได้
    """
    print("\n" + "=" * 60)
    print("วิธีที่ 3: Known Plaintext Attack")
    print("=" * 60)
    
    # สมมติว่า plaintext เริ่มด้วย "THEFLAG"
    known_plain = "THEFLAG"
    known_cipher = CIPHERTEXT[:7]
    
    print(f"Known plaintext:  {known_plain}")
    print(f"Known ciphertext: {known_cipher}")
    
    # จากสูตร: y = ax + b (mod 26)
    # ใช้ 2 คู่ตัวอักษรเพื่อแก้สมการ
    
    # T(19) → S(18): 18 = 19a + b (mod 26)
    # H(7) → Q(16):  16 = 7a + b (mod 26)  [แก้ไข: H→Q ไม่ใช่ H→J]
    
    # ตรวจสอบการจับคู่
    print("\nLetter mappings:")
    for p, c in zip(known_plain, known_cipher):
        p_val = ord(p) - ord('A')
        c_val = ord(c) - ord('A')
        print(f"  {p}({p_val:2d}) → {c}({c_val:2d})")
    
    # แก้สมการ
    print("\nSolving equations:")
    print("  From T→S: 18 = 19a + b (mod 26)  ... (1)")
    print("  From H→Q: 16 = 7a + b (mod 26)   ... (2)")
    print("  Subtract: 2 = 12a (mod 26)")
    
    # หา a จาก 12a ≡ 2 (mod 26)
    # ลดรูป: 6a ≡ 1 (mod 13)
    # a ≡ 11 (mod 13)
    
    # ลองค่า a ที่เป็นไปได้
    valid_a = [a for a in range(1, 26) if gcd(a, 26) == 1]
    
    print("\n🔍 Testing possible 'a' values:")
    for a in valid_a:
        if (12 * a) % 26 == 2:
            # หา b จากสมการ (1): b = 18 - 19a (mod 26)
            b = (18 - 19 * a) % 26
            result = affine_decrypt(CIPHERTEXT, a, b)
            print(f"  ✓ a={a:2d}, b={b:2d}: {result}")
            if "THEFLAG" in result:
                print(f"\n🎯 Found! a={a}, b={b}")
                return a, b, result
    
    return None, None, None


def method4_online_tools():
    """
    วิธีที่ 4: ใช้เครื่องมือออนไลน์
    ================================
    """
    print("\n" + "=" * 60)
    print("วิธีที่ 4: ใช้เครื่องมือออนไลน์")
    print("=" * 60)
    
    print("""
    เครื่องมือออนไลน์ที่รองรับ Automatic Decryption:
    
    1. dCode (https://www.dcode.fr/affine-cipher)
       - วาง ciphertext
       - เลือก "Automatic Decryption" หรือ "Brute Force"
       - ระบบจะลอง keys ทั้งหมดและแสดงผลที่อ่านออก
    
    2. CyberChef (https://gchq.github.io/CyberChef/)
       - ใช้ "Affine Cipher Brute Force" recipe
       - หรือลอง keys ทีละค่า
    
    3. Boxentriq (https://www.boxentriq.com/code-breaking/affine-cipher)
       - มี auto-solve feature
       - รองรับ frequency analysis
    
    4. Rumkin (http://rumkin.com/tools/cipher/affine.php)
       - ลอง keys ทีละค่า
       - เหมาะสำหรับ manual testing
    """)


def bonus_cryptanalysis():
    """
    Bonus: ทฤษฎี Cryptanalysis สำหรับ Affine Cipher
    ===============================================
    """
    print("\n" + "=" * 60)
    print("📚 Bonus: Cryptanalysis Theory")
    print("=" * 60)
    
    print("""
    วิธีโจมตี Affine Cipher:
    ========================
    
    1. Brute Force (312 keys)
       - ลองทุก a ∈ {1,3,5,7,9,11,15,17,19,21,23,25}
       - ลองทุก b ∈ {0,1,2,...,25}
       - รวม 12 × 26 = 312 keys
       - ใช้เวลาไม่กี่วินาทีด้วยคอมพิวเตอร์
    
    2. Frequency Analysis
       - นับความถี่ตัวอักษรใน ciphertext
       - เปรียบเทียบกับความถี่ในภาษาอังกฤษ
       - สมมติว่าตัวที่พบมากที่สุดคือ E หรือ T
       - แก้สมการหา a, b
    
    3. Known Plaintext Attack
       - ถ้ารู้แม้แค่ 2 ตัวอักษรของ plaintext
       - สามารถตั้งสมการและแก้หา a, b ได้
       - ตัวอย่าง: รู้ว่าเริ่มด้วย "TH" หรือ "THE"
    
    4. Ciphertext-Only Attack
       - ใช้ digraph/trigraph frequency
       - TH, HE, IN, ER พบบ่อยในภาษาอังกฤษ
       - วิเคราะห์ pattern ในข้อความ
    
    ทำไม Affine Cipher ถึงไม่ปลอดภัย?
    --------------------------------
    - Key space เล็กมาก (312 keys)
    - เป็น monoalphabetic → อ่อนต่อ frequency analysis
    - สามารถ crack ได้ในเวลาไม่กี่วินาที
    """)


if __name__ == "__main__":
    print("🔮 รหัสลึกลับแห่งนักเล่นแร่แปรธาตุ - Solution")
    print("=" * 60)
    print("Difficulty: ⭐⭐⭐⭐☆ (Hard)")
    print("=" * 60)
    
    a, b, plaintext = method1_bruteforce()
    method2_frequency_analysis()
    method3_known_plaintext()
    method4_online_tools()
    bonus_cryptanalysis()
    
    print("\n" + "=" * 60)
    print("✅ สรุปคำตอบ")
    print("=" * 60)
    
    # ถอดรหัสด้วย key ที่ถูกต้อง
    correct_plaintext = affine_decrypt(CIPHERTEXT, CORRECT_A, CORRECT_B)
    print(f"Key: a={CORRECT_A}, b={CORRECT_B}")
    print(f"Plaintext: {correct_plaintext}")
    
    # สร้าง flag
    flag_content = "CRYPTOGRAPHY_MASTER"
    flag_hash = hashlib.md5(flag_content.encode()).hexdigest()
    print(f"Flag: flag{{{flag_hash}}}")

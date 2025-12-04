"""
The Prime Minister's Secret - Solution
RSA Decryption Challenge

Multiple methods: Manual, Script, Online Tools
"""

def gcd(a, b):
    """คำนวณ Greatest Common Divisor"""
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    """คำนวณ modular multiplicative inverse"""
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd_val, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd_val, x, y
    
    _, x, _ = extended_gcd(e % phi, phi)
    return (x % phi + phi) % phi

def method1_manual():
    """
    วิธีที่ 1: ทำมือ (Manual Calculation)
    
    ขั้นตอน:
    1. จากข้อมูลที่ได้: p=61, q=53, n=3233, e=17, c=2790
    2. คำนวณ φ(n) = (p-1) × (q-1) = 60 × 52 = 3120
    3. คำนวณ d = e^(-1) mod φ(n) 
       หา d ที่ทำให้ (e × d) mod φ(n) = 1
       (17 × d) mod 3120 = 1
       d = 2753
    4. ถอดรหัส: m = c^d mod n = 2790^2753 mod 3233 = 65
    5. 65 ใน ASCII = 'A' (แต่นี่แค่ตัวอย่าง)
    """
    print("=== วิธีที่ 1: Manual Calculation ===")
    print("1. p = 61, q = 53")
    print("2. n = p × q = 3233")
    print("3. φ(n) = (p-1) × (q-1) = 60 × 52 = 3120")
    print("4. d = e^(-1) mod φ(n)")
    print("   หา d ที่ทำให้ (17 × d) mod 3120 = 1")
    print("   d = 2753")
    print("5. ถอดรหัส: m = c^d mod n")
    print()

def method2_script():
    """
    วิธีที่ 2: ใช้ Python Script
    """
    print("=== วิธีที่ 2: Python Script ===")
    
    # Given values from data.txt
    p = 61
    q = 53
    n = 3233  # p * q
    e = 17
    
    # Encrypted message (each number is an encrypted character)
    encrypted_message = [
        1369, 745, 1632, 2923, 855, 
        2412, 1230, 1632, 119, 612, 
        2412, 2906, 2271, 368, 119, 
        612, 624, 1107, 368, 2412, 
        1516
    ]
    
    # Calculate φ(n) = (p-1)(q-1)
    phi_n = (p - 1) * (q - 1)
    print(f"φ(n) = (p-1)(q-1) = {phi_n}")
    
    # Calculate private key d
    d = mod_inverse(e, phi_n)
    print(f"d = {d}")
    
    # Verify: (e * d) mod φ(n) should equal 1
    print(f"Verification: (e × d) mod φ(n) = {(e * d) % phi_n}")
    
    # Decrypt each character
    decrypted_chars = []
    for c in encrypted_message:
        m = pow(c, d, n)  # m = c^d mod n
        decrypted_chars.append(chr(m))
    
    flag = ''.join(decrypted_chars)
    print(f"\n🚩 Flag: {flag}")
    return flag

def method3_online_tools():
    """
    วิธีที่ 3: ใช้ Online Tools
    
    เครื่องมือที่แนะนำ:
    1. dCode RSA Cipher: https://www.dcode.fr/rsa-cipher
    2. RsaCtfTool: https://github.com/Ganapati/RsaCtfTool
    3. CyberChef: https://gchq.github.io/CyberChef/
    4. Online RSA Calculator: https://www.cs.drexel.edu/~jpopyack/IntroCS/HW/RSAWorksheet.html
    
    ขั้นตอน (dCode):
    1. ไปที่ https://www.dcode.fr/rsa-cipher
    2. เลือก "Decrypt"
    3. ใส่ค่า:
       - Modulo N: 3233
       - Public Exponent E: 17
       - Prime P: 61
       - Prime Q: 53
       - Encrypted Message: แต่ละตัวเลขใน list
    4. กด Decrypt
    """
    print("=== วิธีที่ 3: Online Tools ===")
    print("1. dCode RSA Cipher: https://www.dcode.fr/rsa-cipher")
    print("2. RsaCtfTool: https://github.com/Ganapati/RsaCtfTool")
    print("3. Online RSA Calculator")
    print()
    print("ขั้นตอน:")
    print("1. ใส่ค่า n=3233, e=17, p=61, q=53")
    print("2. ถอดรหัสแต่ละตัวเลขใน encrypted_message")
    print("3. แปลงผลลัพธ์เป็น ASCII characters")

def bonus_theory():
    """
    Bonus: ทฤษฎี RSA
    
    RSA (Rivest-Shamir-Adleman) เป็นระบบเข้ารหัสแบบ asymmetric
    
    การสร้างกุญแจ:
    1. เลือก prime numbers p และ q
    2. คำนวณ n = p × q
    3. คำนวณ φ(n) = (p-1)(q-1)  (Euler's totient)
    4. เลือก e ที่ 1 < e < φ(n) และ gcd(e, φ(n)) = 1
    5. คำนวณ d = e^(-1) mod φ(n)
    
    Public Key: (n, e)
    Private Key: (n, d)
    
    การเข้ารหัส: c = m^e mod n
    การถอดรหัส: m = c^d mod n
    
    ความปลอดภัย:
    - อยู่บนความยากของการ factorize n กลับเป็น p × q
    - ถ้าใครรู้ p และ q ก็สามารถคำนวณ d และถอดรหัสได้
    """
    print("=== Bonus: RSA Theory ===")
    print("RSA ตั้งชื่อตาม: Rivest, Shamir, Adleman")
    print()
    print("Key Generation:")
    print("1. Choose primes p, q")
    print("2. n = p × q")
    print("3. φ(n) = (p-1)(q-1)")
    print("4. Choose e where gcd(e, φ(n)) = 1")
    print("5. d = e^(-1) mod φ(n)")
    print()
    print("Encryption: c = m^e mod n")
    print("Decryption: m = c^d mod n")

def generate_challenge():
    """
    ฟังก์ชันสำหรับสร้าง challenge ใหม่
    """
    import hashlib
    
    p = 61
    q = 53
    n = p * q  # 3233
    e = 17
    phi_n = (p - 1) * (q - 1)  # 3120
    d = mod_inverse(e, phi_n)  # 2753
    
    # Create a simple flag message
    flag_content = "rsa_pr1m3_p0w3r"
    flag = f"flag{{{flag_content}}}"
    
    print(f"Generating challenge with flag: {flag}")
    print(f"d = {d}")
    
    # Encrypt each character
    encrypted = []
    for char in flag:
        m = ord(char)
        c = pow(m, e, n)
        encrypted.append(c)
    
    print(f"Encrypted: {encrypted}")
    
    # Verify decryption
    decrypted = ''.join([chr(pow(c, d, n)) for c in encrypted])
    print(f"Decryption verification: {decrypted}")
    
    return encrypted

if __name__ == "__main__":
    print("=" * 60)
    print("The Prime Minister's Secret - RSA Solution")
    print("=" * 60)
    print()
    
    method1_manual()
    print()
    
    flag = method2_script()
    print()
    
    method3_online_tools()
    print()
    
    bonus_theory()
    print()
    
    print("=" * 60)
    print("Challenge Generation (for reference)")
    print("=" * 60)
    generate_challenge()

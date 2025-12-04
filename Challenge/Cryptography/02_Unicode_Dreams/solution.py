"""
Unicode Dreams - Solution
=========================
Challenge: Decode the bootstring encoded messages
Flag: flag{8806bc86bb52331ed1043c0a1f13dd50}

Multiple solution methods provided below.
"""

import codecs

# ============================================
# Method 1: Manual Python Script
# ============================================
def method1_python_script():
    """
    วิธีที่ 1: ใช้ Python decode punycode
    
    ในโจทย์นี้ ข้อมูลไม่มี prefix 'xn--' 
    แต่ยังคงเป็น punycode encoding เหมือนเดิม
    """
    
    # Encoded messages from data.txt (without xn-- prefix)
    encoded_messages = [
        ("l3c1bib8a0a", "MSG #1"),
        ("l3cckcf7bl2ftbxn5v", "MSG #2"),
        ("12ca4e2dn1h", "MSG #3"),
        ("8806bc86bb52331ed1043c0a1f13dd50-ek7g0t", "MSG #4 - CLASSIFIED"),
    ]
    
    print("=== Method 1: Python Punycode Decode ===\n")
    
    for encoded, label in encoded_messages:
        # Decode directly (no need to remove prefix)
        decoded = encoded.encode('ascii').decode('punycode')
        print(f"[{label}]")
        print(f"Encoded: {encoded}")
        print(f"Decoded: {decoded}")
        print("-" * 40)
    
    # Extract flag from last decoded message
    print("\n📝 Translation of decoded Thai text:")
    print("MSG #1: สวัสดี = Hello")
    print("MSG #2: ยินดีต้อนรับ = Welcome")
    print("MSG #3: นักแฮก = Hacker")
    print("MSG #4: ธง = Flag + MD5 hash")
    
    print("\n🚩 FLAG: flag{8806bc86bb52331ed1043c0a1f13dd50}")


# ============================================
# Method 2: Using codecs module  
# ============================================
def method2_codecs():
    """
    วิธีที่ 2: ใช้ codecs module
    """
    
    print("\n=== Method 2: Using codecs module ===\n")
    
    target = "8806bc86bb52331ed1043c0a1f13dd50-ek7g0t"
    
    # Using codecs
    decoded = codecs.decode(target, 'punycode')
    print(f"Target: {target}")
    print(f"Decoded: {decoded}")
    
    # The Thai character ธง means "flag"
    print("\nธง (Thai) = 'flag' (English)")
    flag_hash = decoded[2:]  # Skip ธง (2 characters)
    print(f"\n🚩 FLAG: flag{{{flag_hash}}}")


# ============================================
# Method 3: Online Tools
# ============================================
def method3_online_tools():
    """
    วิธีที่ 3: ใช้เครื่องมือออนไลน์
    
    Online Punycode Converters:
    1. https://www.punycoder.com/
    2. https://mothereff.in/punycode
    3. https://onlinetools.com/unicode/convert-punycode-to-unicode
    
    ข้อควรระวัง: เครื่องมือบางตัวอาจต้องการ prefix 'xn--'
    ถ้าไม่ทำงาน ให้ลองเพิ่ม xn-- ข้างหน้า
    
    ขั้นตอน:
    1. ไปที่เว็บไซต์ด้านบน
    2. วาง 8806bc86bb52331ed1043c0a1f13dd50-ek7g0t
       หรือ xn--8806bc86bb52331ed1043c0a1f13dd50-ek7g0t
    3. คลิก Decode
    4. จะได้: ธง8806bc86bb52331ed1043c0a1f13dd50
    5. 'ธง' คือ 'flag' ในภาษาไทย
    6. flag คือ: flag{8806bc86bb52331ed1043c0a1f13dd50}
    """
    
    print("\n=== Method 3: Online Tools ===\n")
    print("Recommended online tools:")
    print("1. https://www.punycoder.com/")
    print("2. https://mothereff.in/punycode")
    print("3. https://onlinetools.com/unicode/convert-punycode-to-unicode")
    print("\nNote: Some tools may require 'xn--' prefix")
    print("Try: xn--8806bc86bb52331ed1043c0a1f13dd50-ek7g0t")
    print("\n🚩 FLAG: flag{8806bc86bb52331ed1043c0a1f13dd50}")


# ============================================
# Method 4: Decode All Messages
# ============================================
def method4_decode_all():
    """
    วิธีที่ 4: Decode ทุกข้อความ
    """
    
    print("\n=== Method 4: Decode All Messages ===\n")
    
    messages = [
        "l3c1bib8a0a",
        "l3cckcf7bl2ftbxn5v",
        "12ca4e2dn1h",
        "8806bc86bb52331ed1043c0a1f13dd50-ek7g0t"
    ]
    
    translations = {
        "สวัสดี": "Hello",
        "ยินดีต้อนรับ": "Welcome", 
        "นักแฮก": "Hacker",
    }
    
    for i, msg in enumerate(messages, 1):
        decoded = msg.encode('ascii').decode('punycode')
        meaning = translations.get(decoded, "Contains the flag!")
        print(f"Message {i}: {msg}")
        print(f"  Decoded: {decoded}")
        print(f"  Meaning: {meaning}")
        print()
    
    print("🚩 FLAG: flag{8806bc86bb52331ed1043c0a1f13dd50}")


# ============================================
# Bonus: Punycode Structure Explained
# ============================================
def bonus_theory():
    """
    Bonus: โครงสร้าง Punycode
    
    Punycode string ประกอบด้วย:
    1. Basic code points (ASCII) ที่อยู่ด้านหน้า
    2. Delimiter '-' (ถ้ามี basic code points)
    3. Extended code points ที่ถูก encode
    
    ตัวอย่าง: 8806bc86bb52331ed1043c0a1f13dd50-ek7g0t
    - 8806bc86bb52331ed1043c0a1f13dd50 = ASCII part (MD5 hash)
    - ek7g0t = encoded Thai characters (ธง)
    """
    
    print("\n=== Bonus: Punycode Structure ===\n")
    
    print("Punycode format: [basic_ascii]-[encoded_unicode]")
    print()
    print("Example breakdown:")
    print("8806bc86bb52331ed1043c0a1f13dd50-ek7g0t")
    print("├── 8806bc86bb52331ed1043c0a1f13dd50 (ASCII part)")
    print("└── ek7g0t (encoded Thai: ธง)")
    print()
    print("When decoded: ธง8806bc86bb52331ed1043c0a1f13dd50")
    print("ธง = 'flag' in Thai")


# ============================================
# Main
# ============================================
if __name__ == "__main__":
    print("=" * 50)
    print("Unicode Dreams - Solution")
    print("=" * 50)
    
    method1_python_script()
    method2_codecs()
    method3_online_tools()
    method4_decode_all()
    bonus_theory()
    
    print("\n" + "=" * 50)
    print("🎉 FINAL FLAG: flag{8806bc86bb52331ed1043c0a1f13dd50}")
    print("=" * 50)

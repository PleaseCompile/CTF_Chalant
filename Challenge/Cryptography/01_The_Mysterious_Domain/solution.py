"""
The Mysterious Domain - Solution
================================
Challenge: Decode the mysterious xn-- domains
Flag: flag{1c39255b1ff406a693c40afffba5167e}

Multiple solution methods provided below.
"""

import codecs

# ============================================
# Method 1: Manual Python Script
# ============================================
def method1_python_script():
    """
    วิธีที่ 1: ใช้ Python decode punycode
    
    Punycode เป็นการเข้ารหัสที่ใช้กับ Internationalized Domain Names (IDN)
    - prefix xn-- บ่งบอกว่าเป็น punycode
    - ใช้ในการแปลง Unicode เป็น ASCII สำหรับ DNS
    """
    
    # Encoded domains from data.txt
    encoded_domains = [
        "xn--42c8buaqi6de",           # LOG ENTRY 001
        "xn--c3c2aa9a3cb9fudubf",     # LOG ENTRY 002
        "xn--l3ckx7ji",               # LOG ENTRY 003
        "xn--1c39255b1ff406a693c40afffba5167e-kh7god82awxrl",  # PRIMARY TARGET
    ]
    
    print("=== Method 1: Python Punycode Decode ===\n")
    
    for domain in encoded_domains:
        # Remove 'xn--' prefix before decoding
        punycode_part = domain[4:]  # Remove 'xn--'
        
        # Decode using punycode
        decoded = punycode_part.encode('ascii').decode('punycode')
        print(f"Encoded: {domain}")
        print(f"Decoded: {decoded}")
        print("-" * 40)
    
    # Extract flag from last decoded message
    last_decoded = "ธงคือ1c39255b1ff406a693c40afffba5167e"
    flag_hash = last_decoded.replace("ธงคือ", "")  # Remove Thai prefix "ธงคือ" (means "flag is")
    print(f"\n🚩 FLAG: flag{{{flag_hash}}}")


# ============================================
# Method 2: Using codecs module
# ============================================
def method2_codecs():
    """
    วิธีที่ 2: ใช้ codecs module
    
    Python's codecs module รองรับ punycode encoding/decoding โดยตรง
    """
    
    print("\n=== Method 2: Using codecs module ===\n")
    
    target = "xn--1c39255b1ff406a693c40afffba5167e-kh7god82awxrl"
    punycode_part = target[4:]  # Remove 'xn--'
    
    # Using codecs
    decoded = codecs.decode(punycode_part, 'punycode')
    print(f"Target: {target}")
    print(f"Decoded: {decoded}")
    
    # Extract hash (after Thai characters)
    # Use replace() for consistency and robustness with Thai characters
    flag_hash = decoded.replace("ธงคือ", "")  # Remove Thai prefix "ธงคือ" (means "flag is")
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
    3. https://www.browserling.com/tools/punycode-decode
    4. https://www.name.com/punycode-converter
    
    ขั้นตอน:
    1. ไปที่เว็บไซต์ด้านบน
    2. วาง xn--1c39255b1ff406a693c40afffba5167e-kh7god82awxrl
    3. คลิก Decode
    4. จะได้: ธงคือ1c39255b1ff406a693c40afffba5167e
    5. 'ธงคือ' คือ 'flag is' ในภาษาไทย
    6. ดังนั้น flag คือ: flag{1c39255b1ff406a693c40afffba5167e}
    """
    
    print("\n=== Method 3: Online Tools ===\n")
    print("Recommended online tools:")
    print("1. https://www.punycoder.com/")
    print("2. https://mothereff.in/punycode")
    print("3. https://www.browserling.com/tools/punycode-decode")
    print("\nSteps:")
    print("1. Go to any online punycode decoder")
    print("2. Paste: xn--1c39255b1ff406a693c40afffba5167e-kh7god82awxrl")
    print("3. Decode to get: ธงคือ1c39255b1ff406a693c40afffba5167e")
    print("4. 'ธงคือ' means 'flag is' in Thai")
    print("\n🚩 FLAG: flag{1c39255b1ff406a693c40afffba5167e}")


# ============================================
# Method 4: Command Line (Linux/Mac)
# ============================================
def method4_command_line():
    """
    วิธีที่ 4: ใช้ Command Line
    
    Linux/Mac มี idn command สำหรับ decode
    หรือใช้ Python one-liner
    """
    
    print("\n=== Method 4: Command Line ===\n")
    print("Option A - Using Python one-liner:")
    print('python3 -c "print(\'1c39255b1ff406a693c40afffba5167e-kh7god82awxrl\'.encode(\'ascii\').decode(\'punycode\'))"')
    print("\nOption B - Using idn command (if available):")
    print("echo 'xn--1c39255b1ff406a693c40afffba5167e-kh7god82awxrl' | idn --decode")
    print("\n🚩 FLAG: flag{1c39255b1ff406a693c40afffba5167e}")


# ============================================
# Bonus: Understanding Punycode
# ============================================
def bonus_theory():
    """
    Bonus: ทฤษฎี Punycode
    
    Punycode คืออะไร?
    - เป็นการเข้ารหัสที่ใช้ใน Internationalized Domain Names (IDN)
    - แปลง Unicode ให้เป็น ASCII-compatible encoding (ACE)
    - prefix 'xn--' บ่งบอกว่าเป็น Punycode encoded string
    
    ทำไมต้องใช้?
    - DNS system รองรับเฉพาะ ASCII characters
    - เพื่อให้ domain names ภาษาอื่นๆ ใช้งานได้ (เช่น ไทย, จีน, อาหรับ)
    
    RFC 3492 - Punycode: A Bootstring encoding of Unicode
    """
    
    print("\n=== Bonus: Punycode Theory ===\n")
    
    # Example encoding
    examples = [
        ("münchen", "German city"),
        ("北京", "Beijing in Chinese"),
        ("กรุงเทพ", "Bangkok in Thai"),
    ]
    
    print("How Punycode works:\n")
    for text, description in examples:
        encoded = text.encode('punycode').decode('ascii')
        print(f"Original: {text} ({description})")
        print(f"Punycode: xn--{encoded}")
        print()


# ============================================
# Main
# ============================================
if __name__ == "__main__":
    print("=" * 50)
    print("The Mysterious Domain - Solution")
    print("=" * 50)
    
    method1_python_script()
    method2_codecs()
    method3_online_tools()
    method4_command_line()
    bonus_theory()
    
    print("\n" + "=" * 50)
    print("🎉 FINAL FLAG: flag{1c39255b1ff406a693c40afffba5167e}")
    print("=" * 50)

"""
Unicode Dreams - Solution (HARD MODE)
=====================================
Challenge: Decode Base64 wrapped Punycode messages
Flag: flag{1c39255b1ff406a693c40afffba5167e}

This challenge requires TWO decoding steps:
1. First: Base64 decode
2. Then: Punycode decode

Multiple solution methods provided below.
"""

import codecs
import base64

# ============================================
# Method 1: Manual Python Script (Two-step decode)
# ============================================
def method1_python_script():
    """
    วิธีที่ 1: ใช้ Python decode Base64 แล้วต่อด้วย Punycode
    
    โจทย์นี้ยากขึ้นเพราะมี 2 ชั้นการเข้ารหัส:
    1. Punycode (Unicode → ASCII)
    2. Base64 (ซ่อน Punycode อีกชั้น)
    """
    
    # Encoded messages from data.txt (Base64 wrapped)
    encoded_messages = [
        ("bDNjMWJpYjhhMGE=", "MSG #1"),
        ("bDNjY2tjZjdibDJmdGJ4bjV2", "MSG #2"),
        ("MTJjYTRlMmRuMWg=", "MSG #3"),
        ("MWMzOTI1NWIxZmY0MDZhNjkzYzQwYWZmZmJhNTE2N2UtZWs3ZzB0", "MSG #4 - CLASSIFIED"),
    ]
    
    print("=== Method 1: Two-Step Decode (Base64 → Punycode) ===\n")
    
    for b64_encoded, label in encoded_messages:
        # Step 1: Base64 decode
        punycode_str = base64.b64decode(b64_encoded).decode('ascii')
        print(f"[{label}]")
        print(f"Base64 Input: {b64_encoded}")
        print(f"After Base64: {punycode_str}")
        
        # Step 2: Punycode decode
        decoded = punycode_str.encode('ascii').decode('punycode')
        print(f"Final Output: {decoded}")
        print("-" * 50)
    
    # Extract flag from last decoded message
    print("\n📝 Translation of decoded Thai text:")
    print("MSG #1: สวัสดี = Hello")
    print("MSG #2: ยินดีต้อนรับ = Welcome")
    print("MSG #3: นักแฮก = Hacker")
    print("MSG #4: ธง = Flag + MD5 hash")
    
    print("\n🚩 FLAG: flag{1c39255b1ff406a693c40afffba5167e}")


# ============================================
# Method 2: Using codecs module  
# ============================================
def method2_codecs():
    """
    วิธีที่ 2: ใช้ codecs module + base64
    """
    
    print("\n=== Method 2: Using codecs + base64 modules ===\n")
    
    # Target message (Base64 encoded)
    b64_target = "MWMzOTI1NWIxZmY0MDZhNjkzYzQwYWZmZmJhNTE2N2UtZWs3ZzB0"
    
    # Step 1: Base64 decode
    punycode_str = base64.b64decode(b64_target).decode('ascii')
    print(f"Base64 Input: {b64_target}")
    print(f"After Base64: {punycode_str}")
    
    # Step 2: Using codecs for punycode
    decoded = codecs.decode(punycode_str, 'punycode')
    print(f"Final Decoded: {decoded}")
    
    # The Thai character ธง means "flag" in English
    print("\nธง (Thai) = 'flag' (English)")
    # Use replace() for robustness with Thai characters
    flag_hash = decoded.replace("ธง", "")  # Remove Thai prefix "ธง" (means "flag")
    print(f"\n🚩 FLAG: flag{{{flag_hash}}}")


# ============================================
# Method 3: Online Tools (Two-step process)
# ============================================
def method3_online_tools():
    """
    วิธีที่ 3: ใช้เครื่องมือออนไลน์ (ต้องทำ 2 ขั้นตอน)
    
    ขั้นตอนที่ 1 - Base64 Decode:
    - https://www.base64decode.org/
    - https://base64.guru/converter/decode
    
    ขั้นตอนที่ 2 - Punycode Decode:
    - https://www.punycoder.com/
    - https://mothereff.in/punycode
    
    ขั้นตอน:
    1. นำ MWMzOTI1NWIxZmY0MDZhNjkzYzQwYWZmZmJhNTE2N2UtZWs3ZzB0 ไป decode Base64
    2. จะได้: 1c39255b1ff406a693c40afffba5167e-ek7g0t
    3. นำไป decode Punycode
    4. จะได้: ธง1c39255b1ff406a693c40afffba5167e
    5. 'ธง' คือ 'flag' ในภาษาไทย
    6. flag คือ: flag{1c39255b1ff406a693c40afffba5167e}
    """
    
    print("\n=== Method 3: Online Tools (Two Steps) ===\n")
    print("STEP 1 - Base64 Decode:")
    print("  Tool: https://www.base64decode.org/")
    print("  Input: MWMzOTI1NWIxZmY0MDZhNjkzYzQwYWZmZmJhNTE2N2UtZWs3ZzB0")
    print("  Output: 1c39255b1ff406a693c40afffba5167e-ek7g0t")
    print()
    print("STEP 2 - Punycode Decode:")
    print("  Tool: https://www.punycoder.com/")
    print("  Input: 1c39255b1ff406a693c40afffba5167e-ek7g0t")
    print("  Output: ธง1c39255b1ff406a693c40afffba5167e")
    print()
    print("Note: 'ธง' means 'flag' in Thai")
    print("\n🚩 FLAG: flag{1c39255b1ff406a693c40afffba5167e}")


# ============================================
# Method 4: Python One-liner
# ============================================
def method4_oneliner():
    """
    วิธีที่ 4: Python One-liner
    """
    
    print("\n=== Method 4: Python One-liner ===\n")
    
    oneliner = '''python3 -c "import base64; print(base64.b64decode('MWMzOTI1NWIxZmY0MDZhNjkzYzQwYWZmZmJhNTE2N2UtZWs3ZzB0').decode().encode('ascii').decode('punycode'))"'''
    
    print("Command:")
    print(oneliner)
    print("\nOutput: ธง1c39255b1ff406a693c40afffba5167e")
    print("\n🚩 FLAG: flag{1c39255b1ff406a693c40afffba5167e}")


# ============================================
# Method 5: Decode All Messages
# ============================================
def method5_decode_all():
    """
    วิธีที่ 5: Decode ทุกข้อความ
    """
    
    print("\n=== Method 5: Decode All Messages ===\n")
    
    messages = [
        "bDNjMWJpYjhhMGE=",
        "bDNjY2tjZjdibDJmdGJ4bjV2",
        "MTJjYTRlMmRuMWg=",
        "MWMzOTI1NWIxZmY0MDZhNjkzYzQwYWZmZmJhNTE2N2UtZWs3ZzB0"
    ]
    
    translations = {
        "สวัสดี": "Hello",
        "ยินดีต้อนรับ": "Welcome", 
        "นักแฮก": "Hacker",
    }
    
    for i, b64_msg in enumerate(messages, 1):
        # Two-step decode
        punycode_str = base64.b64decode(b64_msg).decode('ascii')
        decoded = punycode_str.encode('ascii').decode('punycode')
        meaning = translations.get(decoded, "Contains the flag!")
        
        print(f"Message {i}:")
        print(f"  Base64: {b64_msg}")
        print(f"  Punycode: {punycode_str}")
        print(f"  Decoded: {decoded}")
        print(f"  Meaning: {meaning}")
        print()
    
    print("🚩 FLAG: flag{1c39255b1ff406a693c40afffba5167e}")


# ============================================
# Bonus: Understanding the Layered Encoding
# ============================================
def bonus_theory():
    """
    Bonus: โครงสร้างการเข้ารหัสแบบหลายชั้น
    
    Layer 1: Punycode
    - แปลง Thai text → ASCII
    - ธง1c39255b1ff406a693c40afffba5167e → 1c39255b1ff406a693c40afffba5167e-ek7g0t
    
    Layer 2: Base64
    - ซ่อน Punycode อีกชั้น
    - 1c39255b1ff406a693c40afffba5167e-ek7g0t → MWMzOTI1NWIxZmY0MDZhNjkzYzQwYWZmZmJhNTE2N2UtZWs3ZzB0
    """
    
    print("\n=== Bonus: Layered Encoding Structure ===\n")
    
    print("Encoding Process (how the challenge was created):")
    print()
    print("Step 1: Original Thai text")
    print("  → ธง1c39255b1ff406a693c40afffba5167e")
    print()
    print("Step 2: Apply Punycode encoding")
    print("  → 1c39255b1ff406a693c40afffba5167e-ek7g0t")
    print()
    print("Step 3: Apply Base64 encoding")
    print("  → MWMzOTI1NWIxZmY0MDZhNjkzYzQwYWZmZmJhNTE2N2UtZWs3ZzB0")
    print()
    print("Decoding Process (how to solve):")
    print("  Base64 → Punycode → Thai text with flag")
    print()
    print("Punycode format: [basic_ascii]-[encoded_unicode]")
    print("  1c39255b1ff406a693c40afffba5167e = ASCII (MD5 hash)")
    print("  ek7g0t = encoded Thai: ธง (flag)")


# ============================================
# Main
# ============================================
if __name__ == "__main__":
    print("=" * 55)
    print("Unicode Dreams - Solution (HARD MODE)")
    print("Two-Layer Encoding: Base64 + Punycode")
    print("=" * 55)
    
    method1_python_script()
    method2_codecs()
    method3_online_tools()
    method4_oneliner()
    method5_decode_all()
    bonus_theory()
    
    print("\n" + "=" * 55)
    print("🎉 FINAL FLAG: flag{1c39255b1ff406a693c40afffba5167e}")
    print("=" * 55)

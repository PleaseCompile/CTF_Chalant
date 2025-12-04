"""
📻 The Radio Operator's Last Transmission - Solution
====================================================

Challenge: Morse Audio Decoding
Difficulty: ⭐⭐☆☆☆ (Easy-Medium)

Multiple methods to solve this challenge:
1. Manual decoding (using Morse code chart)
2. Python script (automated decoding)
3. Online tools
4. Audio analysis tools
"""

import hashlib


# ============================================================
# Method 1: Manual Decoding (ทำมือ)
# ============================================================

def method1_manual():
    """
    วิธีที่ 1: ถอดรหัสด้วยมือโดยใช้ตาราง Morse Code
    
    ขั้นตอน:
    1. ฟังไฟล์เสียงและจดรูปแบบ:
       - เสียงสั้น = จุด (.)
       - เสียงยาว = ขีด (-)
       
    2. ใช้ตาราง Morse Code:
       A = .-      N = -.
       B = -...    O = ---
       C = -.-.    P = .--.
       D = -..     Q = --.-
       E = .       R = .-.
       F = ..-.    S = ...
       G = --.     T = -
       H = ....    U = ..-
       I = ..      V = ...-
       J = .---    W = .--
       K = -.-     X = -..-
       L = .-..    Y = -.--
       M = --      Z = --..
       
       0 = -----   5 = .....
       1 = .----   6 = -....
       2 = ..---   7 = --...
       3 = ...--   8 = ---..
       4 = ....-   9 = ----.
       
    3. Morse จากไฟล์:
       - .... .   = THE
       ... . -.-. .-. . -   = SECRET
       -- . ... ... .- --. .   = MESSAGE
       .. ...   = IS
       -.. --- - ...   = DOTS
       .- -. -..   = AND
       -.. .- ... .... . ... = DASHES
       
    4. ข้อความที่ได้: THE SECRET MESSAGE IS DOTS AND DASHES
    
    5. สร้าง flag จาก keyword: DOTS_AND_DASHES
    """
    
    morse_from_file = "- .... .   ... . -.-. .-. . -   -- . ... ... .- --. .   .. ...   -.. --- - ...   .- -. -..   -.. .- ... .... . ..."
    
    print("=" * 60)
    print("Method 1: Manual Decoding")
    print("=" * 60)
    print(f"\nMorse Code: {morse_from_file}")
    print("\nDecoded Message: THE SECRET MESSAGE IS DOTS AND DASHES")
    
    keyword = "DOTS_AND_DASHES"
    flag_hash = hashlib.md5(keyword.encode()).hexdigest()
    print(f"\nKeyword for flag: {keyword}")
    print(f"Flag: flag{{{flag_hash}}}")
    
    return f"flag{{{flag_hash}}}"


# ============================================================
# Method 2: Python Script (Automated)
# ============================================================

def method2_script():
    """
    วิธีที่ 2: ใช้ Python script ถอดรหัสอัตโนมัติ
    """
    
    # Morse Code Dictionary
    MORSE_CODE_DICT = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z', '.----': '1', '..---': '2', '...--': '3',
        '....-': '4', '.....': '5', '-....': '6', '--...': '7',
        '---..': '8', '----.': '9', '-----': '0'
    }
    
    def decode_morse(morse_code):
        """Decode Morse code to text"""
        words = morse_code.strip().split('   ')  # Words separated by 3 spaces
        decoded_message = []
        
        for word in words:
            letters = word.split(' ')  # Letters separated by 1 space
            decoded_word = ''
            for letter in letters:
                if letter in MORSE_CODE_DICT:
                    decoded_word += MORSE_CODE_DICT[letter]
            decoded_message.append(decoded_word)
        
        return ' '.join(decoded_message)
    
    # Morse code from the challenge
    morse_code = "- .... .   ... . -.-. .-. . -   -- . ... ... .- --. .   .. ...   -.. --- - ...   .- -. -..   -.. .- ... .... . ..."
    
    print("=" * 60)
    print("Method 2: Python Script (Automated)")
    print("=" * 60)
    
    decoded = decode_morse(morse_code)
    print(f"\nInput Morse: {morse_code}")
    print(f"Decoded: {decoded}")
    
    # Generate flag
    keyword = "DOTS_AND_DASHES"
    flag_hash = hashlib.md5(keyword.encode()).hexdigest()
    print(f"\nFlag: flag{{{flag_hash}}}")
    
    return f"flag{{{flag_hash}}}"


# ============================================================
# Method 3: Online Tools
# ============================================================

def method3_online():
    """
    วิธีที่ 3: ใช้เครื่องมือออนไลน์
    
    แนะนำเว็บไซต์:
    
    1. Morse Code Audio Decoder:
       - https://morsecode.world/international/decoder/audio-decoder-adaptive.html
       - อัพโหลดไฟล์ .wav แล้วจะถอดรหัสให้อัตโนมัติ
    
    2. Morse Code Translator:
       - https://morsecode.world/international/translator.html
       - แปลง morse text เป็นข้อความ
    
    3. Online Morse Decoder:
       - https://www.dcode.fr/morse-code
       - รองรับทั้ง text และ audio
    
    4. Morse Code Audio Decoder (Chrome Extension):
       - ใช้ไมโครโฟนฟังเสียง Morse แล้วถอดรหัส
    
    ขั้นตอน:
    1. ไปที่เว็บ morsecode.world
    2. เลือก "Audio Decoder"
    3. อัพโหลดไฟล์ transmission.wav
    4. รอระบบประมวลผล
    5. อ่านข้อความที่ถอดรหัสได้
    6. สร้าง flag จาก keyword ที่ได้
    """
    
    print("=" * 60)
    print("Method 3: Online Tools")
    print("=" * 60)
    print("""
Recommended Online Tools:

1. 🌐 Morse Code Audio Decoder (BEST for audio files):
   URL: https://morsecode.world/international/decoder/audio-decoder-adaptive.html
   - Upload .wav file
   - Auto-decode the audio

2. 🌐 dCode Morse Decoder:
   URL: https://www.dcode.fr/morse-code
   - Supports text and audio
   - Multi-language interface

3. 🌐 Morse Code Translator:
   URL: https://morsecode.world/international/translator.html
   - Convert morse text to message

Steps:
1. Go to morsecode.world audio decoder
2. Upload transmission.wav
3. Wait for processing
4. Read decoded message: THE SECRET MESSAGE IS DOTS AND DASHES
5. Generate flag from keyword: DOTS_AND_DASHES
    """)
    
    keyword = "DOTS_AND_DASHES"
    flag_hash = hashlib.md5(keyword.encode()).hexdigest()
    print(f"\nFlag: flag{{{flag_hash}}}")
    
    return f"flag{{{flag_hash}}}"


# ============================================================
# Method 4: Audio Analysis with Audacity
# ============================================================

def method4_audacity():
    """
    วิธีที่ 4: วิเคราะห์ไฟล์เสียงด้วย Audacity
    
    ขั้นตอน:
    1. เปิดไฟล์ transmission.wav ใน Audacity
    2. ดู waveform - จะเห็นรูปแบบ:
       - สัญญาณสั้น = จุด (dit)
       - สัญญาณยาว = ขีด (dah)
       - ช่องว่างสั้น = ระหว่างตัวอักษร
       - ช่องว่างยาว = ระหว่างคำ
    3. จดรูปแบบและถอดรหัสด้วยตาราง Morse
    
    การวิเคราะห์:
    - เสียงสั้น (dit): ~100ms, แสดงเป็นจุด (.)
    - เสียงยาว (dah): ~300ms, แสดงเป็นขีด (-)
    - ความถี่: ~700 Hz (standard CW tone)
    """
    
    print("=" * 60)
    print("Method 4: Audio Analysis with Audacity")
    print("=" * 60)
    print("""
Steps to analyze with Audacity:

1. Open Audacity (free audio software)
2. Load transmission.wav
3. Zoom in on the waveform
4. Identify patterns:
   - Short burst (~100ms) = Dit (.)
   - Long burst (~300ms) = Dah (-)
   - Short gap = between letters
   - Long gap = between words
   
5. Write down the pattern:
   - .... .   ... . -.-. .-. . -   ...
   
6. Use Morse chart to decode

Waveform Analysis:
==================
|█|   |███|   |█|   = T H E
 .     -       .
 
Time markers help identify dit vs dah!
    """)
    
    keyword = "DOTS_AND_DASHES"
    flag_hash = hashlib.md5(keyword.encode()).hexdigest()
    print(f"\nFlag: flag{{{flag_hash}}}")
    
    return f"flag{{{flag_hash}}}"


# ============================================================
# Bonus: Theory and Background
# ============================================================

def bonus_theory():
    """
    Bonus: ทฤษฎีเกี่ยวกับ Morse Code
    
    ประวัติศาสตร์:
    - คิดค้นโดย Samuel F.B. Morse และ Alfred Vail ในปี 1837
    - ใช้สำหรับโทรเลข (Telegraph)
    - ยังคงใช้ในการสื่อสาร HAM Radio และการบินจนถึงปัจจุบัน
    
    โครงสร้าง:
    - จุด (Dit): หน่วยเวลาพื้นฐาน
    - ขีด (Dah): 3 หน่วยเวลา
    - ช่องว่างระหว่างสัญญาณ: 1 หน่วยเวลา
    - ช่องว่างระหว่างตัวอักษร: 3 หน่วยเวลา
    - ช่องว่างระหว่างคำ: 7 หน่วยเวลา
    
    SOS:
    - ... --- ... (สามจุด, สามขีด, สามจุด)
    - สัญญาณขอความช่วยเหลือสากล
    - เลือกเพราะจำง่ายและไม่สับสนกับสัญญาณอื่น
    """
    
    print("=" * 60)
    print("Bonus: Morse Code Theory")
    print("=" * 60)
    print("""
📚 History:
- Invented by Samuel F.B. Morse & Alfred Vail (1837)
- Used for Telegraph communication
- Still used in HAM Radio and aviation today

📊 Structure:
- Dit (.): 1 time unit
- Dah (-): 3 time units
- Signal gap: 1 time unit
- Letter gap: 3 time units
- Word gap: 7 time units

🆘 Famous SOS Signal:
... --- ... (three dots, three dashes, three dots)

📻 Audio Characteristics:
- Standard CW tone: 600-800 Hz
- ITU standard dit duration at 12 WPM: 100ms
- Dah is always 3x longer than dit

🎯 CTF Tips:
- Listen for pattern of short/long beeps
- Use online audio decoder for quick solve
- Audacity helps visualize the waveform
    """)


# ============================================================
# Main Execution
# ============================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("📻 THE RADIO OPERATOR'S LAST TRANSMISSION - SOLUTIONS")
    print("=" * 60 + "\n")
    
    # Run all methods
    flag1 = method1_manual()
    print("\n")
    
    flag2 = method2_script()
    print("\n")
    
    flag3 = method3_online()
    print("\n")
    
    method4_audacity()
    print("\n")
    
    bonus_theory()
    
    print("\n" + "=" * 60)
    print("✅ FINAL ANSWER")
    print("=" * 60)
    print(f"\n🚩 Flag: {flag1}")
    print("\n(All methods should produce the same flag)")

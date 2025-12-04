"""
🛥️ The Submarine's Silent Cry - Solution
=========================================

Challenge: Morse Audio / Waveform Analysis
Difficulty: ⭐⭐⭐☆☆ (Medium)

Multiple methods to solve this challenge:
1. Visual pattern analysis
2. Python script (automated decoding)
3. Online tools
4. Audio software analysis
"""

import hashlib


# ============================================================
# Method 1: Visual Pattern Analysis (วิเคราะห์รูปแบบด้วยตา)
# ============================================================

def method1_visual():
    """
    วิธีที่ 1: วิเคราะห์รูปแบบ waveform ด้วยตา
    
    ขั้นตอน:
    1. ดูไฟล์ waveform_analysis.txt
    2. สังเกตรูปแบบ:
       - ▄ = สั้น = จุด (.)
       - ▄▄▄ = ยาว = ขีด (-)
       - | | = แยกคำ
       
    3. แปลงเป็น morse code:
       ▄ ▄ ▄ = ...
       ▄ ▄▄▄ = .-
       ▄ ▄ ▄ ▄▄▄ = ...-
       ▄ = .
       (และต่อไป...)
       
    4. ถอดรหัส morse:
       ... = S
       .- = A
       ...- = V
       . = E
       - = T
       .... = H
       . = E
       ... = S
       ..- = U
       -... = B
       -- = M
       .- = A
       .-. = R
       .. = I
       -. = N
       . = E
       
    5. ข้อความ: SAVE THE SUBMARINE
    """
    
    print("=" * 60)
    print("Method 1: Visual Pattern Analysis")
    print("=" * 60)
    
    print("""
Waveform Pattern:
▄ ▄ ▄   ▄ ▄▄▄   ▄ ▄ ▄ ▄▄▄   ▄   |  ▄▄▄   ▄ ▄ ▄ ▄   ▄  |  ...

Conversion:
▄ = . (dit/short)
▄▄▄ = - (dah/long)

Morse Code: ... .- ...- .   - .... .   ... ..- -... -- .- .-. .. -. .

Decoded by letter:
... = S
.- = A  
...- = V
. = E
(space)
- = T
.... = H
. = E
(space)
... = S
..- = U
-... = B
-- = M
.- = A
.-. = R
.. = I
-. = N
. = E

Message: SAVE THE SUBMARINE
    """)
    
    keyword = "SUBMARINE"
    flag_hash = hashlib.md5(keyword.encode()).hexdigest()
    print(f"\nKeyword: {keyword}")
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
    
    def waveform_to_morse(waveform):
        """Convert waveform symbols to morse code"""
        # Replace visual symbols with standard morse
        morse = waveform.replace('▄▄▄', '-').replace('▄', '.')
        # Clean up spacing
        morse = morse.replace('|', '').strip()
        return morse
    
    def decode_morse(morse_code):
        """Decode Morse code to text"""
        words = morse_code.strip().split('   ')
        decoded_message = []
        
        for word in words:
            letters = word.split(' ')
            decoded_word = ''
            for letter in letters:
                letter = letter.strip()
                if letter in MORSE_CODE_DICT:
                    decoded_word += MORSE_CODE_DICT[letter]
            if decoded_word:
                decoded_message.append(decoded_word)
        
        return ' '.join(decoded_message)
    
    # Standard morse from the challenge
    morse_code = "... .- ...- .   - .... .   ... ..- -... -- .- .-. .. -. ."
    
    print("=" * 60)
    print("Method 2: Python Script (Automated)")
    print("=" * 60)
    
    decoded = decode_morse(morse_code)
    print(f"\nInput Morse: {morse_code}")
    print(f"Decoded: {decoded}")
    
    # Generate flag
    keyword = "SUBMARINE"
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
    
    3. CyberChef (Multi-purpose):
       - https://gchq.github.io/CyberChef/
       - ใช้ "From Morse Code" operation
    
    4. dCode:
       - https://www.dcode.fr/morse-code
       - รองรับหลายรูปแบบ input
    """
    
    print("=" * 60)
    print("Method 3: Online Tools")
    print("=" * 60)
    print("""
Recommended Online Tools:

1. 🌐 CyberChef (RECOMMENDED for this challenge):
   URL: https://gchq.github.io/CyberChef/
   Operation: "From Morse Code"
   - Paste: ... .- ...- .   - .... .   ... ..- -... -- .- .-. .. -. .
   - Get decoded text

2. 🌐 Morse Code Audio Decoder:
   URL: https://morsecode.world/international/decoder/audio-decoder-adaptive.html
   - Upload emergency_signal.wav
   - Auto-decode

3. 🌐 dCode Morse Decoder:
   URL: https://www.dcode.fr/morse-code
   - Paste morse code
   - Get decoded message

Steps:
1. Copy morse code from waveform_analysis.txt
2. Go to CyberChef or dCode
3. Decode: SAVE THE SUBMARINE
4. Create flag from keyword: SUBMARINE
    """)
    
    keyword = "SUBMARINE"
    flag_hash = hashlib.md5(keyword.encode()).hexdigest()
    print(f"\nFlag: flag{{{flag_hash}}}")
    
    return f"flag{{{flag_hash}}}"


# ============================================================
# Method 4: Waveform to Morse Converter
# ============================================================

def method4_waveform_converter():
    """
    วิธีที่ 4: เขียน script แปลง waveform เป็น morse
    """
    
    def convert_visual_to_morse(visual):
        """Convert visual waveform to standard morse notation"""
        # Replace visual symbols
        result = visual
        result = result.replace('▄▄▄', '-')
        result = result.replace('▄', '.')
        result = result.replace('|', ' ')
        
        # Clean up multiple spaces
        while '    ' in result:
            result = result.replace('    ', '   ')
        
        return result.strip()
    
    # Waveform from the challenge
    waveform = "▄ ▄ ▄   ▄ ▄▄▄   ▄ ▄ ▄ ▄▄▄   ▄       |     |       ▄▄▄   ▄ ▄ ▄ ▄   ▄       |     |       ▄ ▄ ▄   ▄ ▄ ▄▄▄   ▄▄▄ ▄ ▄ ▄   ▄▄▄ ▄▄▄   ▄ ▄▄▄   ▄ ▄▄▄ ▄   ▄ ▄   ▄▄▄ ▄   ▄"
    
    print("=" * 60)
    print("Method 4: Waveform to Morse Converter")
    print("=" * 60)
    
    morse = convert_visual_to_morse(waveform)
    print(f"\nOriginal Waveform:\n{waveform}")
    print(f"\nConverted to Morse:\n{morse}")
    
    # Manual decode guide
    print("""
Standard Morse Reference:
... .- ...- .   - .... .   ... ..- -... -- .- .-. .. -. .

Decode:
S-A-V-E (space) T-H-E (space) S-U-B-M-A-R-I-N-E

Message: SAVE THE SUBMARINE
    """)
    
    keyword = "SUBMARINE"
    flag_hash = hashlib.md5(keyword.encode()).hexdigest()
    print(f"\nFlag: flag{{{flag_hash}}}")
    
    return f"flag{{{flag_hash}}}"


# ============================================================
# Bonus: Audio Analysis with Python
# ============================================================

def bonus_audio_analysis():
    """
    Bonus: วิเคราะห์ไฟล์เสียง morse ด้วย Python
    
    หมายเหตุ: ต้องมีไฟล์ .wav จริงและติดตั้ง library
    pip install scipy numpy
    """
    
    print("=" * 60)
    print("Bonus: Audio Analysis with Python")
    print("=" * 60)
    print("""
Code to analyze real Morse audio files:

```python
import numpy as np
from scipy.io import wavfile

def analyze_morse_audio(filename):
    # Read audio file
    sample_rate, audio_data = wavfile.read(filename)
    
    # Convert to mono if stereo
    if len(audio_data.shape) > 1:
        audio_data = audio_data.mean(axis=1)
    
    # Detect signal envelope
    envelope = np.abs(audio_data)
    
    # Threshold to find pulses
    threshold = envelope.max() * 0.5
    is_signal = envelope > threshold
    
    # Find transitions
    transitions = np.diff(is_signal.astype(int))
    starts = np.where(transitions == 1)[0]
    ends = np.where(transitions == -1)[0]
    
    # Calculate durations
    if len(starts) > 0 and len(ends) > 0:
        # Ensure matching pairs
        if starts[0] > ends[0]:
            ends = ends[1:]
        if len(starts) > len(ends):
            starts = starts[:len(ends)]
        
        durations = (ends - starts) / sample_rate * 1000  # ms
        
        # Classify as dit or dah
        avg_duration = durations.mean()
        morse = ''
        for d in durations:
            if d < avg_duration:
                morse += '.'
            else:
                morse += '-'
            morse += ' '
        
        return morse
    
    return "No signal detected"

# Usage:
# morse = analyze_morse_audio('emergency_signal.wav')
# print(morse)
```

Tools recommended for audio analysis:
1. Audacity (visual waveform + spectrogram)
2. Sonic Visualiser (advanced analysis)
3. Python scipy/numpy (automated processing)
    """)


# ============================================================
# Bonus: Theory
# ============================================================

def bonus_theory():
    """
    Bonus: ทฤษฎีเพิ่มเติมเกี่ยวกับ Morse Audio
    """
    
    print("=" * 60)
    print("Bonus: Morse Audio Theory")
    print("=" * 60)
    print("""
📊 Waveform Analysis Basics:
============================

1. TIME DOMAIN
   - X-axis: Time (seconds/milliseconds)
   - Y-axis: Amplitude (signal strength)
   - Short pulse → Dit (.)
   - Long pulse → Dah (-)
   
2. FREQUENCY DOMAIN  
   - Standard CW tone: 600-800 Hz
   - Can use FFT to isolate morse signal
   
3. TIMING STANDARDS (ITU)
   - Dit: 1 unit
   - Dah: 3 units
   - Intra-character gap: 1 unit
   - Inter-character gap: 3 units
   - Inter-word gap: 7 units

🔊 Audio File Analysis:
======================
1. Load in Audacity/other software
2. View waveform (zoom in)
3. Look for pulse patterns
4. Measure durations
5. Convert to dots/dashes

🛥️ Naval Communication History:
================================
- Morse code used for maritime communication since 1840s
- SOS became international distress signal in 1906
- Still used in emergency beacons today
- Submarines use low-frequency transmitters

🎯 CTF Tips:
============
- Look for visual patterns in waveforms
- Use online decoders for quick results
- Verify by manual decoding
- Check for multiple encoding layers
    """)


# ============================================================
# Main Execution
# ============================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("🛥️ THE SUBMARINE'S SILENT CRY - SOLUTIONS")
    print("=" * 60 + "\n")
    
    # Run all methods
    flag1 = method1_visual()
    print("\n")
    
    flag2 = method2_script()
    print("\n")
    
    flag3 = method3_online()
    print("\n")
    
    method4_waveform_converter()
    print("\n")
    
    bonus_audio_analysis()
    print("\n")
    
    bonus_theory()
    
    print("\n" + "=" * 60)
    print("✅ FINAL ANSWER")
    print("=" * 60)
    print(f"\n🚩 Flag: {flag1}")
    print("\n(All methods should produce the same flag)")

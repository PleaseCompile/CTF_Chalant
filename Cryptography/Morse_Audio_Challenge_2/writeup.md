# 🛥️ The Submarine's Silent Cry - Writeup

## 📚 พื้นฐานที่ต้องรู้ (Background Knowledge)

### Waveform Analysis คืออะไร?

**Waveform** คือการแสดงผลของสัญญาณเสียงในรูปแบบกราฟ:
- แกน X = เวลา
- แกน Y = ความแรงของสัญญาณ (amplitude)

ในโจทย์นี้ waveform ถูกแปลงเป็นรูปแบบข้อความ:
- `▄` = สัญญาณสั้น (pulse สั้น)
- `▄▄▄` = สัญญาณยาว (pulse ยาว)

### ความเชื่อมโยงกับ Morse Code

เมื่อเห็นรูปแบบ "สั้น" และ "ยาว" สลับกัน ให้นึกถึง:
- **Morse Code** - ระบบ encoding ที่ใช้ dit (.) และ dah (-)
- **CW (Continuous Wave)** - การส่ง Morse ผ่านคลื่นวิทยุ

### Clues จาก Story

1. **"เสียง Titanic"** → SOS signal → Morse Code
2. **"สั้น-ยาว สลับกัน"** → Dit-Dah pattern
3. **"สมัย telegraph"** → Morse system
4. **"CW"** → Continuous Wave = Morse

---

## 🔍 วิธีแก้โจทย์ทีละขั้นตอน

### ขั้นตอนที่ 1: วิเคราะห์ไฟล์ข้อมูล

เปิดไฟล์ `waveform_analysis.txt`:

```
Pattern Key:
▄ = Short pulse (~100ms) 
▄▄▄ = Long pulse (~300ms)

CORRECTED WAVEFORM DATA:
▄ ▄ ▄   ▄ ▄▄▄   ▄ ▄ ▄ ▄▄▄   ▄   |  ▄▄▄   ▄ ▄ ▄ ▄   ▄  |  ▄ ▄ ▄   ▄ ▄ ▄▄▄   ▄▄▄ ▄ ▄ ▄   ▄▄▄ ▄▄▄   ▄ ▄▄▄   ▄ ▄▄▄ ▄   ▄ ▄   ▄▄▄ ▄   ▄

STANDARD NOTATION:
... .- ...- .   - .... .   ... ..- -... -- .- .-. .. -. .
```

### ขั้นตอนที่ 2: แปลง Waveform เป็น Morse

| Waveform | Morse | ตัวอักษร |
|----------|-------|---------|
| ▄ ▄ ▄ | ... | S |
| ▄ ▄▄▄ | .- | A |
| ▄ ▄ ▄ ▄▄▄ | ...- | V |
| ▄ | . | E |
| [word break] | | (space) |
| ▄▄▄ | - | T |
| ▄ ▄ ▄ ▄ | .... | H |
| ▄ | . | E |
| [word break] | | (space) |
| ▄ ▄ ▄ | ... | S |
| ▄ ▄ ▄▄▄ | ..- | U |
| ▄▄▄ ▄ ▄ ▄ | -... | B |
| ▄▄▄ ▄▄▄ | -- | M |
| ▄ ▄▄▄ | .- | A |
| ▄ ▄▄▄ ▄ | .-. | R |
| ▄ ▄ | .. | I |
| ▄▄▄ ▄ | -. | N |
| ▄ | . | E |

### ขั้นตอนที่ 3: รวมเป็นข้อความ

```
S-A-V-E  T-H-E  S-U-B-M-A-R-I-N-E
```

**ข้อความ:** `SAVE THE SUBMARINE`

### ขั้นตอนที่ 4: สร้าง Flag

Keyword จากข้อความ: `SUBMARINE`

```python
import hashlib
keyword = "SUBMARINE"
flag_hash = hashlib.md5(keyword.encode()).hexdigest()
# ผลลัพธ์: 837c37407b42beedaebb7a83e94207d4
```

**🚩 Flag:** `flag{837c37407b42beedaebb7a83e94207d4}`

---

## 💻 วิธีแก้หลายแบบ

### วิธีที่ 1: Visual Analysis

```
1. อ่าน waveform_analysis.txt
2. แปลง ▄ → . และ ▄▄▄ → -
3. ใช้ตาราง Morse decode
4. ได้: SAVE THE SUBMARINE
```

### วิธีที่ 2: Python Script

```python
MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z'
}

morse = "... .- ...- .   - .... .   ... ..- -... -- .- .-. .. -. ."
words = morse.split('   ')
result = []
for word in words:
    letters = word.split(' ')
    decoded = ''.join([MORSE_CODE_DICT.get(l, '') for l in letters])
    result.append(decoded)
print(' '.join(result))
# Output: SAVE THE SUBMARINE
```

### วิธีที่ 3: CyberChef

1. ไปที่ https://gchq.github.io/CyberChef/
2. เลือก operation: "From Morse Code"
3. Paste: `... .- ...- .   - .... .   ... ..- -... -- .- .-. .. -. .`
4. ผลลัพธ์: `SAVE THE SUBMARINE`

### วิธีที่ 4: Online Morse Decoder

1. ไปที่ https://www.dcode.fr/morse-code
2. Paste morse code
3. Click "Decrypt"
4. อ่านผลลัพธ์

---

## 🎓 สิ่งที่ได้เรียนรู้

### 1. Waveform Analysis
- การอ่านและวิเคราะห์ visual representation ของเสียง
- การแปลง waveform เป็นข้อมูลที่ใช้งานได้

### 2. Pattern Recognition
- การระบุรูปแบบซ้ำๆ ในข้อมูล
- การเชื่อมโยง visual pattern กับ encoding system

### 3. Multi-format Data
- ข้อมูลเดียวกันสามารถแสดงได้หลายรูปแบบ:
  - Audio (เสียง)
  - Waveform (กราฟ)
  - Text (▄ และ ▄▄▄)
  - Standard notation (. และ -)

---

## 🔐 Key Takeaways

| หัวข้อ | สิ่งที่เรียนรู้ |
|-------|---------------|
| Waveform | การแปลงเสียงเป็น visual |
| Pattern | Short/Long → Dit/Dah → Morse |
| Tools | CyberChef, dCode, Audacity |
| Analysis | Multiple representations of data |

---

## 📚 Further Learning

### เครื่องมือที่ควรรู้จัก

1. **Audacity** - Open-source audio editor
   - https://www.audacityteam.org/
   - ใช้ดู waveform, spectrogram

2. **Sonic Visualiser** - Advanced audio analysis
   - https://www.sonicvisualiser.org/
   - มี plugins สำหรับ analysis

3. **CyberChef** - Swiss Army knife for data
   - https://gchq.github.io/CyberChef/
   - รองรับหลายรูปแบบ encoding

### โจทย์ที่เกี่ยวข้อง

1. **Spectrogram Steganography** - ซ่อนข้อมูลใน frequency domain
2. **SSTV Decoding** - Slow Scan Television images
3. **DTMF Analysis** - Dual-Tone Multi-Frequency (เสียงโทรศัพท์)

---

## 🆚 เปรียบเทียบกับ Challenge 1

| Feature | Challenge 1 | Challenge 2 |
|---------|-------------|-------------|
| ชื่อ | Radio Operator's Last Transmission | Submarine's Silent Cry |
| Theme | WW2 Radio | Modern Navy |
| Data | Text morse | Visual waveform |
| Approach | ฟังเสียง | ดู pattern |
| Message | THE SECRET MESSAGE... | SAVE THE SUBMARINE |
| Difficulty | ⭐⭐ | ⭐⭐⭐ |

---

## 🚩 Final Flag

```
flag{837c37407b42beedaebb7a83e94207d4}
```

---

## 💡 Tips สำหรับโจทย์ลักษณะนี้

1. **อ่าน hints ให้ละเอียด** - มักจะมี keywords ที่บอกใบ้
2. **มองหา pattern** - Short/Long, High/Low, Fast/Slow
3. **ลอง common encodings ก่อน** - Morse, Binary, Base64
4. **ใช้เครื่องมือออนไลน์** - ประหยัดเวลา
5. **จด notes** - Pattern ที่เห็น, การแปลงที่ลอง

# 📻 The Radio Operator's Last Transmission - Writeup

## 📚 พื้นฐานที่ต้องรู้ (Background Knowledge)

### Morse Code คืออะไร?

**Morse Code** คือระบบการเข้ารหัสตัวอักษรและตัวเลขโดยใช้สัญญาณสองประเภท:
- **จุด (Dit/Dot)**: `.` - สัญญาณสั้น
- **ขีด (Dah/Dash)**: `-` - สัญญาณยาว

ระบบนี้คิดค้นโดย **Samuel F.B. Morse** และ **Alfred Vail** ในปี ค.ศ. 1837 สำหรับใช้กับโทรเลข

### ตัวอย่าง Morse Code พื้นฐาน

| ตัวอักษร | Morse | ตัวอักษร | Morse |
|---------|-------|---------|-------|
| A | .- | N | -. |
| B | -... | O | --- |
| C | -.-. | P | .--. |
| D | -.. | Q | --.- |
| E | . | R | .-. |
| F | ..-. | S | ... |
| G | --. | T | - |
| H | .... | U | ..- |
| I | .. | V | ...- |
| J | .--- | W | .-- |
| K | -.- | X | -..- |
| L | .-.. | Y | -.-- |
| M | -- | Z | --.. |

### Morse Audio

**Morse Audio** คือ Morse Code ที่ส่งในรูปแบบเสียง:
- **เสียงสั้น (Beep สั้น)** = จุด (.)
- **เสียงยาว (Beep ยาว)** = ขีด (-)
- **ช่องเงียบสั้น** = ระหว่างตัวอักษร
- **ช่องเงียบยาว** = ระหว่างคำ

ความถี่เสียงมาตรฐาน: **600-800 Hz** (เสียงแหลม)

---

## 🔍 วิธีแก้โจทย์ทีละขั้นตอน

### ขั้นตอนที่ 1: ระบุประเภทของโจทย์

เมื่ออ่านโจทย์และ hint จะพบว่า:
- มีไฟล์เสียงที่มี "เสียงยาว-สั้น สลับกัน"
- Hint กล่าวถึง "จุดและขีด", "HAM Radio", "SOS"
- มีการอ้างถึง Samuel Morse

**สรุป:** นี่คือ **Morse Code Audio Challenge**

### ขั้นตอนที่ 2: วิเคราะห์ไฟล์เสียง

**ตัวเลือกที่ 1: ใช้เครื่องมือออนไลน์**
1. ไปที่ https://morsecode.world/international/decoder/audio-decoder-adaptive.html
2. อัพโหลดไฟล์ `transmission.wav`
3. รอให้ระบบถอดรหัส

**ตัวเลือกที่ 2: ใช้ Audacity**
1. เปิดไฟล์ใน Audacity
2. ดู waveform และจดรูปแบบ
3. แยกแยะ dit (สั้น) และ dah (ยาว)

**ตัวเลือกที่ 3: ฟังและจดด้วยมือ**
1. เปิดไฟล์เสียง
2. จดเมื่อได้ยินเสียงสั้น (.) หรือยาว (-)

### ขั้นตอนที่ 3: แปลง Morse เป็นข้อความ

จากไฟล์ `morse_data.txt`:

```
- .... .   ... . -.-. .-. . -   -- . ... ... .- --. .   .. ...   -.. --- - ...   .- -. -..   -.. .- ... .... . ...
```

แยกเป็นคำๆ (คำแยกด้วย 3 ช่องว่าง):

| Morse | ตัวอักษร |
|-------|---------|
| - | T |
| .... | H |
| . | E |
| (space) | (word break) |
| ... | S |
| . | E |
| -.-. | C |
| .-. | R |
| . | E |
| - | T |
| (space) | (word break) |
| -- | M |
| . | E |
| ... | S |
| ... | S |
| .- | A |
| --. | G |
| . | E |
| (space) | (word break) |
| .. | I |
| ... | S |
| (space) | (word break) |
| -.. | D |
| --- | O |
| - | T |
| ... | S |
| (space) | (word break) |
| .- | A |
| -. | N |
| -.. | D |
| (space) | (word break) |
| -.. | D |
| .- | A |
| ... | S |
| .... | H |
| . | E |
| ... | S |

**ข้อความที่ได้:** `THE SECRET MESSAGE IS DOTS AND DASHES`

### ขั้นตอนที่ 4: สร้าง Flag

จากข้อความ keyword คือ: `DOTS_AND_DASHES`

สร้าง MD5 hash:
```python
import hashlib
keyword = "DOTS_AND_DASHES"
flag_hash = hashlib.md5(keyword.encode()).hexdigest()
# ผลลัพธ์: 12e5c91b04d63ae4e6252e299d7a0122
```

**🚩 Flag:** `flag{12e5c91b04d63ae4e6252e299d7a0122}`

---

## 💻 วิธีแก้หลายแบบ

### วิธีที่ 1: Manual Decode

```
1. ฟังเสียงและจดรูปแบบ
2. ใช้ตาราง Morse Code แปลงทีละตัวอักษร
3. ได้ข้อความ: THE SECRET MESSAGE IS DOTS AND DASHES
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

morse_code = "- .... .   ... . -.-. .-. . -   -- . ... ... .- --. .   .. ...   -.. --- - ...   .- -. -..   -.. .- ... .... . ..."

words = morse_code.split('   ')
decoded = []
for word in words:
    letters = word.split(' ')
    decoded_word = ''.join([MORSE_CODE_DICT.get(l, '') for l in letters])
    decoded.append(decoded_word)
    
print(' '.join(decoded))
# Output: THE SECRET MESSAGE IS DOTS AND DASHES
```

### วิธีที่ 3: Online Tools

1. **morsecode.world** - Audio Decoder
   - URL: https://morsecode.world/international/decoder/audio-decoder-adaptive.html
   - อัพโหลด .wav file แล้วจะถอดรหัสอัตโนมัติ

2. **dCode.fr**
   - URL: https://www.dcode.fr/morse-code
   - รองรับทั้ง text และ audio

---

## 🎓 สิ่งที่ได้เรียนรู้

1. **Morse Code Fundamentals**
   - โครงสร้าง dit และ dah
   - การแยกตัวอักษรและคำ

2. **Audio Analysis**
   - การวิเคราะห์ไฟล์เสียง
   - การใช้ Audacity หรือเครื่องมืออื่น

3. **Pattern Recognition**
   - การระบุรูปแบบจาก hints
   - การเชื่อมโยง clues เข้าด้วยกัน

---

## 🔐 Key Takeaways

| หัวข้อ | สิ่งที่เรียนรู้ |
|-------|---------------|
| Morse Code | ระบบ encoding ด้วย . และ - |
| Audio Analysis | การวิเคราะห์ waveform |
| CTF Skills | การอ่าน hints และระบุประเภทโจทย์ |
| Tools | morsecode.world, Audacity, dCode |

---

## 📚 Further Learning

### แหล่งเรียนรู้เพิ่มเติม

1. **Morse Code Practice**
   - https://lcwo.net/ - Learn CW Online
   - https://morsecode.world/international/trainer/trainer.html

2. **Audio Analysis**
   - Audacity: https://www.audacityteam.org/
   - Sonic Visualiser: https://www.sonicvisualiser.org/

3. **CTF Resources**
   - CTF Wiki: https://ctf-wiki.org/
   - CyberChef: https://gchq.github.io/CyberChef/

### โจทย์ที่คล้ายกัน

- **Spectrogram Analysis** - ซ่อนข้อมูลใน audio spectrum
- **DTMF Decoding** - เสียงปุ่มโทรศัพท์
- **SSTV** - Slow Scan Television images in audio

---

## 🚩 Final Flag

```
flag{12e5c91b04d63ae4e6252e299d7a0122}
```

# 🛥️ The Submarine's Silent Cry

## 🎯 Concept (แนวคิดหลัก)

โจทย์นี้สอนเกี่ยวกับการวิเคราะห์รูปแบบเสียงที่ซ่อนข้อมูลไว้ - ระบบสัญญาณฉุกเฉินที่ใช้มาตั้งแต่ยุคสงครามโลก

---

## 📖 Story (เนื้อเรื่อง)

ทะเลลึกในมหาสมุทรแปซิฟิก ปี 2024...

คุณเป็นนักวิเคราะห์สัญญาณของกองทัพเรือ ในคืนหนึ่งที่อากาศสงบ ระบบตรวจจับของคุณได้รับสัญญาณแปลกประหลาดจากใต้ทะเลลึก

**"เสียงนี้... มันไม่ใช่เสียงปลาวาฬ"** คุณพึมพำกับตัวเอง

สัญญาณมีรูปแบบที่ชัดเจน - **บางครั้งสั้น บางครั้งยาว** - เหมือนมีใครบางคนกำลังพยายามส่งข้อความ

ตามรายงาน เรือดำน้ำ **"USS Phantom"** หายไปในพื้นที่นี้เมื่อ 72 ชั่วโมงก่อน ลูกเรือได้รับการฝึกการสื่อสารฉุกเฉินแบบโบราณ - วิธีที่ใช้กันมาตั้งแต่สมัย **"Titanic"** ขอความช่วยเหลือ

ไฟล์เสียงถูกแปลงเป็น **waveform visualization** เพื่อให้คุณวิเคราะห์ได้ง่ายขึ้น

**"ถ้าเราถอดรหัสนี้ได้... เราอาจช่วยชีวิตพวกเขาได้"**

---

## 💡 Hints (คำใบ้)

### 🇹🇭 ภาษาไทย
1. **Hint 1:** ดูรูปแบบของ waveform ดีๆ - คลื่นบางอันสั้น บางอันยาว ไม่ใช่เรื่องบังเอิญ
2. **Hint 2:** สัญญาณ **"SOS"** ที่เรือ Titanic ส่งก็ใช้ระบบเดียวกันนี้ - สามสั้น สามยาว สามสั้น
3. **Hint 3:** นักวิทยุสมัครเล่นเรียกสัญญาณนี้ว่า **"CW"** (Continuous Wave)
4. **Hint 4:** รูปแบบนี้คิดค้นในยุคที่การสื่อสารใช้สายโทรเลข
5. **Final Hint:** ลองหา **"waveform audio decoder beep pattern"** ดู

### 🇬🇧 English
1. **Hint 1:** Look at the waveform pattern - some waves are short, some are long. It's not random.
2. **Hint 2:** The **"SOS"** signal from Titanic used the same system - three short, three long, three short
3. **Hint 3:** HAM radio operators call this signal **"CW"** (Continuous Wave)
4. **Hint 4:** This system was invented during the telegraph era
5. **Final Hint:** Try searching **"waveform audio decoder beep pattern"**

---

## 📦 Data Files

### ไฟล์ที่ 1: `emergency_signal.wav`
ไฟล์เสียงจากระบบ sonar ความยาว 45 วินาที

### ไฟล์ที่ 2: `waveform_analysis.txt`
การแปลง waveform เป็นรูปแบบข้อความ:

```
Signal Analysis Report
======================
Time: 00:00:00 - 00:00:45
Frequency: 750 Hz
Pattern Detected: YES

Visual Representation:
▄ ▄ ▄   ▄▄▄   ▄ ▄ ▄ ▄   ▄ ▄▄▄   ▄▄▄ ▄▄▄ ▄   ▄▄▄ ▄ ▄   ▄▄▄ ▄▄▄   ▄ ▄ ▄   ...

(▄ = short pulse, ▄▄▄ = long pulse)
```

---

## 🎮 Challenge

1. วิเคราะห์ไฟล์ `waveform_analysis.txt` หรือฟังไฟล์ `emergency_signal.wav`
2. ระบุรูปแบบของสัญญาณ (สั้น/ยาว)
3. หาวิธีถอดรหัสที่เหมาะสม
4. แปลงสัญญาณเป็นข้อความ
5. หา flag จากข้อความที่ได้

---

## 🚩 Flag Format

```
flag{md5_hash}
```

---

## 📊 Difficulty

⭐⭐⭐☆☆ (Medium)

**Skills Required:**
- การวิเคราะห์ pattern
- ความเข้าใจเรื่องการ encoding
- การใช้เครื่องมือถอดรหัส

---

## 🆚 ความแตกต่างจาก Challenge 1

| Feature | Challenge 1 | Challenge 2 |
|---------|-------------|-------------|
| Theme | สงครามโลก WW2 | เรือดำน้ำสมัยใหม่ |
| Data Format | Text-based morse | Visual waveform |
| Approach | ฟังเสียง → ถอดรหัส | ดูรูปแบบ → วิเคราะห์ |
| Difficulty | Easy-Medium | Medium |
| Learning | Morse basics | Waveform analysis |

---

## 🎓 Learning Objectives

หลังจากทำโจทย์นี้สำเร็จ คุณจะเข้าใจ:
1. การวิเคราะห์ waveform และ signal patterns
2. ความสัมพันธ์ระหว่างเสียงและข้อมูล
3. การใช้เครื่องมือ visualize สัญญาณ
4. ประยุกต์ใช้ knowledge จากโจทย์ก่อนหน้า

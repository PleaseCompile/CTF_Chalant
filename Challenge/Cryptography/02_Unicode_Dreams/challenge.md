# 🌈 Unicode Dreams (HARD MODE)

## ⚠️ Difficulty: ⭐⭐⭐⭐ (Hard)

## 🎯 Concept (ไทย)
ศึกษาการแปลงตัวอักษร Unicode ให้กลายเป็นรูปแบบที่ระบบคอมพิวเตอร์รุ่นเก่าสามารถอ่านได้ **พร้อมกับการซ่อนข้อมูลเพิ่มเติมอีกชั้น**

## 📖 Story (ไทย)

คุณได้รับอีเมลลึกลับจากเพื่อนที่อยู่ต่างประเทศ...

> "เฮ้!
>
> ฉันกำลังทำโปรเจกต์เกี่ยวกับการส่งข้อความข้ามภาษา แต่เจอปัญหาแปลกๆ...
>
> เวลาฉันส่งข้อความที่มีตัวอักษรพิเศษไปให้ระบบเก่าๆ มันจะแปลงข้อความให้กลายเป็นรหัสแปลกๆ!
>
> ระบบมันบอกว่าเป็น 'Bootstring encoding' อะไรสักอย่าง... 
>
> แต่เดี๋ยวก่อน! ระบบได้อัปเดตความปลอดภัยใหม่ มันครอบข้อมูลด้วยอีกชั้นหนึ่ง...
> ดูเหมือนจะเป็นการเข้ารหัสที่ใช้ตัวอักษร 64 ตัว...
>
> ฉันได้ยินมาว่าการเข้ารหัสแบบนี้ถูกใช้ตอนที่อินเทอร์เน็ตต้องการให้ตัวอักษรจากทุกประเทศทำงานด้วยกันได้
> เหมือนเป็นการสร้าง 'สะพาน' ระหว่างโลก Unicode และโลก ASCII
>
> ช่วยถอดรหัสข้อความเหล่านี้ให้ที! **ระวัง มีการเข้ารหัส 2 ชั้น!** ข้อความสุดท้ายคือความลับสำคัญ!"

## 💡 Hints

### 🇹🇭 Hint ภาษาไทย
1. การเข้ารหัสนี้เป็นส่วนหนึ่งของ IDNA (Internationalized Domain Names in Applications)
2. ลองค้นหาเกี่ยวกับ "Unicode to ASCII conversion for internet protocols"
3. **สังเกตดีๆ ข้อมูลถูกห่อด้วยการเข้ารหัสอีกชั้น** - มันใช้ตัวอักษร A-Z, a-z, 0-9 และ = 
4. RFC 3492 คือกุญแจสำคัญในการไขรหัสชั้นใน
5. **ต้อง decode 2 ครั้ง!** - ชั้นนอกก่อน แล้วค่อยชั้นใน

### 🇬🇧 Hint in English
1. This encoding is part of the IDNA specification
2. Search for "Unicode to ASCII compatible encoding"
3. **Look carefully - data is wrapped with another encoding layer** - it uses A-Z, a-z, 0-9 and =
4. The Bootstring algorithm transforms unicode into something machines can understand
5. **You need to decode TWICE!** - outer layer first, then inner layer

## 📦 Data

ไฟล์ที่ต้องใช้: `data.txt`

## 🎮 Challenge

ถอดรหัสข้อความทั้งหมดจากไฟล์ `data.txt` เพื่อค้นหา flag ที่ซ่อนอยู่ในข้อความสุดท้าย
**ระวัง: มีการเข้ารหัส 2 ชั้น!**

## 🚩 Flag Format

```
flag{md5_hash}
```

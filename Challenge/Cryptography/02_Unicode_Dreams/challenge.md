# 🌈 Unicode Dreams

## 🎯 Concept (ไทย)
ศึกษาการแปลงตัวอักษร Unicode ให้กลายเป็นรูปแบบที่ระบบคอมพิวเตอร์รุ่นเก่าสามารถอ่านได้

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
> ฉันได้ยินมาว่าการเข้ารหัสแบบนี้ถูกใช้ตอนที่อินเทอร์เน็ตต้องการให้ตัวอักษรจากทุกประเทศทำงานด้วยกันได้
> เหมือนเป็นการสร้าง 'สะพาน' ระหว่างโลก Unicode และโลก ASCII
>
> ช่วยถอดรหัสข้อความเหล่านี้ให้ที! ข้อความสุดท้ายคือความลับสำคัญ!"

## 💡 Hints

### 🇹🇭 Hint ภาษาไทย
1. การเข้ารหัสนี้เป็นส่วนหนึ่งของ IDNA (Internationalized Domain Names in Applications)
2. ลองค้นหาเกี่ยวกับ "Unicode to ASCII conversion for internet protocols"
3. ทุกภาษาในโลกสามารถแปลงเป็น ASCII ได้ด้วยวิธีนี้ รวมถึงภาษาไทย!
4. RFC 3492 คือกุญแจสำคัญในการไขรหัสนี้

### 🇬🇧 Hint in English
1. This encoding is part of the IDNA specification
2. Search for "Unicode to ASCII compatible encoding"
3. Every language in the world can be converted to ASCII using this method
4. The Bootstring algorithm transforms unicode into something machines can understand

## 📦 Data

ไฟล์ที่ต้องใช้: `data.txt`

## 🎮 Challenge

ถอดรหัสข้อความทั้งหมดจากไฟล์ `data.txt` เพื่อค้นหา flag ที่ซ่อนอยู่ในข้อความสุดท้าย

## 🚩 Flag Format

```
flag{md5_hash}
```

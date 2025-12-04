# 🌐 The Mysterious Domain

## 🎯 Concept (ไทย)
ศึกษาวิธีการแปลงชื่อโดเมนที่มีตัวอักษรพิเศษให้กลายเป็น ASCII ที่คอมพิวเตอร์อ่านได้

## 📖 Story (ไทย)

ในห้องทำงานของนักสืบไซเบอร์ จู่ๆ ก็มีอีเมลลึกลับส่งเข้ามา...

> "ถึงนักสืบ,
>
> ฉันพบเบาะแสสำคัญเกี่ยวกับองค์กรลับ พวกเขาใช้ที่อยู่เว็บไซต์แปลกๆ ที่ดูเหมือนจะไม่ใช่ภาษาปกติ...
>
> ฉันสังเกตว่าทุกครั้งที่พวกเขาส่งลิงก์ให้กัน มันจะขึ้นต้นด้วยตัวอักษรแปลกๆ ราวกับว่าเป็นรหัสลับ
> 
> ลิงก์เหล่านี้ดูเหมือนจะเป็น domain name แต่ทำไมมันถึงขึ้นต้นด้วย `xn--` ล่ะ?
> ฉันได้ยินมาว่าวิธีนี้ถูกใช้เพื่อทำให้ตัวอักษร 'สากล' กลายเป็น 'ASCII' ที่ระบบ DNS อ่านได้
>
> ช่วยถอดรหัสนี้ให้ที!"

## 💡 Hints

### 🇹🇭 Hint ภาษาไทย
1. ลองสังเกต prefix `xn--` มันเป็นตัวบ่งบอกมาตรฐานการเข้ารหัสบางอย่าง
2. การเข้ารหัสนี้ถูกออกแบบมาเพื่อให้ internationalized domain names (IDN) ทำงานได้บน DNS
3. ลองค้นหาเกี่ยวกับ "ASCII Compatible Encoding" หรือ "Bootstring algorithm"
4. RFC 3492 อาจให้คำตอบที่คุณต้องการ...

### 🇬🇧 Hint in English
1. Notice the `xn--` prefix? It's an ACE prefix that indicates a specific encoding standard
2. This encoding was designed to make non-ASCII domain names work with DNS
3. Try searching for "internationalized domain names encoding" or "Bootstring"
4. The answer lies in how the internet handles unicode in URLs...

## 📦 Data

ไฟล์ที่ต้องใช้: `data.txt`

## 🎮 Challenge

ถอดรหัสข้อความจากไฟล์ `data.txt` เพื่อค้นหา flag ที่ซ่อนอยู่

## 🚩 Flag Format

```
flag{md5_hash}
```

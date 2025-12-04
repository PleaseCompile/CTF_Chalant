# 👯 The Twins' Treasure

## 🎯 Concept (ไทย)
การเข้ารหัสที่ใช้การยกกำลังกับตัวเลขขนาดใหญ่ แต่ถ้าเลขชี้กำลังน้อยเกินไป ความลับอาจรั่วไหลได้ง่ายๆ

## 📖 Story (ไทย)
> ฝาแฝดคู่หนึ่งค้นพบสมบัติโบราณ แต่พ่อของพวกเขาได้ซ่อนรหัสผ่านไว้ก่อนจากไป
>
> พ่อบอกว่า "ข้าใช้ตัวเลขที่คูณกันได้ผลลัพธ์มหาศาล แล้วยกกำลังด้วยเลขเล็กๆ แค่ 3"
>
> "เลข 3 มันเป็นเลขมงคล" พ่อพูดพร้อมยิ้ม "แต่ถ้าข้อความสั้นเกินไป และไม่ได้เติมอะไรเพิ่ม... บางทีก็แค่ถอดรากที่สามก็ได้"
>
> ฝาแฝดจ้องมองกันด้วยความงุนงง แต่ลึกๆ พวกเขารู้ว่าพ่อกำลังใบ้ทางให้...

## 📖 Story (English)
> Twin siblings discovered an ancient treasure, but their father hid the password before he passed away.
>
> Father said: "I used numbers that multiply to something enormous, then raised it to the power of just 3."
>
> "Three is a lucky number," Father smiled. "But if the message is too short, and nothing extra is added... sometimes just taking the cube root is enough."
>
> The twins stared at each other in confusion, but deep down they knew their father was giving them a hint...

## 💡 Hints

### ระดับที่ 1 (Easy)
- 🇹🇭 **ไทย**: "ยกกำลัง 3" และ "ถอดราก" - ถ้า c = m³ แล้ว m จะหาได้อย่างไร?
- 🇬🇧 **English**: "Raised to the power of 3" and "taking the root" - if c = m³, how do you find m?

### ระดับที่ 2 (Medium)
- 🇹🇭 **ไทย**: ในการเข้ารหัสแบบนี้ ถ้า e=3 และ m³ < n แล้ว c = m³ โดยไม่มี mod!
- 🇬🇧 **English**: In this encryption, if e=3 and m³ < n, then c = m³ without any mod!

### ระดับที่ 3 (Hard)
- 🇹🇭 **ไทย**: ใช้ Python: `int(c ** (1/3))` หรือ `gmpy2.iroot(c, 3)` เพื่อถอดรากที่ 3
- 🇬🇧 **English**: Use Python: `int(c ** (1/3))` or `gmpy2.iroot(c, 3)` for cube root

## 📦 Data

ไฟล์: `data.txt`

สิ่งที่ฝาแฝดพบในหีบสมบัติ:
- `n` = ผลคูณของตัวเลขพิเศษ 2 ตัว (ใหญ่มาก)
- `e` = เลขชี้กำลัง (เลขมงคล)
- `c` = ข้อความที่ถูกเข้ารหัส

พ่อทิ้งโน้ตไว้: "ข้อความสั้นนัก จนยกกำลังแล้วก็ยังไม่ถึง n"

## 🎮 Challenge

1. สังเกตว่า `e` มีค่าน้อยมาก
2. คิดว่าถ้า m^e < n จะเกิดอะไรขึ้น
3. หาวิธีถอดรหัสโดยไม่ต้องรู้ p และ q

## 🚩 Flag Format
```
flag{...}
```

## 📚 What You'll Learn
- จุดอ่อนของการใช้ e ที่มีค่าน้อย (Small e attack)
- ความสำคัญของ padding ในการเข้ารหัส
- การใช้ cube root ในการโจมตี RSA

---
*"Sometimes, the simplest solution is the right one. When the exponent is small, the math becomes... elementary."*

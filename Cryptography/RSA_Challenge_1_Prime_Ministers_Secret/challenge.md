# 🔐 The Prime Minister's Secret

## 🎯 Concept (ไทย)
การเข้ารหัสที่ใช้หลักการทางคณิตศาสตร์กับตัวเลขพิเศษ - ตัวเลขที่หารลงตัวได้เพียงแค่ 1 และตัวมันเอง

## 📖 Story (ไทย)
> นายกรัฐมนตรีคนหนึ่งเชื่อในพลังของตัวเลข "พิเศษ" มาก เขาบอกว่า "ความลับที่แข็งแกร่งที่สุด คือความลับที่ถูกคูณด้วยตัวเลขที่ไม่มีใครหารได้"
>
> เขาเลือกตัวเลขพิเศษ 2 ตัวที่เขารักมาก แล้วคูณมันเข้าด้วยกันเพื่อสร้าง "กุญแจสาธารณะ"
>
> เขากระซิบกับผู้ช่วยว่า "ถ้าใครรู้ตัวเลข 2 ตัวนี้ พวกเขาจะสามารถ 'กลับ' กระบวนการได้... แต่ไม่มีใครรู้หรอก"
>
> น่าเสียดาย... เขาลืมไปว่าเขาจดไว้ในสมุดบันทึก

## 📖 Story (English)
> A Prime Minister believed deeply in the power of "special" numbers - numbers that can only be divided by 1 and themselves.
>
> He whispered to his assistant: "The strongest secret is one multiplied by numbers no one can divide."
>
> He chose two special numbers he loved, multiplied them together to create his "public key."
>
> "If anyone knows these two numbers, they could 'reverse' the process... but no one will ever know."
>
> Unfortunately... he forgot he wrote them down in his notebook.

## 💡 Hints

### ระดับที่ 1 (Easy)
- 🇹🇭 **ไทย**: ตัวเลข "พิเศษ" ที่หารลงตัวได้แค่ 1 และตัวเอง ในภาษาคณิตศาสตร์เรียกว่าอะไร? และถ้าเรารู้ 2 ตัวที่คูณกัน เราจะ "กลับ" กระบวนการได้อย่างไร?
- 🇬🇧 **English**: What do we call numbers that can only be divided by 1 and themselves? And if we know the two that were multiplied, how can we "reverse" the process?

### ระดับที่ 2 (Medium)
- 🇹🇭 **ไทย**: การเข้ารหัสนี้ตั้งชื่อตามนักคณิตศาสตร์ 3 คน ที่ชื่อขึ้นต้นด้วย R, S, และ A
- 🇬🇧 **English**: This encryption was named after 3 mathematicians whose names start with R, S, and A

### ระดับที่ 3 (Hard)
- 🇹🇭 **ไทย**: `d = inverse(e, φ(n))` และ `φ(n) = (p-1) × (q-1)` - การยกกำลังย้อนกลับ!
- 🇬🇧 **English**: `d = inverse(e, φ(n))` and `φ(n) = (p-1) × (q-1)` - Reverse the exponentiation!

## 📦 Data

ไฟล์: `data.txt`

สิ่งที่คุณพบในสมุดบันทึกของนายกรัฐมนตรี:
- `p` = ตัวเลขพิเศษตัวที่ 1
- `q` = ตัวเลขพิเศษตัวที่ 2  
- `n` = p × q (ผลคูณที่ใช้เป็นกุญแจ)
- `e` = ตัวเลขที่ใช้ยกกำลัง (exponent)
- `c` = ข้อความที่ถูกเข้ารหัสแล้ว

## 🎮 Challenge

1. เข้าใจความสัมพันธ์ของตัวเลขทั้งหมด
2. ค้นหาวิธี "กลับ" กระบวนการเข้ารหัส
3. ถอดรหัสเพื่อหา flag

## 🚩 Flag Format
```
flag{...}
```

## 📚 What You'll Learn
- หลักการของการเข้ารหัสแบบ asymmetric
- ความสำคัญของ prime numbers ในการเข้ารหัส
- การคำนวณ modular inverse

---
*"In the world of cryptography, the beauty of mathematics becomes the guardian of secrets."*

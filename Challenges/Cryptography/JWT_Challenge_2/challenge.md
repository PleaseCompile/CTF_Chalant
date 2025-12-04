# 🎭 The Identity Forge

## 🎯 Concept (Thai)
การปลอมแปลงตัวตนผ่านการแก้ไขข้อมูลที่ส่งผ่านระหว่างระบบ โดยเปลี่ยนบทบาทจากผู้ใช้ธรรมดาเป็นผู้ดูแลระบบ

## 📖 Story (Thai)

> คุณเป็นนักวิจัยด้านความปลอดภัยที่กำลังทดสอบระบบเว็บแห่งหนึ่ง
>
> ขณะวิเคราะห์ traffic คุณพบว่าระบบใช้ "บัตรผ่าน" แบบดิจิทัลที่ประกอบด้วยสามส่วน คั่นด้วยจุด
>
> บัตรผ่านนี้มีข้อมูลระบุตัวตน รวมถึงระดับสิทธิ์ของผู้ใช้
>
> เมื่อตรวจสอบส่วนแรกของบัตรผ่าน คุณพบว่า:
>
> *"ส่วนแรกบอกวิธีการตรวจสอบความถูกต้อง... แต่ถ้าเราบอกว่าไม่ต้องตรวจสอบล่ะ?"*
>
> คุณนึกถึงช่องโหว่เก่าแก่ที่บางระบบยอมรับ "บัตรผ่าน" ที่ไม่มีการลงลายเซ็น
>
> **เป้าหมาย**: แก้ไขบัตรผ่านเพื่อเปลี่ยนสิทธิ์จาก `user` เป็น `admin` และหา flag ที่ซ่อนอยู่

## 💡 Hint

### ภาษาไทย
1. ส่วนแรกของ "บัตรผ่าน" มีข้อมูลเกี่ยวกับ `alg` (algorithm)
2. ลองเปลี่ยนค่า algorithm เป็น "none" - บางระบบยอมรับ!
3. ถ้า algorithm เป็น "none" ส่วนลายเซ็นก็ไม่จำเป็น (เว้นว่างได้)
4. อย่าลืมเปลี่ยน `role` ในส่วนที่สองด้วย

### English
1. The first part of the "pass" contains info about `alg` (algorithm)
2. Try changing the algorithm to "none" - some systems accept it!
3. If algorithm is "none", the signature part is not needed (can be empty)
4. Don't forget to change `role` in the second part

## 📦 Data
ดูไฟล์ `data.txt` - มี token ของ user ปกติ และ server simulation

## 🎮 Challenge
1. วิเคราะห์ token ที่ให้มา
2. แก้ไข token เพื่อเปลี่ยน role เป็น admin
3. ใช้ช่องโหว่ algorithm none
4. ส่ง token ปลอมไปยัง server เพื่อรับ flag

## 🚩 Flag Format
`flag{...}`

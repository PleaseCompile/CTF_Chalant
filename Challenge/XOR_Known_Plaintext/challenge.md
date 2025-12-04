# 🔐 XOR Known Plaintext Attack

## 🎯 Concept (Thai)
การโจมตีแบบ Known Plaintext Attack บน XOR cipher - เมื่อเรารู้ส่วนหนึ่งของข้อความที่ถูกเข้ารหัส เราสามารถหา key ได้!

## 🎯 Concept (English)
Known Plaintext Attack on XOR cipher - when we know part of the encrypted message, we can recover the key!

---

## 📖 Story (Thai)
คุณเป็นนักวิเคราะห์ความปลอดภัยที่ได้รับไฟล์การสื่อสารที่ถูกเข้ารหัส ระบบนี้ใช้โปรโตคอล SECURECOMM v2.1 ซึ่งทุกข้อความจะเริ่มต้นด้วย header มาตรฐาน: `SECURECOMM:v2.1|FROM:`

คุณดักจับได้ข้อความที่เข้ารหัสแล้ว และเนื่องจากคุณรู้ format ของ header คุณอาจหา key และถอดรหัสข้อความทั้งหมดได้!

## 📖 Story (English)
You're a security analyst who received an encrypted communication file. The system uses SECURECOMM v2.1 protocol where every message starts with a standard header: `SECURECOMM:v2.1|FROM:`

You intercepted an encrypted message, and since you know the header format, you might be able to recover the key and decrypt the entire message!

---

## 💡 Hints

### Thai
1. 💡 XOR มีคุณสมบัติพิเศษ: A ⊕ B ⊕ B = A
2. 💡 ถ้า Plaintext ⊕ Key = Ciphertext แล้ว Plaintext ⊕ Ciphertext = ?
3. 💡 Key อาจเป็นคำซ้ำๆ (repeating key)

### English
1. 💡 XOR has a special property: A ⊕ B ⊕ B = A
2. 💡 If Plaintext ⊕ Key = Ciphertext, then Plaintext ⊕ Ciphertext = ?
3. 💡 The key might be a repeating word

---

## 📦 Data

### Intercepted Data
````
Ciphertext (hex): 000000071711100a0e1f7f22616b722e03061c08791301191a0b3f1f161369232f33222f2b2a310d2c270c23363c3828160b07
````

### Known Information
````
Protocol Header: SECURECOMM:v2.1|FROM:
````

---

## 🎮 Challenge

1. ใช้ Known Plaintext (header) เพื่อหา encryption key
2. ถอดรหัสข้อความทั้งหมด
3. หา flag ที่ซ่อนอยู่

---

## 🚩 Flag Format
````
flag{...}
````

---

## 📊 Difficulty
⭐⭐☆☆☆ (Easy-Medium)

## 📚 Category
Cryptography - XOR Cipher - Known Plaintext Attack

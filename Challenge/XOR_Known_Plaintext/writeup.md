# XOR Known Plaintext Attack - Writeup

## 📚 พื้นฐานที่ต้องรู้ (Prerequisites)

### XOR คืออะไร?

XOR (Exclusive OR) เป็นการดำเนินการทางตรรกะที่ให้ผลเป็น 1 เมื่อ input ต่างกัน:

| A | B | A XOR B |
|---|---|---------|
| 0 | 0 |    0    |
| 0 | 1 |    1    |
| 1 | 0 |    1    |
| 1 | 1 |    0    |

### คุณสมบัติสำคัญของ XOR

````python
# 1. Identity: A ⊕ 0 = A
5 ^ 0 = 5

# 2. Self-inverse: A ⊕ A = 0
5 ^ 5 = 0

# 3. Commutative: A ⊕ B = B ⊕ A
5 ^ 3 = 3 ^ 5

# 4. Associative: (A ⊕ B) ⊕ C = A ⊕ (B ⊕ C)
(5 ^ 3) ^ 2 = 5 ^ (3 ^ 2)
````

### XOR Cipher ทำงานอย่างไร?

````
Encryption: Plaintext ⊕ Key = Ciphertext
Decryption: Ciphertext ⊕ Key = Plaintext
````

ถ้า key สั้นกว่า message, key จะถูกใช้ซ้ำ (repeating key):

````
Message:  H  E  L  L  O  W  O  R  L  D
Key:      S  E  C  R  E  T  S  E  C  R  (repeating "SECRET")
Result:   XOR each pair
````

---

## 🔍 Known Plaintext Attack คืออะไร?

### หลักการ

ถ้าเรารู้ส่วนหนึ่งของ plaintext และ ciphertext:

````
Plaintext ⊕ Key = Ciphertext
````

เราสามารถหา Key ได้โดย:

````
Plaintext ⊕ Ciphertext = Plaintext ⊕ (Plaintext ⊕ Key)
                       = (Plaintext ⊕ Plaintext) ⊕ Key
                       = 0 ⊕ Key
                       = Key
````

**สรุป: Plaintext ⊕ Ciphertext = Key**

---

## 🔍 วิธีแก้โจทย์ทีละขั้นตอน

### ข้อมูลที่ได้รับ

````python
ciphertext_hex = "000000071711100a0e1f7f22616b722e03061c08791301191a0b3f1f161369232f33222f2b2a310d2c270c23363c3828160b07"
known_plaintext = "SECURECOMM:v2.1|FROM:"
````

### Step 1: แปลง Hex เป็น Bytes

````python
ciphertext = bytes.fromhex(ciphertext_hex)
# Result: b'\x00\x00\x00\x07\x17\x11\x10\n\x0e\x1f..."
print(len(ciphertext))  # 51 bytes
````

### Step 2: XOR Known Plaintext กับ Ciphertext

````python
known_plaintext = "SECURECOMM:v2.1|FROM:"  # 21 characters

key_bytes = []
for i in range(len(known_plaintext)):
    key_byte = ord(known_plaintext[i]) ^ ciphertext[i]
    key_bytes.append(key_byte)

key = bytes(key_bytes)
print(key)  # b'SECRETSECRETSECRETSEC'
````

### Step 3: ระบุ Key Pattern

````
Extracted: SECRETSECRETSECRETSEC
Pattern:   SECRET (repeating)
````

Key คือ `SECRET` ที่ถูกใช้ซ้ำๆ!

### Step 4: Decrypt ข้อความทั้งหมด

````python
key = "SECRET"
decrypted = ""

for i in range(len(ciphertext)):
    decrypted_char = chr(ciphertext[i] ^ ord(key[i % len(key)]))
    decrypted += decrypted_char

print(decrypted)
# Output: SECURECOMM:v2.1|FROM:ADMIN|MSG:flag{xor_is_fun}|END
````

### Step 5: หา Flag

````
🚩 FLAG: flag{xor_is_fun}
````

---

## 💻 Complete Solution Script

````python
#!/usr/bin/env python3
"""
XOR Known Plaintext Attack - Complete Solution
"""

# Data
ciphertext_hex = "000000071711100a0e1f7f22616b722e03061c08791301191a0b3f1f161369232f33222f2b2a310d2c270c23363c3828160b07"
known_plaintext = "SECURECOMM:v2.1|FROM:"

# Convert hex to bytes
ciphertext = bytes.fromhex(ciphertext_hex)

# Extract key using known plaintext attack
key_bytes = []
for i in range(len(known_plaintext)):
    key_bytes.append(ord(known_plaintext[i]) ^ ciphertext[i])

print(f"Extracted key: {bytes(key_bytes)}")
# Output: b'SECRETSECRETSECRETSEC'

# Detect repeating pattern
key = "SECRET"  # Identified from extracted key

# Decrypt full message
decrypted = ""
for i in range(len(ciphertext)):
    decrypted += chr(ciphertext[i] ^ ord(key[i % len(key)]))

print(f"Decrypted: {decrypted}")
# Output: SECURECOMM:v2.1|FROM:ADMIN|MSG:flag{xor_is_fun}|END

# Extract flag
import re
flag = re.search(r'flag\{[^}]+\}', decrypted).group()
print(f"FLAG: {flag}")
# Output: flag{xor_is_fun}
````

---

## 💻 Alternative Methods

### Using CyberChef

1. ไปที่ [CyberChef](https://gchq.github.io/CyberChef/)
2. เพิ่ม Operations:
   - "From Hex"
   - "XOR" with key "SECRET"
3. วาง ciphertext_hex ใน Input
4. อ่าน Output

### One-liner Python

````python
key = "SECRET"
print(''.join(chr(b ^ ord(key[i%6])) for i,b in enumerate(bytes.fromhex("000000071711100a0e1f7f22616b722e03061c08791301191a0b3f1f161369232f33222f2b2a310d2c270c23363c3828160b07"))))
````

---

## 🎓 สิ่งที่ได้เรียนรู้

1. **XOR Properties**: XOR มีคุณสมบัติ self-inverse (A ⊕ A = 0)
2. **Known Plaintext Attack**: เมื่อรู้ plaintext บางส่วน สามารถหา key ได้
3. **Repeating Key Weakness**: Key ที่ซ้ำๆ สามารถถูกตรวจจับได้
4. **Real-world Impact**: WEP WiFi ถูก crack ด้วยวิธีนี้

---

## 🔐 Key Takeaways

| Topic | Lesson |
|-------|--------|
| XOR Cipher | ง่ายต่อการโจมตีถ้ารู้ plaintext บางส่วน |
| Key Management | ไม่ควรใช้ key ซ้ำหรือ key สั้น |
| Protocol Headers | Header ที่คาดเดาได้เป็นจุดอ่อน |
| Secure Encryption | ใช้ AES หรือ algorithms ที่ได้มาตรฐาน |

---

## 📚 Further Learning

1. **One-Time Pad**: XOR ที่ปลอดภัยจริงๆ (key ยาวเท่า message)
2. **Stream Ciphers**: การพัฒนาจาก XOR (เช่น RC4, ChaCha20)
3. **Frequency Analysis**: การโจมตี cipher โดยดู pattern
4. **Real CTF Challenges**: ลองทำ XOR challenges บน [CryptoHack](https://cryptohack.org/)

---

## 🚩 FLAG

````
flag{xor_is_fun}
````

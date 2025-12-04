# Unicode Dreams - Writeup (HARD MODE)

## ⚠️ ระดับความยาก: HARD

โจทย์นี้ใช้การเข้ารหัสแบบ **2 ชั้น (Two-Layer Encoding)**:
1. **Layer 1:** Punycode (Unicode → ASCII)
2. **Layer 2:** Base64 (ซ่อน Punycode)

---

## 📚 พื้นฐานที่ต้องรู้ (สอนตั้งแต่ 0)

### Punycode คืออะไร? (ทบทวน)

**Punycode** เป็น encoding ที่ใช้แปลง Unicode characters ให้เป็น ASCII format โดยอิงตาม **Bootstring algorithm** ที่ถูกกำหนดไว้ใน RFC 3492

### Base64 คืออะไร?

**Base64** เป็นการเข้ารหัสที่แปลงข้อมูล binary ให้เป็น ASCII text ใช้ตัวอักษร A-Z, a-z, 0-9, +, / และ = สำหรับ padding

### โครงสร้างของการเข้ารหัสสองชั้น

```
Original Thai text
       ↓
   [Punycode]
       ↓
    [Base64]
       ↓
 Final Output (data.txt)
```

---

## 🔍 วิธีแก้โจทย์ทีละขั้นตอน

### ขั้นตอนที่ 1: วิเคราะห์โจทย์

จาก `data.txt` พบข้อมูลที่ถูก encode:

```
[MSG #1] Output: bDNjMWJpYjhhMGE=
[MSG #2] Output: bDNjY2tjZjdibDJmdGJ4bjV2
[MSG #3] Output: MTJjYTRlMmRuMWg=
[MSG #4] Output: MWMzOTI1NWIxZmY0MDZhNjkzYzQwYWZmZmJhNTE2N2UtZWs3ZzB0  ★ CLASSIFIED ★
```

### ขั้นตอนที่ 2: หา Clues จากโจทย์

จาก description และ hints:
- "Bootstring algorithm" → RFC 3492 → Punycode!
- "SECURITY UPDATE: Output is now Base64 encoded for transport" → Base64!
- ต้อง decode 2 ชั้น!

### ขั้นตอนที่ 3: สังเกต Pattern

ข้อสังเกต:
1. ข้อมูลดูเหมือน Base64 (ตัวอักษร A-Za-z0-9+/ และ = padding)
2. System note บอกว่า outputs ถูก "wrapped in Base64"
3. ต้อง unwrap Base64 ก่อน แล้วค่อย decode Punycode

### ขั้นตอนที่ 4: Decode สองชั้น

#### Step 1: Base64 Decode

```python
import base64
b64_encoded = "MWMzOTI1NWIxZmY0MDZhNjkzYzQwYWZmZmJhNTE2N2UtZWs3ZzB0"
punycode_str = base64.b64decode(b64_encoded).decode('ascii')
print(punycode_str)
# Output: 1c39255b1ff406a693c40afffba5167e-ek7g0t
```

#### Step 2: Punycode Decode

```python
decoded = punycode_str.encode('ascii').decode('punycode')
print(decoded)
# Output: ธง1c39255b1ff406a693c40afffba5167e (ธง = "flag" in Thai)
```

### ขั้นตอนที่ 5: แปลความหมาย

`ธง` ในภาษาไทย แปลว่า "flag"

ดังนั้น: `ธง1c39255b1ff406a693c40afffba5167e` = `flag{1c39255b1ff406a693c40afffba5167e}`

---

## 💻 วิธีแก้หลายแบบ

### วิธี A: Python Script (Complete)

```python
import base64

b64_messages = [
    "bDNjMWJpYjhhMGE=",
    "bDNjY2tjZjdibDJmdGJ4bjV2",
    "MTJjYTRlMmRuMWg=",
    "MWMzOTI1NWIxZmY0MDZhNjkzYzQwYWZmZmJhNTE2N2UtZWs3ZzB0"
]

for b64_msg in b64_messages:
    # Step 1: Base64 decode
    punycode_str = base64.b64decode(b64_msg).decode('ascii')
    # Step 2: Punycode decode
    decoded = punycode_str.encode('ascii').decode('punycode')
    print(f"{b64_msg} → {punycode_str} → {decoded}")
```

**Output:**
```
bDNjMWJpYjhhMGE= → l3c1bib8a0a → สวัสดี (Hello)
bDNjY2tjZjdibDJmdGJ4bjV2 → l3cckcf7bl2ftbxn5v → ยินดีต้อนรับ (Welcome)
MTJjYTRlMmRuMWg= → 12ca4e2dn1h → นักแฮก (Hacker)
MWMzOTI1NWIxZmY0MDZhNjkzYzQwYWZmZmJhNTE2N2UtZWs3ZzB0 → 1c39255b1ff406a693c40afffba5167e-ek7g0t → ธง1c39255b1ff406a693c40afffba5167e
```

### วิธี B: Python One-liner

```bash
python3 -c "import base64; print(base64.b64decode('MWMzOTI1NWIxZmY0MDZhNjkzYzQwYWZmZmJhNTE2N2UtZWs3ZzB0').decode().encode('ascii').decode('punycode'))"
```

### วิธี C: Online Tools (Two Steps)

**Step 1 - Base64 Decode:**
1. ไปที่ https://www.base64decode.org/
2. วาง `MWMzOTI1NWIxZmY0MDZhNjkzYzQwYWZmZmJhNTE2N2UtZWs3ZzB0`
3. ได้: `1c39255b1ff406a693c40afffba5167e-ek7g0t`

**Step 2 - Punycode Decode:**
1. ไปที่ https://www.punycoder.com/
2. วาง `1c39255b1ff406a693c40afffba5167e-ek7g0t`
3. ได้: `ธง1c39255b1ff406a693c40afffba5167e`

---

## 🎓 สิ่งที่ได้เรียนรู้

1. **Layered Encoding** - การเข้ารหัสหลายชั้น
2. **Base64** - การเข้ารหัสที่ใช้สำหรับ transport data
3. **Punycode** สามารถ encode โดยไม่มี `xn--` prefix ได้
4. การวิเคราะห์ลำดับขั้นตอนการ decode

---

## 🔐 Key Takeaways

### เปรียบเทียบกับโจทย์ที่ 1

| หัวข้อ | Challenge 1 | Challenge 2 (HARD) |
|--------|-------------|-------------|
| Encoding Layers | 1 (Punycode only) | 2 (Base64 + Punycode) |
| Format | มี `xn--` prefix | Base64 wrapped |
| Context | Domain names | Secure transmission |
| Difficulty | ⭐⭐ | ⭐⭐⭐⭐ |

### Pattern Recognition Tips

- ถ้าเห็น `=` ที่ท้าย และ ตัวอักษร A-Za-z0-9+/ → น่าจะเป็น Base64
- ถ้า decode Base64 แล้วเห็น `-` ตามด้วย lowercase letters → น่าจะเป็น Punycode
- เมื่อเจอการเข้ารหัสหลายชั้น → ให้ decode ทีละชั้น

---

## 📚 Further Learning

1. **RFC 3492** - Punycode: A Bootstring encoding of Unicode
2. **RFC 4648** - Base64 encoding
3. **Multi-layer encoding** - Techniques in CTF challenges
4. **CyberChef** - Tool for chaining multiple encodings

---

## 🚩 Flag

```
flag{1c39255b1ff406a693c40afffba5167e}
```

---

## 📋 Full Decoded Messages

| Message | Base64 | Punycode | Thai | Meaning |
|---------|--------|----------|------|---------|
| #1 | bDNjMWJpYjhhMGE= | l3c1bib8a0a | สวัสดี | Hello |
| #2 | bDNjY2tjZjdibDJmdGJ4bjV2 | l3cckcf7bl2ftbxn5v | ยินดีต้อนรับ | Welcome |
| #3 | MTJjYTRlMmRuMWg= | 12ca4e2dn1h | นักแฮก | Hacker |
| #4 | MWMzOTI1NWIx... | 1c39255b...-ek7g0t | ธง[hash] | Flag |

# Unicode Dreams - Writeup

## 📚 พื้นฐานที่ต้องรู้ (สอนตั้งแต่ 0)

### Punycode คืออะไร? (ทบทวน)

**Punycode** เป็น encoding ที่ใช้แปลง Unicode characters ให้เป็น ASCII format โดยอิงตาม **Bootstring algorithm** ที่ถูกกำหนดไว้ใน RFC 3492

### โครงสร้างของ Punycode String

Punycode string ประกอบด้วย:

```
[ASCII_characters]-[encoded_unicode]
```

| ส่วน | คำอธิบาย |
|------|----------|
| ASCII characters | ตัวอักษร ASCII ที่มีในข้อความต้นฉบับ |
| `-` | Delimiter ที่แยก ASCII กับ encoded part |
| encoded unicode | ตัวอักษร Unicode ที่ถูก encode |

### ตัวอย่างโครงสร้าง

```
8806bc86bb52331ed1043c0a1f13dd50-ek7g0t
├── 8806bc86bb52331ed1043c0a1f13dd50  ← ASCII (MD5 hash)
├── -                                  ← Delimiter
└── ek7g0t                             ← Encoded Thai: ธง
```

เมื่อ decode จะได้: `ธง8806bc86bb52331ed1043c0a1f13dd50`

---

## 🔍 วิธีแก้โจทย์ทีละขั้นตอน

### ขั้นตอนที่ 1: วิเคราะห์โจทย์

จาก `data.txt` พบข้อมูลที่ถูก encode:

```
[MSG #1] Output: l3c1bib8a0a
[MSG #2] Output: l3cckcf7bl2ftbxn5v
[MSG #3] Output: 12ca4e2dn1h
[MSG #4] Output: 8806bc86bb52331ed1043c0a1f13dd50-ek7g0t  ★ CLASSIFIED ★
```

### ขั้นตอนที่ 2: หา Clues จากโจทย์

จาก description และ hints:
- "Bootstring algorithm" → RFC 3492 → Punycode!
- "Unicode to ASCII conversion for internet protocols"
- "international domain names"
- "Thai language"

### ขั้นตอนที่ 3: สังเกต Pattern

ข้อสังเกต:
1. ข้อความที่ 4 มี `-` delimiter ซึ่งแสดงว่ามี ASCII part และ unicode part
2. `8806bc86bb52331ed1043c0a1f13dd50` ดูเหมือน MD5 hash (32 characters hex)
3. `ek7g0t` น่าจะเป็น encoded unicode

### ขั้นตอนที่ 4: Decode ข้อความ

```python
encoded = "8806bc86bb52331ed1043c0a1f13dd50-ek7g0t"
decoded = encoded.encode('ascii').decode('punycode')
print(decoded)  # ธง8806bc86bb52331ed1043c0a1f13dd50 (ธง = "flag" in Thai)
```

### ขั้นตอนที่ 5: แปลความหมาย

`ธง` ในภาษาไทย แปลว่า "flag"

ดังนั้น: `ธง8806bc86bb52331ed1043c0a1f13dd50` = `flag{8806bc86bb52331ed1043c0a1f13dd50}`

---

## 💻 วิธีแก้หลายแบบ

### วิธี A: Python One-liner

```python
print("8806bc86bb52331ed1043c0a1f13dd50-ek7g0t".encode('ascii').decode('punycode'))
```

### วิธี B: Decode ทุกข้อความ

```python
messages = [
    "l3c1bib8a0a",
    "l3cckcf7bl2ftbxn5v",
    "12ca4e2dn1h",
    "8806bc86bb52331ed1043c0a1f13dd50-ek7g0t"
]

for msg in messages:
    decoded = msg.encode('ascii').decode('punycode')
    print(f"{msg} → {decoded}")
```

**Output:**
```
l3c1bib8a0a → สวัสดี (Hello)
l3cckcf7bl2ftbxn5v → ยินดีต้อนรับ (Welcome)
12ca4e2dn1h → นักแฮก (Hacker)
8806bc86bb52331ed1043c0a1f13dd50-ek7g0t → ธง8806bc86bb52331ed1043c0a1f13dd50
```

### วิธี C: Online Tools

1. ไปที่ https://www.punycoder.com/
2. วาง `8806bc86bb52331ed1043c0a1f13dd50-ek7g0t`
3. คลิก Decode
4. ได้: `ธง8806bc86bb52331ed1043c0a1f13dd50`

**หมายเหตุ:** บาง tools อาจต้องเพิ่ม `xn--` prefix

---

## 🎓 สิ่งที่ได้เรียนรู้

1. **Punycode** สามารถ encode โดยไม่มี `xn--` prefix ได้
2. โครงสร้าง Punycode แยก ASCII และ Unicode ด้วย `-`
3. ภาษาไทยสามารถ encode/decode ด้วย Punycode ได้
4. เครื่องมือ decode มีหลายตัวให้เลือกใช้

---

## 🔐 Key Takeaways

### ความแตกต่างจากโจทย์ที่ 1

| หัวข้อ | Challenge 1 | Challenge 2 |
|--------|-------------|-------------|
| Format | มี `xn--` prefix | ไม่มี prefix |
| Context | Domain names | Generic text |
| Structure | Full domain | Raw punycode |
| Complexity | Single decode | Multiple messages |

### Pattern Recognition

- ถ้าเห็น `xn--` → Punycode domain
- ถ้าเห็น `[ascii]-[code]` → Punycode with mixed content
- ถ้ามีแต่ตัวอักษร ASCII แต่มี hints เรื่อง unicode → น่าจะเป็น Punycode

---

## 📚 Further Learning

1. **RFC 3492** - Punycode: A Bootstring encoding of Unicode
2. **RFC 5891** - IDNA 2008 specification
3. **Python codecs** - https://docs.python.org/3/library/codecs.html
4. **Unicode Security** - IDN homograph attacks

---

## 🚩 Flag

```
flag{8806bc86bb52331ed1043c0a1f13dd50}
```

---

## 📋 Full Decoded Messages

| Message | Encoded | Decoded | Meaning |
|---------|---------|---------|---------|
| #1 | l3c1bib8a0a | สวัสดี | Hello |
| #2 | l3cckcf7bl2ftbxn5v | ยินดีต้อนรับ | Welcome |
| #3 | 12ca4e2dn1h | นักแฮก | Hacker |
| #4 | 8806bc86bb52331ed1043c0a1f13dd50-ek7g0t | ธง[hash] | Flag |

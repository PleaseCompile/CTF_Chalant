# The Mysterious Domain - Writeup

## 📚 พื้นฐานที่ต้องรู้ (สอนตั้งแต่ 0)

### Punycode คืออะไร?

**Punycode** เป็นวิธีการเข้ารหัส (encoding) ที่ใช้แปลง Unicode characters ให้กลายเป็น ASCII-compatible string โดยถูกออกแบบมาเพื่อใช้กับ **Internationalized Domain Names (IDN)**

### ทำไมต้องมี Punycode?

- **DNS (Domain Name System)** รองรับเฉพาะตัวอักษร ASCII เท่านั้น
- แต่โลกมีหลายภาษา (ไทย, จีน, อาหรับ, ฮิบรู ฯลฯ) ที่ต้องการใช้ domain names ในภาษาของตัวเอง
- Punycode ช่วยแปลง domain names ที่มีตัวอักษรพิเศษให้กลายเป็น ASCII ที่ DNS อ่านได้

### รู้ได้อย่างไรว่าเป็น Punycode?

**สัญญาณสำคัญ:**
1. ขึ้นต้นด้วย `xn--` (ACE prefix - ASCII Compatible Encoding prefix)
2. ตัวอักษรที่ตามมาจะเป็น ASCII ทั้งหมด
3. มักพบในบริบทของ domain names หรือ URLs

### ตัวอย่าง Punycode

| Original | Punycode |
|----------|----------|
| münchen (เมือง Munich ภาษาเยอรมัน) | xn--mnchen-3ya |
| 北京 (Beijing ภาษาจีน) | xn--fiqs8s |
| กรุงเทพ (Bangkok ภาษาไทย) | xn--12c0bsbkc4d4g |

---

## 🔍 วิธีแก้โจทย์ทีละขั้นตอน

### ขั้นตอนที่ 1: วิเคราะห์ข้อมูลที่ได้รับ

เปิดไฟล์ `data.txt` จะพบข้อมูลเป็น log ของ DNS queries:

```
[LOG ENTRY 001]
xn--42c8buaqi6de.suspicious.net

[LOG ENTRY 002]  
xn--c3c2aa9a3cb9fudubf.darkweb.org

[LOG ENTRY 003]
xn--l3ckx7ji.underground.io

[LOG ENTRY 004] ★ PRIMARY TARGET ★
xn--1c39255b1ff406a693c40afffba5167e-kh7god82awxrl.secret.net
```

### ขั้นตอนที่ 2: สังเกต Pattern

- ทุก domain ขึ้นต้นด้วย `xn--`
- นี่คือ **ACE prefix** ที่บ่งบอกว่าเป็น Punycode encoding!
- Hint ในโจทย์กล่าวถึง "internationalized domain names" และ "ASCII Compatible Encoding"

### ขั้นตอนที่ 3: Decode Punycode

#### วิธีที่ 1: ใช้ Python

```python
# Remove 'xn--' prefix และ decode
domain = "xn--1c39255b1ff406a693c40afffba5167e-kh7god82awxrl"
punycode_part = domain[4:]  # Remove 'xn--'
decoded = punycode_part.encode('ascii').decode('punycode')
print(decoded)
# Output: ธงคือ1c39255b1ff406a693c40afffba5167e
```

#### วิธีที่ 2: ใช้ Online Tools

1. ไปที่ https://www.punycoder.com/
2. วาง `xn--1c39255b1ff406a693c40afffba5167e-kh7god82awxrl`
3. คลิก "Decode"
4. ได้ผลลัพธ์: `ธงคือ1c39255b1ff406a693c40afffba5167e`

### ขั้นตอนที่ 4: แปลความหมาย

ผลลัพธ์ที่ได้: `ธงคือ1c39255b1ff406a693c40afffba5167e`

- `ธงคือ` = "flag is" ในภาษาไทย
- `1c39255b1ff406a693c40afffba5167e` = MD5 hash

### ขั้นตอนที่ 5: สร้าง Flag

รวมกันเป็น: `flag{1c39255b1ff406a693c40afffba5167e}`

---

## 💻 วิธีแก้หลายแบบ

### วิธี A: Python Script

```python
import codecs

domains = [
    "xn--42c8buaqi6de",
    "xn--c3c2aa9a3cb9fudubf", 
    "xn--l3ckx7ji",
    "xn--1c39255b1ff406a693c40afffba5167e-kh7god82awxrl"
]

for domain in domains:
    decoded = domain[4:].encode('ascii').decode('punycode')
    print(f"{domain} -> {decoded}")
```

**Output:**
```
xn--42c8buaqi6de -> ความลับ (secret)
xn--c3c2aa9a3cb9fudubf -> ซ่อนอยู่ใน (is hidden in)
xn--l3ckx7ji -> โดเมน (domain)
xn--1c39255b1ff406a693c40afffba5167e-kh7god82awxrl -> ธงคือ1c39255b1ff406a693c40afffba5167e
```

### วิธี B: Command Line

```bash
python3 -c "print('1c39255b1ff406a693c40afffba5167e-kh7god82awxrl'.encode('ascii').decode('punycode'))"
```

### วิธี C: Online Decoder

- https://www.punycoder.com/
- https://mothereff.in/punycode
- https://www.browserling.com/tools/punycode-decode

---

## 🎓 สิ่งที่ได้เรียนรู้

1. **Punycode** เป็นการเข้ารหัส Unicode เป็น ASCII
2. **ACE prefix `xn--`** เป็นตัวบ่งบอกว่าเป็น Punycode
3. **IDN (Internationalized Domain Names)** ใช้ Punycode เพื่อให้ domain หลายภาษาทำงานได้
4. สามารถ decode Punycode ได้ด้วย Python หรือ online tools

---

## 🔐 Key Takeaways

| หัวข้อ | รายละเอียด |
|--------|------------|
| Encoding | Punycode |
| Identifier | Prefix `xn--` |
| Purpose | IDN - Internationalized Domain Names |
| RFC | RFC 3492 |
| Decode Method | Python `decode('punycode')` หรือ online tools |

---

## 📚 Further Learning

1. **RFC 3492** - Punycode: A Bootstring encoding of Unicode
2. **RFC 5891** - Internationalized Domain Names in Applications (IDNA)
3. **IDN Homograph Attack** - การโจมตีโดยใช้ domain ที่ดูคล้ายกัน
4. **Unicode Security** - ความปลอดภัยที่เกี่ยวข้องกับ Unicode

---

## 🚩 Flag

```
flag{1c39255b1ff406a693c40afffba5167e}
```

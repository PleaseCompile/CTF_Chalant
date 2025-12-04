# 👯 The Twins' Treasure - Writeup

## 📚 พื้นฐานที่ต้องรู้ (สอนตั้งแต่ 0)

### ทบทวน RSA
RSA เป็นการเข้ารหัสแบบ asymmetric ที่ใช้:
- **Encryption**: `c = m^e mod n`
- **Decryption**: `m = c^d mod n`

โดยที่:
- `m` = message (ข้อความต้นฉบับ)
- `c` = ciphertext (ข้อความที่เข้ารหัสแล้ว)
- `e` = public exponent
- `d` = private exponent
- `n` = modulus (p × q)

### Modular Arithmetic คืออะไร?
**Modular** หมายถึงการหารเอาเศษ

ตัวอย่าง:
- `7 mod 3 = 1` (เพราะ 7 ÷ 3 = 2 เศษ 1)
- `10 mod 5 = 0` (เพราะ 10 ÷ 5 = 2 เศษ 0)
- `100 mod 7 = 2`

### จุดสำคัญ: ถ้า x < n แล้ว x mod n = x
```
ถ้า x = 5 และ n = 10
5 mod 10 = 5 (เพราะ 5 < 10)
```

นี่คือหัวใจของ **Small e Attack**!

---

## 🎯 Small e Attack คืออะไร?

### สถานการณ์ปกติ
```
Encryption: c = m^e mod n
ถ้า m = 100, e = 3, n = 50

m^e = 100^3 = 1,000,000
c = 1,000,000 mod 50 = 0  (มี modular reduction)
```

### สถานการณ์ที่มีช่องโหว่
```
Encryption: c = m^e mod n
ถ้า m = 10, e = 3, n = 10000

m^e = 10^3 = 1,000
c = 1,000 mod 10000 = 1,000  (ไม่มี modular reduction!)

เพราะ 1,000 < 10,000 ดังนั้น c = m^e โดยตรง
```

### ผลที่ตามมา
```
ถ้า c = m^e (ไม่มี mod)
แล้ว m = e√c (ถอดรากที่ e)

เมื่อ e = 3: m = ∛c (cube root)
```

---

## 🔍 วิธีแก้โจทย์ทีละขั้นตอน

### ขั้นตอนที่ 1: อ่านโจทย์และวิเคราะห์
จาก story:
- "ยกกำลังด้วยเลขเล็กๆ แค่ 3" → **e = 3**
- "ถ้าข้อความสั้นเกินไป และไม่ได้เติมอะไรเพิ่ม" → **ไม่มี padding, m เล็ก**
- "บางทีก็แค่ถอดรากที่สามก็ได้" → **Small e Attack!**

### ขั้นตอนที่ 2: ดูข้อมูลใน data.txt
```python
n = 77456517883527022021948390318327541222016017783362332779389456750836823396362887818219046441718630076997214181886070089216458166750802938058126021761327197023022783233525512537903958062484242156262272897007577852189268029360558697508856581696596688397858134732906049153694984637487319997358963875751289071741
e = 3
c = 199928678441559346271160947116290616870303022721577936466055587492436426199507510352958248268684005688540664284766982470563248689622058788066917
```

### ขั้นตอนที่ 3: ตรวจสอบว่า c < n
```python
c < n  # True!
```
เนื่องจาก c < n มาก แสดงว่า m^3 < n ดังนั้น **c = m^3 โดยไม่มี mod**

### ขั้นตอนที่ 4: ถอดรากที่ 3
```python
m = ∛c
m = cube_root(199928678441559346271160947116290616870303022721577936466055587492436426199507510352958248268684005688540664284766982470563248689622058788066917)
m = 584734024210386484927995793294631094357640571773
```

### ขั้นตอนที่ 5: แปลง m เป็น string
```python
# Convert integer to bytes
flag_bytes = m.to_bytes((m.bit_length() + 7) // 8, 'big')
flag = flag_bytes.decode()
# flag = "flag{sm4ll_3_4tt4ck}"
```

---

## 💻 วิธีแก้หลายแบบ

### วิธีที่ 1: Python Script (Manual Cube Root)
```python
def integer_cube_root(n):
    """Newton's method for cube root"""
    if n == 0:
        return 0
    x = n
    y = (2 * x + n // (x * x)) // 3
    while y < x:
        x = y
        y = (2 * x + n // (x * x)) // 3
    return x

c = 199928678441559346271160947116290616870303022721577936466055587492436426199507510352958248268684005688540664284766982470563248689622058788066917

m = integer_cube_root(c)

# Verify
assert m ** 3 == c, "Not a perfect cube!"

# Decode
flag = m.to_bytes((m.bit_length() + 7) // 8, 'big').decode()
print(flag)  # flag{sm4ll_3_4tt4ck}
```

### วิธีที่ 2: ใช้ gmpy2 Library
```python
import gmpy2

c = 199928678441559346271160947116290616870303022721577936466055587492436426199507510352958248268684005688540664284766982470563248689622058788066917

m, is_perfect = gmpy2.iroot(c, 3)
print(f"Perfect cube: {is_perfect}")  # True

flag = int(m).to_bytes((int(m).bit_length() + 7) // 8, 'big').decode()
print(flag)  # flag{sm4ll_3_4tt4ck}
```

### วิธีที่ 3: ใช้ Online Tools

**WolframAlpha** (https://www.wolframalpha.com/)
1. ค้นหา: `cube root of 199928678441559346271160947116290616870303022721577936466055587492436426199507510352958248268684005688540664284766982470563248689622058788066917`
2. ได้ผลลัพธ์: `584734024210386484927995793294631094357640571773`
3. แปลงเป็น hex: `0x666c61677b736d346c6c5f335f34747434636b7d`
4. Decode hex to ASCII: `flag{sm4ll_3_4tt4ck}`

**CyberChef**
1. ใส่ค่า m (หลังถอดราก)
2. ใช้ "From Decimal" → "To Hex" → "From Hex"

---

## 🎓 สิ่งที่ได้เรียนรู้

1. **Small e Attack**
   - เกิดขึ้นเมื่อ e เล็ก และ m^e < n
   - สามารถถอดรหัสได้โดยการถอดราก

2. **ความสำคัญของ Padding**
   - Padding ทำให้ m มีขนาดใกล้เคียง n
   - ป้องกัน small e attack

3. **การเลือก e ที่เหมาะสม**
   - e = 65537 เป็นมาตรฐาน
   - ใหญ่พอที่จะป้องกันการโจมตี

---

## 🔐 Key Takeaways

1. **e ที่เล็ก + m ที่เล็ก = ช่องโหว่**
2. **ใช้ e = 65537** เสมอในการใช้งานจริง
3. **ต้องใช้ padding** (เช่น OAEP) ในการเข้ารหัส RSA
4. **ตรวจสอบว่า m^e > n** ก่อนเข้ารหัส

---

## 📚 Further Learning

### Related Attacks
1. **Håstad's Broadcast Attack**
   - เมื่อส่งข้อความเดียวกันไป e คนด้วย n ที่ต่างกัน
   - ใช้ Chinese Remainder Theorem

2. **Coppersmith's Attack**
   - เมื่อรู้บางส่วนของ m
   - ใช้ lattice-based techniques

3. **Franklin-Reiter Related Message Attack**
   - เมื่อมี 2 ข้อความที่เกี่ยวข้องกัน

### Resources
- [RSA Small e Attack](https://crypto.stackexchange.com/questions/6713/low-public-exponent-attack-for-rsa)
- [Coppersmith's Attack](https://en.wikipedia.org/wiki/Coppersmith%27s_attack)
- [CryptoHack RSA Challenges](https://cryptohack.org/challenges/rsa/)

---

## 🚩 Flag
```
flag{sm4ll_3_4tt4ck}
```

---
*"When the exponent is small and the message is short, the math becomes trivially simple. Always pad your messages!"*

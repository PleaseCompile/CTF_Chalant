# 🎭 ประตูสองชั้นแห่งเงามืด (The Double-Locked Gate)

## 🎯 Concept
มีประตูลับที่ต้องผ่าน **สองด่าน** จึงจะเข้าถึงความลับได้
แต่ละด่านใช้ **การแปลงเชิงเส้น** คนละสูตร...

A secret gate that requires passing **two barriers** to access the secret.
Each barrier uses a different **linear transformation**...

---

## ⭐ Difficulty: Hard (⭐⭐⭐⭐⭐)

**ความท้าทาย:** 
- ข้อความถูกเข้ารหัส **2 ครั้ง** ด้วย Affine cipher คนละ key
- ต้องถอดรหัส 2 ชั้น หรือหา combined key
- ต้องเข้าใจว่า Double Affine = Single Affine

---

## 📖 Story

ตำนานเล่าว่า องค์กรโบราณ "Order of the Double Lock" ใช้ระบบป้องกันความลับ 2 ชั้น

เมื่อคุณค้นพบห้องลับของพวกเขา คุณพบจารึกบนผนัง:

> "ประตูแรก: **ห้าคูณ แปดบวก**
> ประตูสอง: **เจ็ดคูณ สามบวก**
> 
> ผู้ที่ผ่านประตูทั้งสองจะได้เข้าถึงความจริง
> แต่จำไว้... การเข้าสองครั้ง = การเข้าครั้งเดียวด้วยสูตรใหม่"

ข้อความลับที่ต้องถอดรหัส:
```
WSRACHJBNIDFQCRCHPRERGMREW
```

คำถามคือ... คุณจะถอดรหัสอย่างไร?

---

## 💡 Hints

### 🇹🇭 คำใบ้ภาษาไทย
1. **"ห้าคูณ แปดบวก"** → ประตูแรก: a₁=5, b₁=8
2. **"เจ็ดคูณ สามบวก"** → ประตูสอง: a₂=7, b₂=3
3. ต้องถอดรหัสประตูสองก่อน แล้วค่อยถอดประตูแรก (ย้อนกลับ!)
4. หรือ... คำนวณ **combined key**: a = (a₂ × a₁) mod 26, b = (a₂ × b₁ + b₂) mod 26
5. Double Affine = Single Affine ด้วย key ใหม่!

### 🇬🇧 English Hints
1. **"Five multiply, Eight add"** → First gate: a₁=5, b₁=8
2. **"Seven multiply, Three add"** → Second gate: a₂=7, b₂=3
3. Must decrypt gate 2 first, then gate 1 (reverse order!)
4. Or... calculate **combined key**: a = (a₂ × a₁) mod 26, b = (a₂ × b₁ + b₂) mod 26
5. Double Affine = Single Affine with new key!

---

## 📦 Data

ไฟล์ข้อมูล: `data.txt`

ข้อความที่เข้ารหัส 2 ชั้น:
```
WSRACHJBNIDFQCRCHPRERGMREW
```

**Keys:**
- First encryption: a₁=5, b₁=8
- Second encryption: a₂=7, b₂=3

**การเข้ารหัส:**
```
Plaintext → [Affine 1: 5x+8] → [Affine 2: 7x+3] → Ciphertext
```

---

## 🎮 Challenge

1. เข้าใจว่าข้อความถูกเข้ารหัส 2 ครั้งอย่างไร
2. ถอดรหัสโดย:
   - วิธี A: ถอดทีละชั้น (ย้อนกลับ)
   - วิธี B: หา combined key แล้วถอดครั้งเดียว
3. หา flag จากข้อความที่ถอดรหัสได้

**หมายเหตุ:** ข้อความที่ถอดรหัสได้จะบอกคุณว่า flag คืออะไร รูปแบบจะเป็น `THEFLAGIS...`

---

## 🚩 Flag Format

```
flag{md5_hash}
```

**คำแนะนำ:** เมื่อถอดรหัสได้ข้อความแล้ว ให้นำส่วนที่อยู่หลัง "THEFLAGIS" มาทำเป็น MD5 hash (เพิ่ม underscore ระหว่างคำ)

---

## 📚 ความรู้ที่จะได้

- Double Encryption และการ compose functions
- ทำไม Double Affine = Single Affine
- Composition of linear transformations
- Group theory basics (closure property)

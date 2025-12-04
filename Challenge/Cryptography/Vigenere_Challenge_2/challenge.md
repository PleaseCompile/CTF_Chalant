# 🎼 The Composer's Code (รหัสของนักประพันธ์เพลง)

## 🎯 Concept
โจทย์นี้จะสอนเกี่ยวกับการเข้ารหัสที่ใช้ "กุญแจ" (key) ที่มีความหมายทั้งในเชิงดนตรีและการเข้ารหัส โดยตัวอักษรแต่ละตัวจะถูก "ทรานสโพส" (เลื่อน) ตามคีย์ที่กำหนด

**Difficulty:** ⭐⭐☆☆☆ (Medium)

---

## 📖 Story

### 🇹🇭 ภาษาไทย
คุณได้รับจดหมายปริศนาจากนักประพันธ์เพลงลึกลับคนหนึ่ง เขาเขียนไว้ว่า:

> *"ข้อความนี้เข้ารหัสด้วย 'คีย์' เหมือนกับการเล่นเปียโน ถ้าคุณมี key ที่ถูกต้อง คุณจะอ่านโน้ตทุกตัวได้ถูกต้อง"*
>
> *"คีย์ของฉันไม่ใช่แค่ตัวเลขเดียว แต่เป็นคำที่วนซ้ำเหมือน motif ในซิมโฟนี"*
>
> *"ลองนึกถึงโน้ตดนตรี... C, D, E, F, G, A, B... แต่ละตัวมีค่าต่างกัน เหมือนตัวอักษร A=0, B=1, C=2..."*

ที่ด้านล่างของจดหมาย มีข้อความเพิ่มเติมว่า:
> *"P.S. กุญแจซ่อนอยู่ในเพลงที่ยิ่งใหญ่ที่สุดของ ABBA... ชื่อเพลงคืออะไรนะ? 🎹"*

### 🇬🇧 English
You received a mysterious letter from an anonymous composer who wrote:

> *"This message is encrypted with a 'key' like playing the piano. If you have the right key, you can read every note correctly."*
>
> *"My key is not just a single number, but a word that repeats like a motif in a symphony."*
>
> *"Think of musical notes... C, D, E, F, G, A, B... each one has a different value, like letters A=0, B=1, C=2..."*

At the bottom of the letter, there's an additional note:
> *"P.S. The key is hidden in ABBA's greatest hit song... What's the song title? 🎹"*

---

## 💡 Hints

### 🇹🇭 Hint ภาษาไทย
1. **Hint 1:** "คีย์ที่วนซ้ำ" + "ตัวอักษรแต่ละตัวถูกเลื่อนต่างกัน" = cipher ชนิดพิเศษที่ไม่ใช่ Caesar
2. **Hint 2:** การเข้ารหัสนี้ถูกตั้งชื่อตามนักเข้ารหัสชาวฝรั่งเศส ลองค้นหา "polyalphabetic cipher" + "French diplomat"
3. **Hint 3:** เพลงดังของ ABBA... "Dancing Queen"? "Mamma Mia"? "Fernando"? ลองทีละตัว (ตัวพิมพ์ใหญ่ทั้งหมด ไม่มีเว้นวรรค)

### 🇬🇧 English Hints
1. **Hint 1:** "Repeating key" + "each letter shifted differently" = a special cipher that's not Caesar
2. **Hint 2:** This cipher is named after a French cryptographer. Search for "polyalphabetic cipher" + "French diplomat"
3. **Hint 3:** ABBA's famous song... "Dancing Queen"? "Mamma Mia"? "Fernando"? Try each one (all uppercase, no spaces)

---

## 📦 Data File
ไฟล์: `secret_melody.txt`

---

## 🎮 Challenge
ถอดรหัสข้อความลับของนักประพันธ์เพลงลึกลับและหา flag ที่ซ่อนอยู่

Decrypt the secret message from the mysterious composer and find the hidden flag.

---

## 🚩 Flag Format
```
flag{...}
```

---

## 📝 Additional Notes
- การเข้ารหัสแบบนี้ใช้ "คีย์" เป็น "คำ" ไม่ใช่ตัวเลขเดียว
- This cipher uses a "word" as the key, not just a single number
- ลองนึกถึง cipher ที่พัฒนาต่อยอดจาก Caesar โดยใช้ key หลายตัว
- Think of a cipher that evolved from Caesar by using multiple keys
- ถ้าลองใช้ frequency analysis จะไม่ได้ผล เพราะตัวอักษรเดียวกันอาจถูกเข้ารหัสเป็นตัวต่างกัน
- Frequency analysis won't work easily because the same letter can be encrypted differently

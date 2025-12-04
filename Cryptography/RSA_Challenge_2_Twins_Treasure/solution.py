"""
The Twins' Treasure - Solution
RSA Small e Attack Challenge

Multiple methods: Manual, Script, Online Tools
"""

def integer_cube_root(n):
    """
    คำนวณ integer cube root ของ n
    ใช้ Newton's method
    """
    if n < 0:
        return -integer_cube_root(-n)
    if n == 0:
        return 0
    x = n
    y = (2 * x + n // (x * x)) // 3
    while y < x:
        x = y
        y = (2 * x + n // (x * x)) // 3
    return x

def integer_nth_root(n, k):
    """
    คำนวณ integer kth root ของ n
    """
    if n < 0:
        return -integer_nth_root(-n, k)
    if n == 0:
        return 0
    x = n
    while True:
        y = ((k - 1) * x + n // (x ** (k - 1))) // k
        if y >= x:
            return x
        x = y

def method1_manual():
    """
    วิธีที่ 1: ทำมือ (Manual Calculation)
    
    จุดสำคัญ:
    1. RSA ปกติ: c = m^e mod n
    2. แต่ถ้า m^e < n แล้ว c = m^e (ไม่มี mod!)
    3. ดังนั้น m = ∛c (cube root)
    
    ขั้นตอน:
    1. สังเกตว่า e = 3 (เล็กมาก)
    2. สังเกตว่า c มีค่าน้อยกว่า n มาก
    3. แปลว่า m^3 < n → c = m^3 โดยไม่มี mod
    4. ดังนั้น m = ∛c
    """
    print("=== วิธีที่ 1: Manual Understanding ===")
    print("1. RSA Encryption: c = m^e mod n")
    print("2. ถ้า m^e < n แล้ว: c = m^e (ไม่มี mod)")
    print("3. เมื่อ e = 3: c = m³")
    print("4. ดังนั้น: m = ∛c (cube root)")
    print()
    print("นี่คือจุดอ่อนของ RSA เมื่อใช้ e ที่เล็กมาก!")
    print()

def method2_script():
    """
    วิธีที่ 2: ใช้ Python Script
    """
    print("=== วิธีที่ 2: Python Script ===")
    
    # Given values from data.txt
    n = 77456517883527022021948390318327541222016017783362332779389456750836823396362887818219046441718630076997214181886070089216458166750802938058126021761327197023022783233525512537903958062484242156262272897007577852189268029360558697508856581696596688397858134732906049153694984637487319997358963875751289071741
    e = 3
    c = 199928678441559346271160947116290616870303022721577936466055587492436426199507510352958248268684005688540664284766982470563248689622058788066917
    
    print(f"n = {n}")
    print(f"e = {e}")
    print(f"c = {c}")
    print()
    
    # Check if c < n (small e attack is possible)
    print(f"c < n: {c < n}")
    print()
    
    # Method 1: Using integer_cube_root
    m = integer_cube_root(c)
    
    # Verify m^3 == c
    if m ** 3 == c:
        print(f"✓ m³ = c (Small e attack works!)")
        print(f"m = {m}")
        
        # Convert integer to bytes
        flag_bytes = m.to_bytes((m.bit_length() + 7) // 8, 'big')
        flag = flag_bytes.decode()
        print(f"\n🚩 Flag: {flag}")
    else:
        print("Small e attack failed")
    
    return flag

def method2_script_gmpy2():
    """
    วิธีที่ 2b: ใช้ gmpy2 library (ถ้ามี)
    """
    print("=== วิธีที่ 2b: Using gmpy2 ===")
    print("pip install gmpy2")
    print()
    print("```python")
    print("import gmpy2")
    print("c = 199928678441559346271160947116290616870303022721577936466055587492436426199507510352958248268684005688540664284766982470563248689622058788066917")
    print("m, is_perfect = gmpy2.iroot(c, 3)")
    print("print(m.to_bytes((m.bit_length() + 7) // 8, 'big').decode())")
    print("```")
    print()

def method3_online_tools():
    """
    วิธีที่ 3: ใช้ Online Tools
    
    เครื่องมือที่แนะนำ:
    1. WolframAlpha: https://www.wolframalpha.com/
       - ค้นหา "cube root of [c]"
    
    2. Online Calculator:
       - https://www.dcode.fr/cube-root
       - https://www.calculator.net/root-calculator.html
    
    3. RsaCtfTool:
       - https://github.com/Ganapati/RsaCtfTool
       - python3 RsaCtfTool.py -n [n] -e 3 --uncipher [c]
    """
    print("=== วิธีที่ 3: Online Tools ===")
    print("1. WolframAlpha: ค้นหา 'cube root of c'")
    print("2. dCode: https://www.dcode.fr/cube-root")
    print("3. RsaCtfTool: python3 RsaCtfTool.py -n [n] -e 3 --uncipher [c]")
    print()
    print("ขั้นตอน:")
    print("1. คัดลอกค่า c จาก data.txt")
    print("2. หา cube root ของ c")
    print("3. แปลงผลลัพธ์เป็น bytes แล้ว decode เป็น string")

def bonus_theory():
    """
    Bonus: ทฤษฎี Small e Attack
    
    Small e Attack:
    - เกิดขึ้นเมื่อ e มีค่าน้อย (เช่น e=3) และ m มีขนาดเล็ก
    - ถ้า m^e < n แล้ว c = m^e (ไม่มี modular reduction)
    - ทำให้สามารถหา m ได้โดยการถอดราก
    
    ทำไมถึงเกิดขึ้น?
    - RSA encryption: c = m^e mod n
    - ถ้า m^e < n แล้ว mod n ไม่มีผลอะไร
    - c = m^e → m = e√c
    
    วิธีป้องกัน:
    1. ใช้ e ที่ใหญ่พอ (e = 65537 เป็นมาตรฐาน)
    2. ใช้ padding (เช่น OAEP) เพื่อให้ m มีขนาดใกล้เคียง n
    3. ไม่เข้ารหัสข้อความสั้นๆ โดยตรง
    
    Variants ของ Small e Attack:
    1. Håstad's Broadcast Attack: เมื่อส่งข้อความเดียวกันไปหลายคน
    2. Coppersmith's Attack: ใช้ lattice-based techniques
    """
    print("=== Bonus: Small e Attack Theory ===")
    print()
    print("สาเหตุ:")
    print("- RSA: c = m^e mod n")
    print("- ถ้า m^e < n → c = m^e (ไม่มี mod)")
    print("- m = ∛c (cube root เมื่อ e=3)")
    print()
    print("วิธีป้องกัน:")
    print("1. ใช้ e = 65537 (standard)")
    print("2. ใช้ padding (OAEP)")
    print("3. ไม่เข้ารหัสข้อความสั้นโดยตรง")
    print()
    print("Related Attacks:")
    print("- Håstad's Broadcast Attack")
    print("- Coppersmith's Attack")

if __name__ == "__main__":
    print("=" * 60)
    print("The Twins' Treasure - Small e Attack Solution")
    print("=" * 60)
    print()
    
    method1_manual()
    print()
    
    flag = method2_script()
    print()
    
    method2_script_gmpy2()
    print()
    
    method3_online_tools()
    print()
    
    bonus_theory()

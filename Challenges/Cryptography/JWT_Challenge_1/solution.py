"""
The Three-Part Puzzle - Solution
JWT (JSON Web Token) Decode Challenge

Multiple methods: Manual, Script, Online Tools
"""

import base64
import json


def method1_manual():
    """
    วิธีที่ 1: ทำมือ (Manual Decode)
    
    ขั้นตอน:
    1. แยก token ออกเป็น 3 ส่วนด้วยจุด (.)
    2. แต่ละส่วนเข้ารหัสด้วย Base64URL
    3. แปลง Base64URL เป็น Base64 ปกติ (แทนที่ - ด้วย +, _ ด้วย /)
    4. Decode Base64 เพื่อดูข้อมูล
    """
    
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkhhY2tlciBIZXJvIiwiZmxhZyI6ImZsYWd7and0X2QzYzBkM19tNHN0M3J9IiwiaWF0IjoxNTE2MjM5MDIyfQ.abc123xyz789"
    
    # แยกส่วน
    parts = token.split('.')
    print(f"Header (Part 1): {parts[0]}")
    print(f"Payload (Part 2): {parts[1]}")
    print(f"Signature (Part 3): {parts[2]}")
    
    # Decode Header
    header_b64 = parts[0].replace('-', '+').replace('_', '/')
    # เพิ่ม padding ถ้าจำเป็น
    header_b64 += '=' * (4 - len(header_b64) % 4) if len(header_b64) % 4 else ''
    header = base64.b64decode(header_b64).decode('utf-8')
    print(f"\nDecoded Header: {header}")
    
    # Decode Payload - ส่วนที่มี flag
    payload_b64 = parts[1].replace('-', '+').replace('_', '/')
    payload_b64 += '=' * (4 - len(payload_b64) % 4) if len(payload_b64) % 4 else ''
    payload = base64.b64decode(payload_b64).decode('utf-8')
    print(f"Decoded Payload: {payload}")
    
    # หา flag
    payload_json = json.loads(payload)
    flag = payload_json.get('flag', 'Not found')
    print(f"\n🚩 FLAG: {flag}")
    
    return flag


def method2_script():
    """
    วิธีที่ 2: ใช้ Script อัตโนมัติ
    
    ใช้ฟังก์ชัน base64.urlsafe_b64decode โดยตรง
    """
    
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkhhY2tlciBIZXJvIiwiZmxhZyI6ImZsYWd7and0X2QzYzBkM19tNHN0M3J9IiwiaWF0IjoxNTE2MjM5MDIyfQ.abc123xyz789"
    
    def decode_jwt_part(part):
        """Decode JWT part with proper padding"""
        # เพิ่ม padding
        padding = 4 - len(part) % 4
        if padding != 4:
            part += '=' * padding
        return base64.urlsafe_b64decode(part).decode('utf-8')
    
    parts = token.split('.')
    
    header = json.loads(decode_jwt_part(parts[0]))
    payload = json.loads(decode_jwt_part(parts[1]))
    
    print("Header:", json.dumps(header, indent=2))
    print("Payload:", json.dumps(payload, indent=2, ensure_ascii=False))
    print(f"\n🚩 FLAG: {payload['flag']}")
    
    return payload['flag']


def method3_online():
    """
    วิธีที่ 3: เครื่องมือออนไลน์
    
    เว็บไซต์ที่ใช้ได้:
    1. https://jwt.io - เว็บยอดนิยมสำหรับ decode JWT
    2. https://www.base64decode.org - decode แต่ละส่วนแยกกัน
    3. https://token.dev - JWT decoder
    
    วิธีใช้ jwt.io:
    1. ไปที่ https://jwt.io
    2. วาง token ในช่อง "Encoded"
    3. ดูผลลัพธ์ในส่วน "Decoded"
    4. หา flag ในส่วน PAYLOAD
    """
    
    print("🌐 Online Tools:")
    print("1. jwt.io - วาง token แล้วดู payload")
    print("2. base64decode.org - decode แต่ละส่วนด้วยมือ")
    print("3. CyberChef - From Base64 -> จะเห็นข้อมูล")
    print()
    print("Token to decode:")
    print("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkhhY2tlciBIZXJvIiwiZmxhZyI6ImZsYWd7and0X2QzYzBkM19tNHN0M3J9IiwiaWF0IjoxNTE2MjM5MDIyfQ.abc123xyz789")


def method4_pyjwt():
    """
    วิธีที่ 4: ใช้ PyJWT library
    
    ติดตั้ง: pip install pyjwt
    """
    
    try:
        import jwt
        
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkhhY2tlciBIZXJvIiwiZmxhZyI6ImZsYWd7and0X2QzYzBkM19tNHN0M3J9IiwiaWF0IjoxNTE2MjM5MDIyfQ.abc123xyz789"
        
        # Decode without verification (เพราะเราไม่รู้ secret)
        payload = jwt.decode(token, options={"verify_signature": False})
        
        print("Decoded payload:", json.dumps(payload, indent=2, ensure_ascii=False))
        print(f"\n🚩 FLAG: {payload['flag']}")
        
        return payload['flag']
        
    except ImportError:
        print("PyJWT not installed. Run: pip install pyjwt")


def bonus_theory():
    """
    Bonus: ทฤษฎี JWT
    
    JWT (JSON Web Token) ประกอบด้วย 3 ส่วน:
    
    1. HEADER - ข้อมูล algorithm และ type
       {"alg": "HS256", "typ": "JWT"}
    
    2. PAYLOAD - ข้อมูลที่ต้องการส่ง (claims)
       {"sub": "1234567890", "name": "John", "iat": 1516239022}
    
    3. SIGNATURE - ลายเซ็นดิจิทัลเพื่อตรวจสอบความถูกต้อง
       HMACSHA256(base64UrlEncode(header) + "." + base64UrlEncode(payload), secret)
    
    ⚠️ สำคัญ: Payload ไม่ได้เข้ารหัส! แค่ encode ด้วย Base64URL
    ดังนั้นข้อมูลใน payload สามารถอ่านได้โดยทุกคน
    ห้ามใส่ข้อมูลลับใน JWT payload!
    """
    
    print(bonus_theory.__doc__)


if __name__ == "__main__":
    print("=" * 50)
    print("Method 1: Manual Decode")
    print("=" * 50)
    method1_manual()
    
    print("\n" + "=" * 50)
    print("Method 2: Script")
    print("=" * 50)
    method2_script()
    
    print("\n" + "=" * 50)
    print("Method 3: Online Tools")
    print("=" * 50)
    method3_online()
    
    print("\n" + "=" * 50)
    print("Method 4: PyJWT Library")
    print("=" * 50)
    method4_pyjwt()
    
    print("\n" + "=" * 50)
    print("Bonus: JWT Theory")
    print("=" * 50)
    bonus_theory()

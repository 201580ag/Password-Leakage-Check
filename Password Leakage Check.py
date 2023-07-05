import requests
import hashlib
import getpass

def check_password_leaks(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    sha1_prefix = sha1_password[:5]
    sha1_suffix = sha1_password[5:]
    
    url = f"https://api.pwnedpasswords.com/range/{sha1_prefix}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        hashes = response.text.splitlines()
        
        for hash in hashes:
            if sha1_suffix in hash:
                return True
    
    return False

password = getpass.getpass('비밀번호를 입력하세요(입력한 비밀번호가 안보이는게 정상입니다): ')

if check_password_leaks(password):
    print("유출된 기록이 있습니다.")
else:
    print("유출된 기록이 없습니다.")

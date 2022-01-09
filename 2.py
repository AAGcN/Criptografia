from Crypto import Random
from Crypto.Cipher import AES
from Block.ctr import aes_ctr
from secrets import token_bytes, randbits
from pwn import *

class SuperSafeServer:
    def __init__(self):
        self._key = token_bytes(AES.key_size[0])
        self._nonce = randbits(64)

    def create_cookie(self, user_data):
        if ';' in user_data or '=' in user_data:
            raise Exception("Caracteres ilegales en user data")
        cookie_string = "cookieversion=2.0;userdata=" + user_data + ";safety=veryhigh"
        return aes_ctr(cookie_string.encode(), self._key, self._nonce)

    def check_admin(self, cookie):
        cookie_string = aes_ctr(cookie, self._key, self._nonce).decode()
        return ';admin=true;' in cookie_string

def forge_cookie():
    server = SuperSafeServer()
    user_data = 'Cocomogolol'
    cookie = server.create_cookie(user_data)
    # Modificar la cookie
    cheat = (b'\x00' * len(b"cookieversion=2.0;userdata=") + xor(b';admin=true', b'Cocomogolol') + b'\x00' * len(b";safety=veryhigh"))
    cookie = xor(cookie, cheat)
    if server.check_admin(cookie):
        print("Acceso Admin!")

    
print(forge_cookie())
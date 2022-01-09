from base64 import b64decode
from Crypto.Cipher import AES

def aes_gcm_encrypt(data, key):
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    nonce = cipher.nonce
    return ciphertext, tag, nonce

def aes_gcm_decrypt(data, tag, nonce, key):
    cipher = AES.new(key, AES.MODE_GCM, nonce)
    padded = cipher.decrypt_and_verify(data, tag)
    return padded

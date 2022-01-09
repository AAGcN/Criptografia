from base64 import b64decode, b64encode

def otp(data, key):
    out = [(lambda a, b : a ^ b)(*l) for l in zip(data, key)]
    return bytes(out)

def repeatingxor(b, key):
    k = (key * len(b))[0:len(b)]
    return otp(b, k)

m = b"keepcoding"

# de bytes (ascii) a bytes (base64)
m_b64 = b64encode(m)
print(m_b64.decode())

# base64 (bytes) a bytes (ascii)
print(b64decode(m_b64))

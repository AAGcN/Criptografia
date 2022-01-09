def otp(mensaje, k):
    return mensaje ^ k

m = b"keepcoding"
k = b"abcdefghij"

c = m ^ k

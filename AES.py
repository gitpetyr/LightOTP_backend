from hashlib import sha256
import base64
from Crypto.Cipher import AES
import os

'''
AES加密封装
'''

def pad(data: str) -> bytes:
    pad_length = 16 - (len(data) % 16)
    return data.encode('utf-8') + bytes([pad_length] * pad_length)

def unpad(data: bytes) -> str:
    pad_length = data[-1]
    return data[:-pad_length].decode('utf-8')

def encrypt(key: str, data: str) -> str:
    key = sha256(key.encode('utf-8')).digest()[:16]
    cipher = AES.new(key, AES.MODE_ECB)
    padded_data = pad(data)
    ciphertext = cipher.encrypt(padded_data)
    return base64.b64encode(ciphertext).decode('utf-8')

def decrypt(key: str, data: str) -> str:
    key = sha256(key.encode('utf-8')).digest()[:16]
    cipher = AES.new(key, AES.MODE_ECB)
    decoded_data = base64.b64decode(data)
    plaintext = cipher.decrypt(decoded_data)
    return unpad(plaintext)

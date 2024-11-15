from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def adjust_key(key_str, required_bytes=32):
    key_bytes = key_str.encode('utf-8')
    if len(key_bytes) < required_bytes:
        # Agregar bytes aleatorios para completar el tamaño
        extra_bytes = get_random_bytes(required_bytes - len(key_bytes))
        key_bytes += extra_bytes
    elif len(key_bytes) > required_bytes:
        # Truncar la clave
        key_bytes = key_bytes[:required_bytes]
    return key_bytes

def adjust_iv(iv_str, required_bytes=16):
    iv_bytes = iv_str.encode('utf-8')
    if len(iv_bytes) < required_bytes:
        # Agregar bytes aleatorios para completar el tamaño
        extra_bytes = get_random_bytes(required_bytes - len(iv_bytes))
        iv_bytes += extra_bytes
    elif len(iv_bytes) > required_bytes:
        # Truncar el IV
        iv_bytes = iv_bytes[:required_bytes]
    return iv_bytes

def aes_encrypt(plaintext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_text = pad(plaintext.encode('utf-8'), AES.block_size)
    ciphertext = cipher.encrypt(padded_text)
    return ciphertext

def aes_decrypt(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_padded_text = cipher.decrypt(ciphertext)
    decrypted_text = unpad(decrypted_padded_text, AES.block_size)
    return decrypted_text.decode('utf-8')

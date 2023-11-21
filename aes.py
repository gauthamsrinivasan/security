from Crypto.Cipher import AES
import binascii
from Crypto.Util.Padding import pad, unpad  # Added padding functions

key = input("Enter the 16-character encryption key: ").encode('utf-8')

def encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_plaintext = pad(plaintext.encode(), AES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_text = cipher.decrypt(ciphertext)
    unpadded_text = unpad(decrypted_text, AES.block_size)
    return unpadded_text.decode()

message = input("Enter the message to encrypt: ")

encrypted_message = encrypt(message, key)
hex_representation = binascii.hexlify(encrypted_message).decode()
print("Encrypted (hex):", hex_representation)

decrypted_message = decrypt(encrypted_message, key)
print("Decrypted:", decrypted_message)
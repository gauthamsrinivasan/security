from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
import binascii

def des_encrypt(key, plaintext):
    cipher = DES3.new(key, DES3.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def des_decrypt(key, ciphertext):
    cipher = DES3.new(key, DES3.MODE_ECB)
    decrypted_text = cipher.decrypt(ciphertext)
    return decrypted_text

def pad_text(text):
    # Pad the text to be a multiple of 8 bytes (DES block size)
    pad_length = 8 - (len(text) % 8)
    padded_text = text + bytes([pad_length] * pad_length)
    return padded_text

def unpad_text(text):
    # Unpad the text by removing the last byte
    pad_length = text[-1]
    return text[:-pad_length]

if __name__ == "__main__":
    # Generate a random 24-byte (192-bit) key for Triple DES
    key = get_random_bytes(24)

    # Get user input for the message to be encrypted
    message = input("Enter the message to be encrypted: ").encode('utf-8')

    # Pad the message
    padded_message = pad_text(message)

    # Encrypt the message
    encrypted_message = des_encrypt(key, padded_message)
    print("Encrypted (hex):", binascii.hexlify(encrypted_message).decode())

    # Decrypt the message
    decrypted_message = des_decrypt(key, encrypted_message)

    # Unpad the decrypted message and print the result
    unpadded_message = unpad_text(decrypted_message)
    print("Decrypted:", unpadded_message.decode('utf-8'))
import numpy as np

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def matrix_modulo_inverse(matrix, modulo):
    det = int(np.round(np.linalg.det(matrix))) % modulo
    det_inv = modinv(det, modulo)
    matrix_inv = np.round(det_inv * np.linalg.inv(matrix)).astype(int) % modulo
    return matrix_inv

def hill_cipher_encrypt(plain_text, key_matrix, modulo):
    plain_text = [ord(char) - ord('A') for char in plain_text]
    plain_text = np.array(plain_text)

    key_matrix = np.array(key_matrix)

    # Padding the plaintext if its length is not a multiple of the key matrix size
    if len(plain_text) % len(key_matrix) != 0:
        padding_size = len(key_matrix) - len(plain_text) % len(key_matrix)
        plain_text = np.append(plain_text, [0] * padding_size)

    cipher_text = []
    for i in range(0, len(plain_text), len(key_matrix)):
        block = plain_text[i:i+len(key_matrix)]
        encrypted_block = np.dot(key_matrix, block) % modulo
        cipher_text.extend(encrypted_block)

    cipher_text = ''.join([chr(char + ord('A')) for char in cipher_text])
    return cipher_text

def hill_cipher_decrypt(cipher_text, key_matrix, modulo):
    cipher_text = [ord(char) - ord('A') for char in cipher_text]
    cipher_text = np.array(cipher_text)

    key_matrix_inv = matrix_modulo_inverse(key_matrix, modulo)

    plain_text = []
    for i in range(0, len(cipher_text), len(key_matrix)):
        block = cipher_text[i:i+len(key_matrix)]
        decrypted_block = np.dot(key_matrix_inv, block) % modulo
        plain_text.extend(decrypted_block)

    plain_text = ''.join([chr(char + ord('A')) for char in plain_text])
    return plain_text

# Example Usage
if __name__ == "__main__":
    # Key matrix should be a square matrix of size n x n
    key_matrix = [[6, 24, 1], [13, 16, 10], [20, 17, 15]]
    modulo = 26  # Modulo for the arithmetic operations

    plain_text = "HELLOHILL"
    
    # Encryption
    cipher_text = hill_cipher_encrypt(plain_text, key_matrix, modulo)
    print(f"Encrypted Text: {cipher_text}")

    # Decryption
    decrypted_text = hill_cipher_decrypt(cipher_text, key_matrix, modulo)
    print(f"Decrypted Text: {decrypted_text}")

def prepare_text(text):
    # Convert text to uppercase and remove spaces
    text = text.upper().replace(" ", "")
    # Replace 'J' with 'I'
    text = text.replace("J", "I")
    return text

def generate_key_matrix(key):
    # Create a 5x5 matrix and fill it with the key
    key_matrix = [['' for _ in range(5)] for _ in range(5)]
    key = prepare_text(key + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    key = "".join(dict.fromkeys(key))
    key_index = 0

    for i in range(5):
        for j in range(5):
            key_matrix[i][j] = key[key_index]
            key_index += 1

    return key_matrix

def find_position(matrix, char):
    # Find the position of a character in the matrix
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def encrypt_playfair(plaintext, key):
    plaintext = prepare_text(plaintext)
    key_matrix = generate_key_matrix(key)
    ciphertext = ''
    for i in range(0, len(plaintext), 2):
        char1 = plaintext[i]
        char2 = plaintext[i + 1] if i + 1 < len(plaintext) else 'X'

        row1, col1 = find_position(key_matrix, char1)
        row2, col2 = find_position(key_matrix, char2)

        if row1 == row2:
            ciphertext += key_matrix[row1][(col1 + 1) % 5]
            ciphertext += key_matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += key_matrix[(row1 + 1) % 5][col1]
            ciphertext += key_matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += key_matrix[row1][col2]
            ciphertext += key_matrix[row2][col1]

    return ciphertext

def decrypt_playfair(ciphertext, key):
    ciphertext = prepare_text(ciphertext)
    key_matrix = generate_key_matrix(key)
    print("Key Matrix : ")
    for row in key_matrix:
        print(row)
    plaintext = ''
    for i in range(0, len(ciphertext), 2):
        char1 = ciphertext[i]
        char2 = ciphertext[i + 1] if i + 1 < len(ciphertext) else 'X'

        row1, col1 = find_position(key_matrix, char1)
        row2, col2 = find_position(key_matrix, char2)

        if row1 == row2:
            plaintext += key_matrix[row1][(col1 - 1) % 5]
            plaintext += key_matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += key_matrix[(row1 - 1) % 5][col1]
            plaintext += key_matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += key_matrix[row1][col2]
            plaintext += key_matrix[row2][col1]

    return plaintext

# Example usage:
plaintext = "Hello earth"
key = "KEYWORD"
encrypted_text = encrypt_playfair(plaintext, key)
decrypted_text = decrypt_playfair(encrypted_text, key)

print("Plaintext:", plaintext)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)

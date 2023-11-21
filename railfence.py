def encrypt_rail_fence(plain_text, rails):
    rail_fence = ['' for _ in range(rails)]
    direction = 1  # 1 for down, -1 for up
    row = 0

    for char in plain_text:
        rail_fence[row] += char
        row += direction

        if row == 0 or row == rails - 1:
            direction = -direction

    cipher_text = ''.join(rail_fence)
    return cipher_text

def decrypt_rail_fence(cipher_text, rails):
    rail_fence = [[''] * len(cipher_text) for _ in range(rails)]
    direction = 1  # 1 for down, -1 for up
    row, col = 0, 0

    for char in cipher_text:
        rail_fence[row][col] = 'X'  # Use a placeholder character to mark the positions of the characters in the rail fence
        col += 1
        row += direction

        if row == 0 or row == rails - 1:
            direction = -direction

    index = 0
    for i in range(rails):
        for j in range(len(cipher_text)):
            if rail_fence[i][j] == 'X':
                rail_fence[i][j] = cipher_text[index]
                index += 1

    decrypted_text = ''
    direction = 1
    row = 0

    for _ in range(len(cipher_text)):
        decrypted_text += rail_fence[row][0]
        rail_fence[row] = rail_fence[row][1:]
        row += direction

        if row == 0 or row == rails - 1:
            direction = -direction

    return decrypted_text

# Example usage:
plain_text = "HELLOWORLD"
rails = 2

# Encryption
cipher_text = encrypt_rail_fence(plain_text, rails)
print(f"Encrypted text: {cipher_text}")

# Decryption
decrypted_text = decrypt_rail_fence(cipher_text, rails)
print(f"Decrypted text: {decrypted_text}")
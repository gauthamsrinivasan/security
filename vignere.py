def vigenere_encrypt(plain_text, key):
    # Convert the key to uppercase
    key = key.upper()
    
    # Initialize an empty string to store the cipher text
    cipher_text = ""

    # Loop through each character in the plain text
    for i in range(len(plain_text)):
        # Get the current character in the plain text
        char = plain_text[i]

        # Check if the character is an alphabet letter
        if char.isalpha():
            # Determine the corresponding key character
            key_char = key[i % len(key)]

            # Convert both the plain text and key characters to uppercase
            char = char.upper()
            key_char = key_char.upper()

            # Encrypt the current character using the Vigenère cipher formula
            encrypted_char = chr(((ord(char) + ord(key_char) - 2 * ord('A')) % 26) + ord('A'))

            # Append the encrypted character to the cipher text
            cipher_text += encrypted_char
        else:
            # If the character is not an alphabet letter, keep it unchanged
            cipher_text += char

    return cipher_text

def vigenere_decrypt(cipher_text, key):
    # Convert the key to uppercase
    key = key.upper()
    
    # Initialize an empty string to store the decrypted text
    decrypted_text = ""

    # Loop through each character in the cipher text
    for i in range(len(cipher_text)):
        # Get the current character in the cipher text
        char = cipher_text[i]

        # Check if the character is an alphabet letter
        if char.isalpha():
            # Determine the corresponding key character
            key_char = key[i % len(key)]

            # Convert both the cipher text and key characters to uppercase
            char = char.upper()
            key_char = key_char.upper()

            # Decrypt the current character using the Vigenère cipher formula
            decrypted_char = chr(((ord(char) - ord(key_char) + 26) % 26) + ord('A'))

            # Append the decrypted character to the decrypted text
            decrypted_text += decrypted_char
        else:
            # If the character is not an alphabet letter, keep it unchanged
            decrypted_text += char

    return decrypted_text

# Example usage:
plain_text = "HELLO"
key = "KEY"

cipher_text = vigenere_encrypt(plain_text, key)
print("Encrypted:", cipher_text)

decrypted_text = vigenere_decrypt(cipher_text, key)
print("Decrypted:", decrypted_text)

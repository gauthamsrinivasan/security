def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            is_upper = char.isupper()
            
            # Shift the character within the range of its case (uppercase or lowercase)
            char_code = ord(char)
            shifted_code = (char_code - ord('A' if is_upper else 'a') + shift) % 26
            new_char = chr(shifted_code + ord('A' if is_upper else 'a'))

            result += new_char
        else:
            # If the character is not a letter, leave it unchanged
            result += char

    return result
def caesar_decipher(result, shift):
    plain = ""

    for char in result:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            is_upper = char.isupper()
            
            # Shift the character within the range of its case (uppercase or lowercase)
            char_code = ord(char)
            shifted_code = (char_code - ord('A' if is_upper else 'a') - shift) % 26
            if shifted_code<0:
                shifted_code=shifted_code+26
            new_char = chr(shifted_code + ord('A' if is_upper else 'a'))

            plain += new_char
        else:
            # If the character is not a letter, leave it unchanged
            plain += char

    return plain


# Example usage:
plaintext = "zacmldkp"
shift_amount = 3
encrypted_text = caesar_cipher(plaintext, shift_amount)
decrypted_text = caesar_decipher(encrypted_text, shift_amount)
print("Original text:", plaintext)
print("Encrypted text:", encrypted_text)
print("Decrypted Text:",decrypted_text )

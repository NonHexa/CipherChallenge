def vigenere_decrypt(ciphertext, key):
    """
    Decrypt a Vigenère cipher with the provided key.

    :param ciphertext: The encrypted text
    :param key: The key used for decryption
    :return: Decrypted plaintext
    """
    plaintext = []
    key = key.lower()
    key_length = len(key)
    key_index = 0

    for char in ciphertext:
        if char.isalpha():  # Process only alphabetic characters
            shift = ord(key[key_index]) - ord('a')
            if char.islower():
                decrypted_char = chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
            else:  # Uppercase
                decrypted_char = chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
            plaintext.append(decrypted_char)
            key_index = (key_index + 1) % key_length  # Cycle through the key
        else:
            plaintext.append(char)  # Non-alphabetic characters are not encrypted

    return ''.join(plaintext)

# Example usage:
ciphertext = input("Enter Text:")
key = "Charles"
plaintext = vigenere_decrypt(ciphertext, key)
print("Decrypted plaintext:", plaintext)

from collections import Counter
import string

def find_repeats(sequence, min_length=3):
    """Finds repeated substrings in the sequence that may indicate the key length."""
    repeats = {}
    for length in range(min_length, len(sequence) // 2):
        seen_substrings = {}
        for i in range(len(sequence) - length):
            substring = sequence[i:i+length]
            if substring in seen_substrings:
                if substring not in repeats:
                    repeats[substring] = []
                repeats[substring].append(i - seen_substrings[substring])
            seen_substrings[substring] = i
    return repeats

def kasiski_analysis(ciphertext, max_key_length=20):
    """Applies the Kasiski examination to guess the key length."""
    repeats = find_repeats(ciphertext)
    spacings = []
    for positions in repeats.values():
        spacings.extend(positions)
    
    if not spacings:
        return 1  # fallback if no patterns are found
    
    key_length_guesses = gcd(spacings)
    if key_length_guesses < 1 or key_length_guesses > max_key_length:
        return min(max_key_length, len(ciphertext))  # limit max key length
    return key_length_guesses

def gcd(numbers):
    """Calculates the greatest common divisor for a list of numbers."""
    from math import gcd
    from functools import reduce
    return reduce(gcd, numbers)

def frequency_score(text):
    """Calculates a score based on the frequency of common English letters."""
    english_freq = {
        'E': 12.7, 'T': 9.1, 'A': 8.2, 'O': 7.5, 'I': 7.0,
        'N': 6.7, 'S': 6.3, 'H': 6.1, 'R': 6.0, 'D': 4.3,
        'L': 4.0, 'C': 2.8, 'U': 2.8, 'M': 2.4, 'W': 2.4,
        'F': 2.2, 'G': 2.0, 'Y': 2.0, 'P': 1.9, 'B': 1.5,
        'V': 1.0, 'K': 0.8, 'X': 0.2, 'J': 0.2, 'Q': 0.1, 'Z': 0.1
    }
    score = sum(english_freq.get(letter, 0) for letter in text.upper())
    return score

def decrypt_caesar(text, shift):
    """Decrypts a text using Caesar shift."""
    decrypted_text = []
    for char in text:
        if char in string.ascii_uppercase:
            decrypted_text.append(chr((ord(char) - shift - 65) % 26 + 65))
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)

def decrypt_with_key(ciphertext, key):
    """Decrypts the ciphertext using the provided Vigenère key."""
    decrypted_text = []
    key_repeats = (len(ciphertext) // len(key)) + 1
    full_key = (key * key_repeats)[:len(ciphertext)]
    
    for c, k in zip(ciphertext, full_key):
        if c in string.ascii_uppercase:
            shift = ord(k) - 65
            decrypted_text.append(chr((ord(c) - shift - 65) % 26 + 65))
        else:
            decrypted_text.append(c)
    return ''.join(decrypted_text)

def vigenere_crack(ciphertext, max_key_length=20):
    """Attempts to decrypt Vigenère cipher by trying different key lengths and analyzing letter frequencies."""
    ciphertext = ''.join(filter(str.isalpha, ciphertext)).upper()
    best_decrypted_text = ""
    best_score = -float('inf')
    probable_key = ""

    for key_length in range(1, max_key_length + 1):
        current_key = ''
        for i in range(key_length):
            segment = ciphertext[i::key_length]
            max_score = -float('inf')
            best_shift = 0

            for shift in range(26):
                decrypted_segment = decrypt_caesar(segment, shift)
                score = frequency_score(decrypted_segment)

                if score > max_score:
                    max_score = score
                    best_shift = shift

            current_key += chr(best_shift + 65)
        
        decrypted_text = decrypt_with_key(ciphertext, current_key)
        total_score = frequency_score(decrypted_text)

        if total_score > best_score:
            best_score = total_score
            best_decrypted_text = decrypted_text
            probable_key = current_key

    return best_decrypted_text, probable_key

# Main Program
if __name__ == "__main__":
    ciphertext = input("Enter the ciphertext to be decoded: ")
    decrypted_text, probable_key = vigenere_crack(ciphertext)
    print(f"Decrypted Text: {decrypted_text}")
    print(f"Probable Key: {probable_key}")
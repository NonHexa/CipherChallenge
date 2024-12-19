from itertools import permutations
from collections import Counter
import string
from math import gcd
from functools import reduce

# Polybius Square Decoder
def polybius_decode(encoded_text, table, row_labels):
    """
    Decodes a Polybius square encoded text using a given table.
    """
    if len(encoded_text) % 2 != 0:
        raise ValueError("Encoded text length must be even (pairs of characters).")
    
    output = ""
    for i in range(0, len(encoded_text), 2):
        try:
            row = int(encoded_text[i]) - 1  # Convert to 0-based index
            col = row_labels.index(encoded_text[i + 1])  # Find the column index
            output += table[row][col]
        except (ValueError, IndexError):
            output += "?"  # Placeholder for invalid pairs
    return output

# Vigenère Cipher Solver
def find_repeats(sequence, min_length=3):
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

def kasiski_analysis(ciphertext):
    repeats = find_repeats(ciphertext)
    spacings = []
    for positions in repeats.values():
        spacings.extend(positions)
    
    if not spacings:
        return None

    return reduce(gcd, spacings) if len(spacings) > 1 else spacings[0]

def index_of_coincidence(text):
    n = len(text)
    freqs = Counter(text)
    return sum(freq * (freq - 1) for freq in freqs.values()) / (n * (n - 1)) if n > 1 else 0

def estimate_key_length_by_ioc(ciphertext, max_length=20):
    ioc_threshold = 0.065
    best_key_length = 1
    closest_ioc = 0

    for key_length in range(1, max_length + 1):
        segments = [''.join(ciphertext[i::key_length]) for i in range(key_length)]
        avg_ioc = sum(index_of_coincidence(segment) for segment in segments) / key_length

        if abs(avg_ioc - ioc_threshold) < abs(closest_ioc - ioc_threshold):
            closest_ioc = avg_ioc
            best_key_length = key_length

    return best_key_length

def frequency_score(text):
    english_freq = {
        'E': 12.7, 'T': 9.1, 'A': 8.2, 'O': 7.5, 'I': 7.0,
        'N': 6.7, 'S': 6.3, 'H': 6.1, 'R': 6.0, 'D': 4.3,
        'L': 4.0, 'C': 2.8, 'U': 2.8, 'M': 2.4, 'W': 2.4,
        'F': 2.2, 'G': 2.0, 'Y': 2.0, 'P': 1.9, 'B': 1.5,
        'V': 1.0, 'K': 0.8, 'X': 0.2, 'J': 0.2, 'Q': 0.1, 'Z': 0.1
    }
    score = 0
    text = text.upper()
    for letter in text:
        if letter in english_freq:
            score += english_freq[letter]
    return score

def decrypt_caesar(text, shift):
    decrypted_text = []
    for char in text:
        if char in string.ascii_uppercase:
            decrypted_text.append(chr((ord(char) - shift - 65) % 26 + 65))
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)

def decrypt_with_key(ciphertext, key):
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

def vigenere_crack(ciphertext):
    ciphertext = ''.join(filter(str.isalpha, ciphertext)).upper()
    kasiski_guess = kasiski_analysis(ciphertext)
    ioc_guess = estimate_key_length_by_ioc(ciphertext)
    key_lengths = {kasiski_guess, ioc_guess}
    key_lengths.update(range(max(1, ioc_guess - 2), ioc_guess + 3))
    key_lengths = sorted(filter(None, key_lengths))

    best_decryption = ""
    best_key = ""
    best_score = -float("inf")

    for key_length in key_lengths:
        probable_key = ''
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
            
            probable_key += chr(best_shift + 65)

        decrypted_text = decrypt_with_key(ciphertext, probable_key)
        decryption_score = frequency_score(decrypted_text)
        
        if decryption_score > best_score:
            best_score = decryption_score
            best_decryption = decrypted_text
            best_key = probable_key

    return best_decryption, best_key

# Main Program
if __name__ == "__main__":
    # Define the Polybius table
    polybius_table = [
        ["a", "f", "k", "p", "u"],
        ["b", "g", "l", "q", "v"],
        ["c", "h", "m", "r", "w"],
        ["d", "i", "n", "s", "x"],
        ["e", "j", "o", "t", "y"]
    ]

    # Input for Polybius Square
    encoded_text = input("Enter the Polybius-encoded text: ")

    best_decryption = ""
    best_key = ""
    best_score = -float("inf")
    best_row_labels = []

    # Generate all permutations of the row labels
    for row_labels_perm in permutations("12345"):
        row_labels = list(row_labels_perm)
        try:
            decoded_polybius = polybius_decode(encoded_text, polybius_table, row_labels)
            decrypted_text, probable_key = vigenere_crack(decoded_polybius)
            score = frequency_score(decrypted_text)

            if score > best_score:
                best_score = score
                best_decryption = decrypted_text
                best_key = probable_key
                best_row_labels = row_labels
        except ValueError:
            continue

    print(f"Best Polybius row labels: {''.join(best_row_labels)}")
    print(f"Vigenère Decrypted Text: {best_decryption}")
    print(f"Probable Key: {best_key}")

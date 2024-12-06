import cipher
from collections import Counter
import math
import random
result = cipher.substitution(
    input("Input ciphertext: "),
    int(input("Input brute precision (0 for unspecified): ")),
    input("Input any cribs in form (a,b,c): "),
    input("Spaces or no spaces (t/f): ")
)
print(result)
#babbage,dear,lovelace,charles,silver,bullet,cipher,transposition,substitution,letter,kate,warne
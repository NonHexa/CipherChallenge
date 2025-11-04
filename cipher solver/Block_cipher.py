import cipher

def get_input_once():
    ciphertext = input("Input ciphertext: ").strip()
    max_block_len = int(input("Input number of max_block_len (0 for unspecified): "))
    crib = input("Input any cribs in form (a,b,c): ").strip()
    spaces = input("Spaces or no spaces (t/f): ").strip()
    brute_precision = int(input("Input brute precision (0 for unspecified): "))
    return ciphertext, max_block_len, crib, spaces, brute_precision

def main():
    try:
        # Get input once
        ciphertext, max_block_len, crib, spaces, brute_precision = get_input_once()
        
        # Run the solver
        result = cipher.block_permutation_transposition(ciphertext, max_block_len, crib, spaces, brute_precision)
        
        # Print result
        print("\nDecrypted text:")
        print(result)
        
    except ValueError as e:
        print(f"Error: {e}")
        
if __name__ == "__main__":
    main()
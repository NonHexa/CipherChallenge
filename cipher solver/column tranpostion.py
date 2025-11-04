import cipher

def get_input_once():
    ciphertext = input("Input ciphertext: ").strip()
    columns = int(input("Input number of columns (0 for unspecified): "))
    cribs = input("Input any cribs in form (a,b,c): ").strip()
    spaces = input("Spaces or no spaces (t/f): ").strip()
    brute_precision = int(input("Input brute precision (0 for unspecified): "))
    return ciphertext, columns, cribs, spaces, brute_precision

def main():
    try:
        # Get input once
        ciphertext, columns, cribs, spaces, brute_precision = get_input_once()
        
        # Run the solver
        result = cipher.columnar_transposition(ciphertext, columns, cribs, spaces, brute_precision)
        
        # Print result
        print("\nDecrypted text:")
        print(result)
        
    except ValueError as e:
        print(f"Error: {e}")
        
if __name__ == "__main__":
    main()
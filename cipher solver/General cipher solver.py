import cipher
import time
while True:

    userinput=input(">").lower()
    if userinput == "quit":
        break
    elif userinput== "help":
        print('''caesar - ceasar cipher
                 english - english detector 
                 bruteforce - try everything
                 quit - to exit''')
        

    else:
        print("Invalid selection")

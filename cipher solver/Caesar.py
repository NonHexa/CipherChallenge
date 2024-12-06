import cipher
import time
print("______________________________________________")
message=input("Enter text: ").lower()
brute_precision=int(input("How close to standard english should the text be?(1 to 100) "))
print("______________________________________________")
print(f"Output:\n{cipher.caesar_shift(message,brute_precision)}")
time.sleep(9999)



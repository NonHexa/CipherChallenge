import random
chars="abcdefghijklmnopqrstuvwxyz"
output=""
for i in range(0,int(input("How many characters: "))):
               output+=chars[random.randint(0,25)]
print("Output: "+output)

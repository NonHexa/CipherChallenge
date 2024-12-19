WORDS = ["carol", "angel", "reindeer", "christmas", "bells", "holly", "elf", "snowball", "candycane", "cocoa", "tinsel", "frost", "wreath", "gingerbread", "nutcracker", "sleigh", "cookie", "holly", "mistletoe"]
HANGMAN_PICS = ['''
     *
    /.\\
   /..'\\
  /.''.'\\
  /.'.'.\\
 /'.''.'.\\
 ^^^[_]^^^
''', '''

    /.\\
   /..'\\
  /.''.'\\
  /.'.'.\\
 /'.''.'.\\
 ^^^[_]^^^''', '''


   /..'\\
  /.''.'\\
  /.'.'.\\
 /'.''.'.\\
 ^^^[_]^^^''', '''



  /.''.'\\
  /.'.'.\\
 /'.''.'.\\
 ^^^[_]^^^''', '''




  /.'.'.\\
 /'.''.'.\\
 ^^^[_]^^^''', '''





 /'.''.'.\\
 ^^^[_]^^^''', '''






    [_]''']
import random
num = random.randint(0,20)
word = WORDS[num]
l = len(word)
i = 0
guesses = 1
g = []
while True:
    print(HANGMAN_PICS[i])
    guess = input("Guess a letter")
    if guess in word:
        if guesses == l:
            print("Welldone")
            print(word)
        else:
            print("welldone")
            guesses += 1
            g.append(guess)
            print(g)
            
    else:
        if i == 6:
            print("fail")
            break
        else:
            print("try again")
            i += 1
            print(g)
        
        
        





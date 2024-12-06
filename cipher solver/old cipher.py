def caesar_shift(message,brute_precision):
    from cipher import english_detect
    letters_caesar='abcdefghijklmnopqrstuvwxyz'
    output_brute=""
    for i in range(26):
        output_caesar=''
        for letter in message:
            if letter not in letters_caesar:
                output_caesar += letter
            else:
                index=(letters_caesar.find(letter))
                shifted_index= (index + i) % len(letters_caesar)
                output_caesar += letters_caesar[shifted_index]
        if english_detect(output_caesar,brute_precision):
            output_brute += f"{i + 1}: {output_caesar}\n"
    return output_brute


def english_detect(message,precision_percentage):
    english_percentage_dict={ "th": 2.9,
    "he": 2.48,
    "in": 1.87,
    "er": 1.73,
    "an": 1.65,
    "re": 1.38,
    "es": 1.35,
    "st": 1.19,
    "on": 1.17,
    "nd": 1.14,
    "en": 1.13,
    "at": 1.08,
    "nt": 1.08,
    "ed": 1.04,
    "ea": 1.01,
    "to": 1.0,
    "or": 0.96,
    "ti": 0.96,
    "ha": 0.94,
    "ar": 0.89,
    "ng": 0.89,
    "is": 0.89,
    "it": 0.88,
    "te": 0.88,
    "ou": 0.85,
    "et": 0.84,
    "of": 0.82,
    "al": 0.82,
    "as": 0.8,
    "le": 0.74,
    "se": 0.73,
    "hi": 0.72,
    "sa": 0.68,
    "ra": 0.64,
    "ro": 0.64,
    "ne": 0.64,
    "ve": 0.63,
    "me": 0.62,
    "ri": 0.62,
    "so": 0.6,
    "de": 0.59,
    "ll": 0.58,
    "ta": 0.58,
    "li": 0.57,
    "si": 0.57,
    "el": 0.55,
    "ec": 0.52,
    "co": 0.52,
    "no": 0.52,
    "ot": 0.51,
    "ma": 0.5,
    "di": 0.5,
    "ic": 0.49,
    "la": 0.49,
    "ho": 0.49,
    "om": 0.48,
    "tt": 0.48,
    "na": 0.48,
    "sh": 0.47,
    "ch": 0.46,
    "be": 0.46,
    "ss": 0.46,
    "rt": 0.46,
    "ee": 0.45,
    "em": 0.45,
    "ns": 0.44,
    "rs": 0.44,
    "ce": 0.43,
    "ur": 0.42,
    "ei": 0.41,
    "ca": 0.41,
    "io": 0.41,
    "ac": 0.4,
    "ts": 0.4,
    "da": 0.39,
    "lo": 0.39,
    "us": 0.39,
    "wa": 0.38,
    "ni": 0.38,
    "dt": 0.38,
    "pe": 0.38,
    "fo": 0.38,
    "ew": 0.37,
    "ut": 0.37,
    "wi": 0.36,
    "il": 0.36,
    "eo": 0.36,
    "ly": 0.36,
    "wh": 0.36,
    "ad": 0.35,
    "un": 0.34,
    "ow": 0.34,
    "tr": 0.34,
    "nc": 0.33,
    "ft": 0.33,
    "do": 0.32,
    "ge": 0.32,
    "ep": 0.32,
    "mo": 0.32,
    "we": 0.31}
    freq_dict = {}
    message=message.lower()
    for i in range(1, len(message)):
        bigram = message[i-1:i+1]
        if bigram in freq_dict:
            freq_dict[bigram] += 1
        else:
            freq_dict[bigram] = 1
    total_bigrams=0
    for i in freq_dict:
        total_bigrams+=freq_dict.get(i)
    percentage_dict={}
    for i in freq_dict:
        percentage_dict[i]=(freq_dict.get(i)/total_bigrams*100)
    precision=0
    for i in english_percentage_dict:
        if percentage_dict.get(i) is not None and (english_percentage_dict.get(i)-0.5) <= percentage_dict.get(i,0) <= (english_percentage_dict.get(i)+0.5):
            precision += 1
        else:
            pass
    if precision >= precision_percentage:
        return True
    else:
        return False

def english_detect_numVar(message,crib,spaces):
    english_percentage_dict={ "th": 2.9,
    "he": 2.48,
    "in": 1.87,
    "er": 1.73,
    "an": 1.65,
    "re": 1.38,
    "es": 1.35,
    "st": 1.19,
    "on": 1.17,
    "nd": 1.14,
    "en": 1.13,
    "at": 1.08,
    "nt": 1.08,
    "ed": 1.04,
    "ea": 1.01,
    "to": 1.0,
    "or": 0.96,
    "ti": 0.96,
    "ha": 0.94,
    "ar": 0.89,
    "ng": 0.89,
    "is": 0.89,
    "it": 0.88,
    "te": 0.88,
    "ou": 0.85,
    "et": 0.84,
    "of": 0.82,
    "al": 0.82,
    "as": 0.8,
    "le": 0.74,
    "se": 0.73,
    "hi": 0.72,
    "sa": 0.68,
    "ra": 0.64,
    "ro": 0.64,
    "ne": 0.64,
    "ve": 0.63,
    "me": 0.62,
    "ri": 0.62,
    "so": 0.6,
    "de": 0.59,
    "ll": 0.58,
    "ta": 0.58,
    "li": 0.57,
    "si": 0.57,
    "el": 0.55,
    "ec": 0.52,
    "co": 0.52,
    "no": 0.52,
    "ot": 0.51,
    "ma": 0.5,
    "di": 0.5,
    "ic": 0.49,
    "la": 0.49,
    "ho": 0.49,
    "om": 0.48,
    "tt": 0.48,
    "na": 0.48,
    "sh": 0.47,
    "ch": 0.46,
    "be": 0.46,
    "ss": 0.46,
    "rt": 0.46,
    "ee": 0.45,
    "em": 0.45,
    "ns": 0.44,
    "rs": 0.44,
    "ce": 0.43,
    "ur": 0.42,
    "ei": 0.41,
    "ca": 0.41,
    "io": 0.41,
    "ac": 0.4,
    "ts": 0.4,
    "da": 0.39,
    "lo": 0.39,
    "us": 0.39,
    "wa": 0.38,
    "ni": 0.38,
    "dt": 0.38,
    "pe": 0.38,
    "fo": 0.38,
    "ew": 0.37,
    "ut": 0.37,
    "wi": 0.36,
    "il": 0.36,
    "eo": 0.36,
    "ly": 0.36,
    "wh": 0.36,
    "ad": 0.35,
    "un": 0.34,
    "ow": 0.34,
    "tr": 0.34,
    "nc": 0.33,
    "ft": 0.33,
    "do": 0.32,
    "ge": 0.32,
    "ep": 0.32,
    "mo": 0.32,
    "we": 0.31}
    freq_dict = {}
    message=message.lower()
    for i in range(1, len(message)):
        bigram = message[i-1:i+1]
        if bigram in freq_dict:
            freq_dict[bigram] += 1
        else:
            freq_dict[bigram] = 1
    total_bigrams=0
    for i in freq_dict:
        total_bigrams+=freq_dict.get(i)
    percentage_dict={}
    for i in freq_dict:
        percentage_dict[i]=(freq_dict.get(i)/total_bigrams*100)
    precision=0
    for i in english_percentage_dict:
        if percentage_dict.get(i) is not None and (english_percentage_dict.get(i)-0.5) <= percentage_dict.get(i,0) <= (english_percentage_dict.get(i)+0.5):
            precision += 1
        if crib.count(message) >1:
            precision+=(crib.count(message)*200)
        if spaces=="f":    
            with open("Oxford 3000 Word List No Spaces.txt") as f:
                words=f.read
                for line in f:
                    sLine = line.strip()
                    if len(sLine) < 4:
                        continue
                    if message.find(sLine) >= 0:
                        print(line)
                        precision+=3
                        print(precision)
        else: 
            with open("Oxford 3000 Word List.txt") as f:
                words=f.read
                for line in f:
                    sLine = line.strip()
                    if len(sLine) < 4:
                        continue
                    if message.find(sLine) >= 0:
                        print(line)
                        precision+=3
                        print(precision)
    return precision

def columnar_transposition():
    pass

def sub_decrypt(message,key):
        chars="abcdefghijklmnopqrstuvwxyz"
        message=message.upper()
        for i in range(len(chars)):
            message=message.replace(chars[i].upper(),key[i].lower())
        return message


def substitution(ciphertext,brute_precision,crib,spaces):
    import random
    import time
    solved=False
    crib_list=crib.split(",")
    chars="abcdefghijklmnopqrstuvwxyz"
    key_old=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    key_new=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    key_old_score=0
    key_new_score=0
    while not solved:
        ranA=random.randint(0,len(chars)-1)
        ranB=random.randint(0,len(chars)-1)
        swapA=key_new[ranA]
        swapB=key_new[ranB]
        key_new[ranA], key_new[ranB] = key_new[ranB], key_new[ranA]
        print("".join(key_new))
        if key_old_score>key_new_score:
            key_new=key_old
        plaintext=ciphertext.upper()
        for i in range(len(chars)):
            plaintext=plaintext.replace(chars[i].upper(),key_new[i].lower())
            plaintext_str=''.join(plaintext)
        if english_detect_numVar(plaintext_str,crib_list,spaces)>=brute_precision:
            solved=True
            return plaintext_str
        else:
            key_old_score=key_new_score
            key_new_score=english_detect_numVar(plaintext_str,crib_list,spaces)
        



def space_remover():
    pass
    
def text_reverser():
    pass

def vigenere():
    pass



result=substitution(input("Input ciphertext"),int(input("Input brute precision")),input("Input any cribs in form (a,b,c)"),input("Spaces or no spaces t/f"))
print(result)
#babbage,kate,warne,dear,mrs,silver,bullet
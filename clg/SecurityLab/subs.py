# Substitution Cipher
from string import ascii_lowercase

all_letters= ascii_lowercase

def convert(input_txt, key):
    output_txt=''
    for char in input_txt:
        if char in all_letters:
            index = all_letters.index(char)
            # for encryption
            output_txt+=all_letters[(index + key) % 26]
            # for decryption
            # output_txt+=all_letters[(index - key) % 26] 
        else:
            output_txt+=char
    return output_txt

key = 4

input_txt= "i am studying data encryption"
# input_txt = input("Enter String")
input_txt=input_txt.lower()
print(convert(input_txt,key))
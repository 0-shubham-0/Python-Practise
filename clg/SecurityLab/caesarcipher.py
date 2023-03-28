from string import ascii_lowercase

ALPHABET = ascii_lowercase
ALPHABET_SIZE = len(ALPHABET)

new_frequency = {'e': 0, 't': 0, 'a': 0, 'o': 0, 'i': 0, 'n': 0, 's': 0, 'h': 0,
                 'r': 0, 'd': 0, 'l': 0, 'c': 0, 'u': 0, 'm': 0, 'w': 0, 'f': 0,
                 'g': 0, 'y': 0, 'p': 0, 'b': 0, 'v': 0, 'k': 0, 'j': 0, 'x': 0,
                 'q': 0, 'z': 0}


def get_dict_key(val, dict):
    for key, value in dict.items():
        if val == value:
            return key
    return "key doesn't exist"


def get_cipher_key(freq: dict):
    highest_freq_letter = get_dict_key(max(freq.values()), freq)
    # print("letter which has highest frequency ", highest_freq_letter)
    index = ALPHABET.index(highest_freq_letter.lower())
    # print(index)
    key = index - 4 % ALPHABET_SIZE
    # print(key)
    return key


def pop_max(freq: dict):
    val = max(freq.values())
    dict_key = get_dict_key(val, freq)
    freq.pop(dict_key)


def createFrequency(text: str):
    for char in text:
        if char in ALPHABET:
            if char.lower() == 'a': new_frequency['a'] += 1
            if char.lower() == 'b': new_frequency['b'] += 1
            if char.lower() == 'c': new_frequency['c'] += 1
            if char.lower() == 'd': new_frequency['d'] += 1
            if char.lower() == 'e': new_frequency['e'] += 1
            if char.lower() == 'f': new_frequency['f'] += 1
            if char.lower() == 'g': new_frequency['g'] += 1
            if char.lower() == 'h': new_frequency['h'] += 1
            if char.lower() == 'i': new_frequency['i'] += 1
            if char.lower() == 'j': new_frequency['j'] += 1
            if char.lower() == 'k': new_frequency['k'] += 1
            if char.lower() == 'l': new_frequency['l'] += 1
            if char.lower() == 'm': new_frequency['m'] += 1
            if char.lower() == 'n': new_frequency['n'] += 1
            if char.lower() == 'o': new_frequency['o'] += 1
            if char.lower() == 'p': new_frequency['p'] += 1
            if char.lower() == 'q': new_frequency['q'] += 1
            if char.lower() == 'r': new_frequency['r'] += 1
            if char.lower() == 's': new_frequency['s'] += 1
            if char.lower() == 't': new_frequency['t'] += 1
            if char.lower() == 'u': new_frequency['u'] += 1
            if char.lower() == 'v': new_frequency['v'] += 1
            if char.lower() == 'w': new_frequency['w'] += 1
            if char.lower() == 'x': new_frequency['x'] += 1
            if char.lower() == 'y': new_frequency['y'] += 1
            if char.lower() == 'z': new_frequency['z'] += 1


def cipher(text: str, key: int, decrypt: bool) -> str:
    output = ''

    for char in text:
        # If the character is not in the english alphabet don't change it.
        if char not in ALPHABET:
            output += char
            continue

        index = ALPHABET.index(char.lower())

        if decrypt:
            new_char = ALPHABET[(index - key) % ALPHABET_SIZE]
        else:
            new_char = ALPHABET[(index + key) % ALPHABET_SIZE]

        # Setting the right case for the letter and adding it to the output
        output += new_char.upper() if char.isupper() else new_char

    return output


# get encrypted/cipher text
cipher_text = input("Enter String")
# create dictionary of the input text
createFrequency(cipher_text)
for i in range(25):
    key = get_cipher_key(new_frequency)
    print(cipher(cipher_text, key, True))
    isCorrect = input("Enter y if correct")
    if isCorrect == 'y':
        break
    pop_max(new_frequency)

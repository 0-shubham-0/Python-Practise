def encryptMessage(key, message):
    ciphertext = []

    for col in range(key):
        pointer = col
        while pointer < len(message):
            ciphertext.append(message[pointer])
            pointer += key

    return ''.join(ciphertext)

myMessage = 'Common sense is not so common.'
myKey = 4
ciphertext = encryptMessage(myKey, myMessage)

print(ciphertext)
sentence = 'hello there hi my name is      rim'
count = 1
for i in range(len(sentence)):
    if sentence[i] == ' ' and sentence[i + 1] != ' ':
        count += 1
print(count)
# print(len(sentence.split()))

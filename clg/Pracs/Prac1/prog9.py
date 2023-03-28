sentence = 'hello the there hi my name is  the    rim'
a = sentence.split()
count = 0
for i in a:
    if i == 'the':
        count += 1
print(count)

# declare one list of names ask user to enter  name to be searched compare the name
names = ['bell', 'mark', 'dark', 'lark', 'park', 'mark']
username = input('Whats your name ?')
count = 0
listlen = 0
ind = []
for name in names:
    listlen += 1
    if name == username:
        count += 1
        ind.append(listlen)

if count > 0:
    print("name is present in the list for", count, "number of times")
    print("at ", ind)
else:
    print(username, "is not present in the list")

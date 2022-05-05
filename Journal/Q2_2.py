names = ['bell', 'mark', 'dark', 'lark', 'park', 'mark']
username = input('Whats your name? ').lower()
count = 0
list_len = 0
ind = []
for name in names:
    list_len += 1
    if name == username:
        count += 1
        ind.append(list_len)

if count > 0:
    print(f"Name {username} is present in the list for", count, "number of times", end=' ')
    print("at", ind)
else:
    print(username, "is not present in the list")

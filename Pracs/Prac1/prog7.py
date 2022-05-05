n = [12, 3, 2, 5]
for j in range(len(n)):
    for i in range(1, (len(n)) - j):
        if n[i] < n[i - 1]:
            t = n[i]
            n[i] = n[i - 1]
            n[i - 1] = t
print(n)

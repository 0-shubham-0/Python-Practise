n = [12, 3, 2, 5]
print(n)
# Sorting algo
for j in range(len(n)):
    for i in range(1, (len(n)) - j):
        if n[i] < n[i - 1]:
            t = n[i]
            n[i] = n[i - 1]
            n[i - 1] = t
ans = int(input("press 1 for ascending order and, press 2 for descending order : "))
if ans == 1:
    print(n)
elif ans == 2:
    n.reverse()
    print(n)

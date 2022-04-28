l = [10, 99, 1, 2, 3, 4, 5, 2, 3, 7]
print(l)

l.append(10)
print(l)

p = l.copy()
print(p)

p.clear()
print(p)

print(l.count(3))
l.pop()
print("popped")
print(l)

l.pop(2)
print("popped index 2")
print(l)

print(l.index(3))
h = "jo"
print(h)
h.capitalize()
print(h.index('j', 0, 1))
extend = [10, 12]
l.extend(extend)
print(l)

l.remove(2)
print(l)

l.sort()
print(l)

l.reverse()
print(l)

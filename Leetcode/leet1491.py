n=len(salary)
salary.sort()
sum = 0
for s in range(n):
    sum += salary[s]
print(sum - salary[0] - salary[-1]) / (n - 2)
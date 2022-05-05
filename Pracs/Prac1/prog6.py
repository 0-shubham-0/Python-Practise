import functions

nums = [1, 2, 3, 4, 5, 6, 7, 8, 54, 3]
print(nums)
n = int(input('number to be searched'))
# i=functions.getindex(nums, int(n))
# print(n, 'is present', nums.count(int(n)), 'number of times at', i)
b = False
j = 0
for k in nums:
    if k == n:
        b = True
        nums.pop(j)
    j += 1
if b:
    print(n, 'is present in list.\n', n, 'removed from the list =', nums)

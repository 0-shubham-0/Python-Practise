import functions

l=[1,2,3,4,5]
print(l)
sum=0
len=0
for n in l:
    sum+=n
    len+=1
print("sum is", sum)
avg= sum / len
print("avg is", avg)
print("sum is", functions.get_sum(l))
print("avg is", functions.get_avg(l))
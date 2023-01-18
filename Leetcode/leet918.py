# def maxSubarraySumCircular(nums):
#     max_current=max_global=-nums[0]
#     n=len(nums)
#     for i in range(1,n):
#         max_current=max(-nums[i],-(nums[i]+max_current))
#         max_global=max(max_current,max_global)
#     print(max_global)
#     sum=nums[0]
#     for i in range(1,n):
#         sum+=nums[i]
#     print(sum-max_global)

# n=[5,-3,5]

# maxSubarraySumCircular(n)

# nums = [5,-3,5]
# nums=[-nums[i] for i in range(len(nums))]
# print(nums)

for i in range(5):
    print(i)
    if i==3:
        break
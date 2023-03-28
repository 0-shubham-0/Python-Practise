import random
import matplotlib.pyplot as plt

# Initializing Variables
num_of_trials = 100000
num_of_toss = 10
heads = 0
total = 0
data = []

for i in range(num_of_trials):
    for n in range(num_of_toss):
        toss = random.randint(0, 1)
        if toss == 1:
            heads += 1
            total += 1
    # print(heads)
    data.append(heads)
    heads = 0
# print(data)
plt.hist(data, bins=40)
plt.title('Number of Heads vs Frequency')
plt.xlabel('number of heads')
plt.ylabel('Frequency')
plt.show()

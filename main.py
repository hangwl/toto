import numpy as np
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt


data = "./data/ToTo.csv"
df = pd.read_csv(data)
df2 = df[df["Draw"]>2994] # toto format changed on 7 oct 2014

WINNINGNOS = ["Winning Number 1","2","3","4","5","6"]
nums = df2[WINNINGNOS].to_numpy()
win_counter = Counter([i for i in range(1,50)])
prob_counter = Counter([i for i in range(1,50)])
for row in nums:
    for num in row:
        win_counter[num] += 1
for i in range(1,50):
    prob_counter[i] = win_counter[i]/len(nums)

if __name__ == "__main__":
    plt.bar(prob_counter.keys(), prob_counter.values())
    plt.axhline(y=6/49, color='r', linestyle='-')
    plt.xticks(np.arange(min(prob_counter.keys()), max(prob_counter.keys())+1, 1.0))
    plt.show()
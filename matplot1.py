import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import seaborn as sns
sns.set()

# x = np.linspace(0, 10, 100)
# function1 = np.sin(x)
# function2 = np.cos(x)
# plt.plot(x, function1)
# plt.plot(x, function2)
plt.xlabel('x')
plt.ylabel('y')
# plt.legend(['sin', 'cos'])

random = 100 * np.random.randn(100, 1)
x = range(1, 101)
# random.sort()
# print(random)
l = []
for i in random:
    l.append(np.int(i)) 
data = pd.Series(l)
distribution = data.value_counts(bins = 20)
print(distribution)
# l.sort()
# x1 = [1, 3, 5, 7]
# y1 = [10, 15, 8, 20]
# x2 = [2, 4, 6, 8]
# y2 = [11, 16, 5, 17]
# plt.bar(x1, y1, color = 'm')
# plt.bar(x2, y2, color = 'c')
# plt.hist(distribution, color = 'c')
plt.scatter(x, l, color = 'm', marker = '*', linewidths = 2)


plt.show()


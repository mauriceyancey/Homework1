%%timeit -n5000
# %%timeit -n1150
# %%timeit -n250

import random

randList =[]
for x in range(10):
    randList.append(random.random())
print(sorted(randList))
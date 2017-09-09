%%timeit
import random

randList =[]
for x in range(10):
    randList.append(random.random())
print(sorted(randList))

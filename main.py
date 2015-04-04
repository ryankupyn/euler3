import math
import primechecker
import factorizer
primelist = []
factorslist = factorizer.factorizer(600851475143)
for x in range(0, len(factorslist)):
    if primechecker.primechecker(factorslist[x]) == True:
        primelist.append(factorslist[x])
print max(primelist)
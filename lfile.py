import random
import sys

f = open("largefile.txt",'a')

for item in xrange(1,500000):
    r = random.randrange(10,10000)
    f.write(str(r) + '\n')



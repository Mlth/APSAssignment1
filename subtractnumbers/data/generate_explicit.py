import random
import sys

random.seed(int(sys.argv[-1])) # fix seed of random generator to last argument


print( random.randrange(-100, 100), random.randrange(-100, 100))
#! /usr/env/python3

import random
import sys

random.seed(int(sys.argv[-1])) # fix seed of random generator to last argument

print( random.randrange(-1000, 1000), random.randrange(-1000, 1000))
#! /usr/bin/env python3

import sys
import re

line = sys.stdin.readline()
assert re.match(r"(0|-?[1-9][0-9]*) (0|-?[1-9][0-9]*)\n", line), line

a, b = map(int, line.split())
assert -1000 < a < 1000
assert -1000 < b < 1000

assert sys.stdin.readline() == ""
sys.exit(42)
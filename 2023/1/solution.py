#! /usr/bin/env python3

import sys

from string import digits


total = 0
for line in sys.stdin:
    line_digits = [d for d in line if d in digits]
    total += int(line_digits[0] + line_digits[-1])

print(total)

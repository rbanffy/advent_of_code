#! /usr/bin/env python3

import sys

from string import digits

def normalized(s: str) -> str:
    print(s)
    spelled_out_digits = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
    indexes = { digit, s.find(digit) for digit in spelled_out_digits if s.find(digit) != -1 }
    min_index = min([ indexes[k] for k in indexes ])
    max_index = max([ indexes[k] for k in indexes ])

    return s


total = 0
for line in sys.stdin:
    line_digits = [d for d in normalized(line) if d in digits]
    total += int(line_digits[0] + line_digits[-1])

print(total)

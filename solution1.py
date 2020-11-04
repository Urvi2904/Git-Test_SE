#!/bin/python3

import sys

def solve(a0, a1, a2, b0, b1, b2):
    arr_a = 0
    arr_b = 0

    if a0>b0:
        arr_a = arr_a + 1
    else:
        arr_b = arr_b + 1

    if a1>b1:
        arr_a = arr_a + 1
    else:
        arr_b = arr_b + 1

    if a2<b2:
        arr_b = arr_b + 1
    else:
        arr_a = arr_a + 1

    return arr_a, arr_b

if __name__ == "__main__" :

	a0, a1, a2 = input().strip().split(' ')
	a0, a1, a2 = [int(a0), int(a1), int(a2)]
	b0, b1, b2 = input().strip().split(' ')
	b0, b1, b2 = [int(b0), int(b1), int(b2)]
	result = solve(a0, a1, a2, b0, b1, b2)
	print (" ".join(map(str, result)))

#!/usr/bin/env python3

def print_fibonacci(length):
    #fib = num of the last two nums
    fib = [0,1]
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    else:
        for i in range(2,length):
            fib.append(fib[i - 1] + fib[i - 2])
        print(fib)

print_fibonacci(9)


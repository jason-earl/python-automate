#!/usr/bin/env python3

from Fib import fib
from EnglishNumber import int_to_english

def main():
    for i in range(70):
        fibber = fib(i)
        print("{}: {}, {}".format(i, fibber, int_to_english(fibber)))

if __name__ == '__main__':
    main()

#!/usr/bin/python3
def fizzbuzz():
    fr num in range(1, 101):
        if num % 3 == 0 and num % 5 != 0:
            print('Fizz', end=' ')
        elif num % 5 == 0 and num % 3 != 0:
            print('Buzz', end=' ')
        elif num % 3 == 0 and num % 5 == 0:
            print('FizBuzz', end=' ')
        else:
            print(num, end=' ')

#!/usr/bin/env python3

def happy_new_year():
    count = 10
    while count > 0:
        print(count)
        count -= 1
    print("Happy New Year!")

def square_integers(int_list):
    return [integ_num**2 for integ_num in int_list]

def fizzbuzz():
    for i in range(100):
        i+=1
        if (i%3==0 and i%5==0):
            print('FizzBuzz')
        elif i%3==0:
            print('Fizz')
        elif i%5==0:
            print('Buzz')
        else:
            print(i)

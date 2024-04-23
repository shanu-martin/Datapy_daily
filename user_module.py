import subprocess
import socket
import sys
def install_req():
    try:
        # Attempt to connect to a well-known website
        socket.create_connection(("www.google.com", 80))  #just checking for internet
        req = ['sympy']
        subprocess.run(['pip', 'install'] + req)
        print('\033[2J\033[H', end='') 
        print(f'\033[94mEstablishing connection...\033[0m \nUser Module : \033[32m Connected \033[0m')
    except OSError:
        print("\033[91mError: Not connected to the internet.\033[0m")
        print(f'\033[94mEstablishing connection\033[0m \nUser Module : \033[91m Not Connected \033[0m')

        sys.exit(1)
install_req()

import math
from sympy import isprime as check


# Functions

# Prime Number
def check_prime(x):
    try:
        x=int(x)
        if check(x):
            print(f"\033[32m{x} is prime\033[0m")
        else:
            print(f"\033[91m{x} is not prime\033[0m")
    except Exception:
        print("\033[91mError: invalid Entry\033[0m")
# Factorial
def fact(x):
    try:
        print(f'Factorail of {x} is : ',math.factorial(int(x)))
    except Exception:
        print("\033[91mError: Invalid Entry\033[0m")
# Fibonacci Series
def fibonacci(n):
    try:
        n=int(n)
        fib_series = [0, 1]
        for i in range(2, n):
            fib_series.append(fib_series[-1] + fib_series[-2])
        print(f"Fibonacci series up to  {n} terms: , \033[94m{fib_series}\033[0m")
    except Exception:
        print("\033[91mError: invalid Entry\033[0m")


# Armstrong Number
def arm(x):
    try:
        x=int(x)
        num_str = str(x)
        num_digits = len(num_str)
        armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
        if armstrong_sum == x:
            print(f"\033[32m{x}is an Armstrong number\033[0m")
        else:
            print(f"\033[91m{x} is not an Armstrong number\033[0m")
    except Exception:
        print("\033[91mError: invalid Entry\033[0m")


# Sum of n
def nsum(*args):
    try:
        total = sum(args)
        print(f"Sum of the numbers \033[94m{args}\033[0m  is:\033[32m {total}\033[0m")
    except Exception:
        print("\033[91mError: invalid Entry\033[0m")


nsum(3,4,5)
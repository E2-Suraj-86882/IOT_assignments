#Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

def fact(param):
    factorial=1
    for i in range(1, param + 1):
        factorial *= i
    print(f"The factorial of {param} is {factorial}")
fact(6)
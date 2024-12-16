#Using for loop, write and run a Python program to find factorial from 0 to 10.
def fact(param):
    factorial=1
    for i in range(1, param + 1):
        factorial *= i
    return factorial

for num in range(11):
    print(f"The factorial of {num} is {fact(num)}")
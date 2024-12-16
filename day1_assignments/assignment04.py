#Write a Python function to find the maximum of three numbers.

def max_three_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        max = num1
    elif num2>=num1 and num2>=num3:
        max = num2
    else:
        max = num3
    return max
print(max_three_num(50,120,30))


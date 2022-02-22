num1 = float(input("enter the first number"))
num2 = float(input("enter the second number"))
num3 = float(input("enter the third number"))

def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        print(str(num1) + "is the greatest")
    elif num2 >= num1 and num2 >= num3:
        print(str(num2) + " is the greatest")
    else:
        print(str(num3) + " is the greatest")
print(max_num(num1, num2,num3))


num1 = float(input("enter a number"))
operator1 = input("enter an operator")
num2 = float(input("enter second number"))

if operator1=="+":
    print(num1 + num2)
elif operator1=="-":
    print(num1-num2)
elif operator1=="*":
    print(num1*num2)
elif operator1=="/":
    print(num1/num2)
else : print("invalid operator")
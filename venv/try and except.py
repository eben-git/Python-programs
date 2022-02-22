try :
    number = (int(input("enter a number: ")))
    print(number)
except ZeroDivisionError as errz:
    print(errz)
except ValueError as err:
    print(err)


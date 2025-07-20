num = eval(input("Please enter the Number 1 to 4 :"))
if num in [1,2,3,4]:
    if num == 1:
        print("one")
    elif num == 2:
        print("two")
    elif num == 3:
        print("Three")
    else:
        print("Four")
else:
    print("Please enter the Valid Number")
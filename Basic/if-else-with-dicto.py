num = eval(input("enter the valid value 1 to 4 :"))
num_word = {1:'one',2:'two',3:'three',4:'four'}
if num in [1,2,3,4]:
    print(num_word.get(num))
else:
    print("Enter the Vaid Number")
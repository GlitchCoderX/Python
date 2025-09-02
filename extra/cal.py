print("Calculator. availalble + - * /")

num1 = int(input("Enter 1st number: "))
action= input("what action you want to do?")
num2 = int(input("Enter 2nd number: "))

print("answer is : ")
if action=="+":
    print(num1+num2)
elif action == "-":
    print(num1-num2)
elif action =="*":
    print(num1*num2)
elif action == "/":
    if num1 == 0:
        print("Unexpected input!!!")
    if num2 == 0:
        print("Unexpected input!!!")
    else : print(num1/num2)
else:  print("Unexpected input!!!")


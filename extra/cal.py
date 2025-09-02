print("Calculator. Available: + - * /")

num1 = int(input("Enter 1st number: "))
action = input("What action do you want to do? ")
num2 = int(input("Enter 2nd number: "))

print("Answer is: ", end="")

if action == "+":
    print(num1 + num2)
elif action == "-":
    print(num1 - num2)
elif action == "*":
    print(num1 * num2)
elif action == "/":
    if num2 == 0:
        print("Unexpected input!!! (cannot divide by zero)")
    else:
        print(num1 / num2)
else:
    print("Unexpected input!!!")

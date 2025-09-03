print("let's take out the bigger number!!!")
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

if num1 > num2 :
    print(f"Number_1 = {num1} is bigger than Number_2 = {num2}")
elif num2 > num1 :
    print(f"Number 2 = {num2} is bigger than Number 1 = {num1}")
elif num1 == num2 :
    print("Same")
else: print("Unexpected input!!!")


for i in range( 1, 21, 3):
    print( i, end=" ")

for j in "abcd":
    print("\n", j, end=" ")

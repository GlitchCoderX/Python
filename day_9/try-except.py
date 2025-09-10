num = int(input('Enter your number: '))
#num2 = int(input('Enter your 2nd number: '))

try:                            #try to execuate the code
    a = num + 1
except:                         #if 'try' can't can't execute the code
    print('something wrong!!')
else:                           #If 'try' works that will too
    print("Your num + 1 = ", a)
finally:                        # it doesn't matter what heppend but it will execuate
    print('Tnx')

try:
    b =num2 ** 2
except NameError:
    print('custom Name error!')
else:
    print(f"your num2's spure is {b}")
finally:
    print('ok ok ok ok ok ok')
a = 9
b = 0

while a < 10:
    a += 1
    print(a, end=" ")
    if a == 7:
        print("hit 7")
        continue
    print("hello")

while b < 16:
    b += 2
    print(b)
    if b == 10:
        break
    
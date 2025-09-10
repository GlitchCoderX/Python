#making function
a1 = 5
a2 = 6

def sum():
    print(a1 + a2)

#with parameters
a = int(input("enter your triangel's base: "))
b = int(input("enter your triangel's height: "))

def tri_area(base, height):
    area = base * height * 0.5
    print(area)

tri_area(a, b)

#using return
sub_bn = int(input("enter your score in Bangla: "))
sub_en = int(input("enter your score in English: "))
sub_ict = int(input("enter your score in ICT: "))

def result(bangla,english,ICT):
    full = bangla+english+ICT
    return full

print(result(sub_bn,sub_en,sub_ict))
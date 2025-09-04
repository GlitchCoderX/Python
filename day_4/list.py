li = [3, 1, 7, 3, 8, 9, 4]
ls = ["apple","Banna", "mango","lorem", "Nahid", "omg","python", "lorem","hello", "lovely"]
l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]

print("------adding items-------") #adding items
print("at first",li)
li.append(12) 
print("After append",li) # add at the end
li.insert(2, 99)
print("after insert", li)# add at no.2
li.extend([55,66])
print("expend",li) # add multiple item at last

print("-----remove-----")
li.remove(4)# 5th item removed
li.pop() # remove the last item
li.pop(3) # remove the 4th item
del li[0] # delete by index
#li.clear()
print("After removin'", li)

print("-----Accsessing item-----")

print(li[1]) # accseing the 2nd item
print(li[-1]) # accessing the last item
print(ls[2:5]) # assessing by a to b point
print(l1[2:11:2]) #assessing by a to b point but gapping 2
print(l1[-2:-11:-1]) #assessing by a to b point but gapping 2 but revarsed

print("-----sarching----")
print("Nahid" in ls) # check if exist
print(ls.index("mango")) # position

LoremPos = ls.index("lorem")
print(LoremPos)
print(ls.index("lorem", LoremPos+1))
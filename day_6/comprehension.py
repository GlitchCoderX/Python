#list 
l1 = [1,2,3,4,5]
l2 = [6,7,8,9,0]

full = l1 + l2 # also can be done by extend. like: l1.extend(l2)
print(full)

# tuple and works like this except dict need this |

#zip, works with anything 

d1 = ["name:", "Roll:", "class:"]
d2 = ["Nahid Hossain", "02", "eight"]

zipped = zip(d1, d2)
print(list(zipped))

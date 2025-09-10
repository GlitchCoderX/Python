f = open("E:/python/extra/pyimp.txt", "r")   # "r" means read mode
text = f.read()
print(text)
f.close()

#also
with open("e:/python/extra/testing/testing.txt", "a+") as txtFile:
    txtFile.write("New line! \n")   # append
    txtFile.seek(0)                # go back to start
    print(txtFile.read())

palarray=[]

for x in range(99,1000):
    for y in range(99,1000):
        string = str(x*y)
        if string == string[::-1]:
             palarray.append(int(string))
palarray.sort()
print palarray

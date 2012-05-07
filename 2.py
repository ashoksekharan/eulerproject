a=1
b=0
temp = 0

print "Printing all the even numbers in fibonacci sequence"
while ((a<4000000) & (b<4000000)):
    a, b = b, a + b
    if (b%2 == 0):
        temp=temp+b
        print b
        print '*',temp


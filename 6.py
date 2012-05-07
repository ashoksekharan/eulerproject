import sys

number = int(sys.argv[1])

squaretemp=0
tempsquare=0
for i in range(0,number+1):
    squaretemp+=i**2
    tempsquare+=i
tempsquare=tempsquare**2
print (tempsquare-squaretemp)

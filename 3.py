import sys

def isprime(number):
    for i in xrange(2,number-1): 
        if number%i == 0:
            print " Composite number found" 
#            exit()
            print i
        if number%i != 0:
            primenumberflag=0
    if primenumberflag == 0:
        print "Prime Number Largest Factor", number

isprime(long(sys.argv[1]))

'''
program to check whether a number is prime
'''
n=int(input("enter num: "))
if n>1:
    for i in range(2,(n//2)+1):
        if (n%i) == 0:
            print(n, "is not prime")
            break
    else :
        print(n, "is prime")
else:
    print(n, "is not prime")

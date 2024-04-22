def Factorial(a):
    c=1
    for i in range(1,a+1):
        c*=i
    return c
    
a=int(input())
b=int(input())
n=Factorial(a)
nk=Factorial(a-b)
k=Factorial(b)
c=n/(nk*k)
print(c)


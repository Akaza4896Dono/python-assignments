x=int(input("Enter a number: "))
def factorial(x):
    fact=1
    if x!=0:
        for el in range(1,x+1):
            fact=fact*el
    return fact
print("Factorial of",x,"is:",factorial(x))
   


n= int(input("Enter a number: "))

factorial = 1
a=1

if n < 0:
    print("Factorial does not exist for negative numbers.")
else:
    for i in range(n):
        
        factorial *=a
        a+=1

    print(f"Factorial of {n} is", factorial)
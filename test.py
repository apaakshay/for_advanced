def max_of_three(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
num1=int(input("Enter number1: "))
num2=int(input("Enter number2: "))
num3=int(input("Enter number3: "))
sum=max_of_three(num1,num2,num3)
print("Largest number=",sum)
replace1=""
num1=int(input("Akshay Enter a Number1:  "))
print(num1)

num2=int(input("Akshay Enter another Number2:  "))
print(num2)

print("These are the operators you can use: ")
print("1. Addition")
print("2. Substraction ")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
result=0
operator=input("Please choose an option from these(1,2,3,4,5): ")
if operator=="1":
    replace1="Addition"
    result=num1+num2

if operator=="2":
    replace1="Substraction"
    result=num1-num2

if operator=="3":
    replace1="Multiplication"
    result=num1*num2

if operator=="4":
    replace1="Division"
    result=num1//num2

if operator=="5":
    replace1="Modulus"
    result=num1%num2
print("The Result Of",replace1,"of",num1,"and",num2,"is",result)

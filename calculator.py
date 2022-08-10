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
sum=input("Please choose an option from these(1,2,3,4,5): ")
if sum=="1":
    print("1.Addition")
    print("the sum of two numbers: ",num1+num2)
if sum=="2":
    print("2.Substraction")
    print("the substraction of two numbers: ", num1 - num2)
if sum=="3":
    print("3.Multiplication")
    print("the Multicplication of two numbers: ", num1 * num2)
if sum=="4":
    print("4.Division")
    print("the divison of two numbers: ", num1 / num2)
if sum=="5":
    print("5.Modulus")
    print("the modulus of two numbers: ", num1 % num2)
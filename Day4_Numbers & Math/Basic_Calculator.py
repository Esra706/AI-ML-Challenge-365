# Basic Calculator 

num1=float(input("Enter the  1st number "))
num2=float(input("Enter the 2nd number "))

print("Print opreation which you want to perform")

print("\nChoose an operation:")
print("+ : Addition")
print("- : Subtraction")
print("* : Multiplication")
print("/ : Division")

choice=input("Enter opreator: (+,-,*,%,/) :")
if choice=="+":
    print(f"Result : {num1} + {num2} = {num1 + num2}")
elif choice=="-":
    print(f"Result : {num1} - {num2} = {num1 - num2}")
elif choice=="%":
    print(f"Result : {num1} % {num2} = {num1 % num2}")
elif choice=="*":
    print(f"Result : {num1} * {num2} = {num1 * num2}")
elif choice == "/":
    # Edge case: Zero se division check karna
    if num2 == 0:
        print("Error: Cannot divide by zero!")
    else:
        print(f"Result: {num1} / {num2} = {num1 / num2}")

print("Thanks for using Calculator ")


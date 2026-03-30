choice = input("What operation would you like to do? +, -, /, *")

num1 = 0
num2 = 0

if choice == "+":
    print("You chose Addition")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("Answer: " + str(num1+num2))
elif choice == "-":
    print("You chose Substaction")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("Answer: " + str(num1-num2))
elif choice == "*":
    print("You chose multiplication")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("Answer: " + str(num1*num2))
elif choice == "/":
    print("You chose division")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("Answer: " + str(num1/num2))
else:
    print("Invalid operation selected, Please try again")


# Explain to the students the concept of varibale initizalise
# Explain why we initizalise - Data overwrite issue. 
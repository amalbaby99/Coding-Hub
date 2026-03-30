choice = input("What operation would you like to do? +, -, /, *")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if choice == "+":
    print("You chose Addition")
    print("Answer: " + str(num1+num2))
elif choice == "-":
    print("You chose Substaction")
    print("Answer: " + str(num1-num2))
elif choice == "*":
    print("You chose multiplication")
    print("Answer: " + str(num1*num2))
elif choice == "/":
    print("You chose division")
    print("Answer: " + str(num1*num2))
else:
    print("Invalid operation selected, Please try again")


# Make the students try this
# Explain the concept of IF, Elif, Else
# Extention task - Ask if anyone can make the program skip asking inputs if the operation is incorrect
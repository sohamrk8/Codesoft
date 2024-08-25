num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


print("Press 1 for Addition")
print("Press 2 for Subtraction")
print("Press 3 for Multiply")
print("Press 4 for Divide")

choice = int(input("Enter your choice 1-4: "))
if choice == 1:
    print("The addition of given number",num1 + num2)
elif choice == 2:
    print("The subtraction of given number",num1 - num2)
elif choice == 3:
    print("The multiplication of given number",num1 * num2)
elif choice == 4:
    print("The division of given number",num1 / num2)
else:
    print("Invalid input")
age =int(input("Enter your age: "))

if age>=18:
    print("You are eligible to vote")

else:
    print("You are not eligible to vote, too young")


#program to check if a number is odd or even
number =int(input("Enter a number: "))

if number%2 == 0:
    print("The number is even.")

else:
    print("The number is odd.")


#program to check the largest number in three inputs using input output
num1 =int(input("Enter the first number: "))
num2 =int(input("Enter the second number: "))
num3 =int(input("Enter the third number: "))

if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3


print(f"The largest number is: {largest}")


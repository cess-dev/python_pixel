def greet():
    print("Welcome to Pixel class!!!")
greet()

# function with parameters
def student(name, age):
    print(f"My name is {name} and I am {age} years old")
student("Mercy", 20)

def add(x,y):
    return x+y
result1=add(6,23)
print(result1)

# function using input output
def add_numbers(a,b):
    return a+b
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

result=add_numbers(num1,num2)
print(f"The sum is {result}")


# create a program that gives 10% discount
def calculate_discount(price):
    discount=price*0.10
    final_price=price-discount
    return final_price
price=float(input("Enter product price: "))
total=calculate_discount(price)
print(f"Price after discount: {total}")
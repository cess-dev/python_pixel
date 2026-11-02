# list datastructure
# mutable/changeable
# has indexes

products = ["Bread", "Milk", "Sugar", "Blueband"]
print(f"My products {products}")
products[0]="Cake"
print(f"Updated products {products}")

products.pop()
print(products)
for p in products:
    print(p)

# tuple datastructure
# immutable, unchangeable
# used on items that dont change

location = ("Nairobi", "Uganda", "Tanzania")
# location[1]="Burundi" --wrong, wont work
print(location)

# set datastructure
# removes duplicates
mystock = {"hp", "lenovo", "dell", "hp"}
print(mystock)

# dictionary datastructure
customer = {
    "name":"Eric",
    "age": 30,
    "city":"Nairobi",
    "proffesion":"Software Engineer"
}

print(f"Name: {customer['name']}")

# store products and their prices
shop={
    "Bread":130,
    "Milk":90,
    "Sugar":190
}
for product, price in shop.items():
    print(product, "Cost Ksh" ,price)
print("Milk cost Ksh", shop["Milk"]) #confirmation

# imagine you are building a school system that 
# calculates the average mark of a student
marks = [76,83,67,90,79]
sum =0
for mark in marks:
    stotal = total=+mark
average = total/len(marks)
print(f"Total marks: {total}")
print(f"Average marks: {average}")

# Create a complex calculator using input output and loops
import math

def show_menu():
    """Displays the calculator menu options."""
    print("ADVANCED PYTHON CALCULATOR")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exponentiation (^)")
    print("6. Square Root (√)")
    print("7. View Calculation History")
    print("8. Exit")
    print("-" * 30)

def calculator():
    # List to store calculation history
    history = []
    
    while True:
        show_menu()
        choice = input("Enter your choice (1-8): ").strip()
        
        # Exit condition
        if choice == '8':
            print("\nThank you for using the calculator. Goodbye!")
            break
            
        # View history
        if choice == '7':
            print("\n--- Calculation History ---")
            if not history:
                print("No calculations recorded yet.")
            else:
                for idx, record in enumerate(history, 1):
                    print(f"{idx}. {record}")
            print("-" * 27)
            continue
            
        # Operations requiring two numbers
        if choice in ['1', '2', '3', '4', '5']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("\n[Error] Invalid input. Please enter numeric values only.")
                continue
                
            if choice == '1':
                result = num1 + num2
                operation_str = f"{num1} + {num2} = {result}"
            elif choice == '2':
                result = num1 - num2
                operation_str = f"{num1} - {num2} = {result}"
            elif choice == '3':
                result = num1 * num2
                operation_str = f"{num1} * {num2} = {result}"
            elif choice == '4':
                if num2 == 0:
                    print("\n[Error] Division by zero is not allowed.")
                    continue
                result = num1 / num2
                operation_str = f"{num1} / {num2} = {result}"
            elif choice == '5':
                result = num1 ** num2
                operation_str = f"{num1} ^ {num2} = {result}"
                
            print(f"Result: {result}")
            history.append(operation_str)
            
        # Operation requiring one number (Square Root)
        elif choice == '6':
            try:
                num = float(input("Enter the number: "))
                if num < 0:
                    print("\n[Error] Cannot calculate the square root of a negative number.")
                    continue
                result = math.sqrt(num)
                operation_str = f"√({num}) = {result}"
                print(f"Result: {result}")
                history.append(operation_str)
            except ValueError:
                print("\n[Error] Invalid input. Please enter a numeric value.")
                continue
        else:
            print("\n[Error] Invalid choice! Please select an option between 1 and 8.")

if __name__ == "__main__":
    calculator()



def add(x, y):
    return x + y

def min(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

# provide options for operations
print("Please select an operation.")
print("For addition select 1. ")
print("For subtraction select 2.")
print("For multiplication  select 3.")
print("For division select 4.")

option = input("Please enter the number of your option 1, 2, 3, 4:")

# limit option to 1,2,3,4
if option > '4':
    print("Invalid input. Please select 1,2,3 or 4.")

elif option < '5':

    print("Please select an operation.")
    print("For addition select 1. ")
    print("For subtraction select 2.")
    print("For multiplication  select 3.")
    print("For division select 4.")


num1 = float(input( "Please enter the first value: "))
num2 = float(input( "Please enter the second value: ")

if choice == '1':
    print(num1, " + ", num2, "=", add(num1,num2))

elif choice == '2':
    print(num1, " - ", num2, "=", min(num1, num2))


elif choice =='4':
    print(num1, " / ", num2, "=", div(num1, num2))
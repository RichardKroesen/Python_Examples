class MyException(Exception):
    pass

try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise MyException("Age cannot be negative.")
except MyException as e:
    print(e)
except ValueError:
    print("Please enter a valid integer.")

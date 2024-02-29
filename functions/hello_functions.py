def greet(name="Bob", company=None): # Function definition
    if company:
        print(f"Hello {name} from {company}, welcome to Python functions!")
    else:
        print(f"Hello {name}, welcome to Python functions!")

first_name = "Wojciech"

greet(first_name, "nocrash.tech") # Calling a function

greet()
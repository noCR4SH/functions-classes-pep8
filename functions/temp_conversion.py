def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

while True:
    print("\n 1. Celsius to Fahrenheit \n 2. Fahrenheit to Celsius \n 3. Exit\n")
    choice = input("Choose a conversion (1-3): ")

    if choice == "1":
        celsius_input = float(input("Enter temperature in Celsius: "))
        # result = celsius_to_fahrenheit(celsius_input)
        print(f"{celsius_input}°C is {celsius_to_fahrenheit(celsius_input):.1f}°F")
    elif choice == "2":
        fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
        result = fahrenheit_to_celsius(fahrenheit_input)
        print(f"{fahrenheit_input}°F is {result:.1f}°C")
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")

print(choice)
print("Bye!")

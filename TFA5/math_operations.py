def divide(x, y):
    return None if y == 0 else x / y

def exponentiate(x, y):
    return x ** y

def remainder(x, y):
    return None if y == 0 else x % y

def summation(start, end):
    return None if start > end else sum(range(start, end + 1))

def get_input():
    try:
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        return x, y
    except ValueError:
        print("Invalid input! Only integers are allowed. ")
        return None, None

def main():
    operations = {
        'D': ("Division", divide),
        'E': ("Exponentiation", exponentiate),
        'R': ("Remainder", remainder),
        'F': ("Summation", summation)
    }
    
    while True:
        print("========================")
        print("   Mathematical Menu    ")
        print("========================")
        for key, (name, _) in operations.items():
            print(f"[{key}] - {name}")
        print("[Q] - Quit")
        print("========================")
        
        choice = input("Enter your choice: ").strip().upper()
        if choice == 'Q':
            print("Goodbye! Thanks for using the program.\n")
            break
        
        if choice in operations:
            num1, num2 = get_input()
            if num1 is None or num2 is None:
                continue
            
            result = operations[choice][1](num1, num2)
            if result is None:
                print("Invalid operation based on provided inputs.\n")
            else:
                print(f"Result: {result}\n")
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

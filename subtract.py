def subtract_two_numbers():

# Subtracts two numbers entered by the user and prints the result.

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 - num2
        print(f"The result of {num1} - {num2} is {result}")
        return result
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return None

# Example usage:
if __name__ == "__main__":
    subtract_two_numbers()


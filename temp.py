def calculate_square(number):
    """
    Calculate the square of a given number
    """
    return number * number

def main():
    # Get user input
    name = input("Enter your name: ")


    number = int(input("Enter a number to calculate its square: "))
    number2 = int(input("Enter a number to calculate its square: "))
    print(number2)
    
    # Calculate the square
    result = calculate_square(number)
    
    # Print the results
    print(f"Hello {name}!")
    print(f"The square of {number} is: {result}")

if __name__ == "__main__":
    main()

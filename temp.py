def calculate_square(number):
    """
    Calculate the square of a given number
    """
    return number * number

def main():
    # Get user input


    print("Hello, World!")
    name = input("Enter your name: ")
    number = int(input("Enter a number to calculate its square: "))
    
    # Calculate the square
    result = calculate_square(number)


    print("Hello, World!")
    
    # Print the results
    print(f"Hello {name}!")
    print(f"The square of {number} is: {result}")

if __name__ == "__main__":
    main()

def smallest_factor(n):
    """Find the smallest factor of a given number."""
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    return n


def is_prime(num):
    """Check if it is a prime number."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_numbers_in_range(start, end):
    """Generate the prime numbers within the specified range."""
    prime_num = [num for num in range(start, end + 1) if is_prime(num)]
    return prime_num


while True:
    print("1. Find the smallest factor of a number")
    print("2. Generate the prime numbers in a range")
    print("0. Exit")

    choice = int(input("Enter your chosen number (0, 1, or 2): "))

    if choice == 0:
        print("Exiting the program.")
        print("Thank you for trying!!")
        break
    elif choice == 1:
        number = int(input("Enter a number: "))
        result = smallest_factor(number)
        print(f"The smallest factor of {number} is: {result}")
        print("____________________________________")
    elif choice == 2:
        start_range = int(input("Enter the start of the range: "))
        end_range = int(input("Enter the end of the range: "))
        primes_in_range = prime_numbers_in_range(start_range, end_range)
        print(f"Prime numbers in the range from {start_range} to {end_range} is: {primes_in_range}")
        print("___________________________________")
    else:
        print("Invalid choice. Please enter 0, 1, or 2.")
        print("___________________________________")
def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b

def main():
    print("Welcome to the Fibonacci number calculator!")
    n = int(input("Please enter the position of the Fibonacci number you want to find: "))
    result = fibonacci(n)
    print(f"The {n}th Fibonacci number is {result}.")

if __name__ == "__main__":
    main()

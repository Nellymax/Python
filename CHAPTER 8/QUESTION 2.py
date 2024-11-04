def syracuse_sequence(n):
    if n <= 0:
        return "Input should be a positive integer."
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def main():
    print("Welcome to the Syracuse sequence generator!")
    n = int(input("Please enter a natural number: "))
    result = syracuse_sequence(n)
    print(f"The Syracuse sequence starting from {n} is: {result}")

if __name__ == "__main__":
    main()

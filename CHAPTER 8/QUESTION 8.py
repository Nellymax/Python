def gcd(m, n):
    while m != 0:
        m, n = n % m, m
    return n

def main():
    print("Welcome to the GCD calculator!")
    m = int(input("Please enter the first number: "))
    n = int(input("Please enter the second number: "))
    result = gcd(m, n)
    print(f"The GCD of {m} and {n} is {result}.")

if __name__ == "__main__":
    main()

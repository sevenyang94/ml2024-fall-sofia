def main():
    numbers = []

    N = int(input("Enter a integer N: "))

    for i in range(N):
        number = int(input(f"Enter number {i + 1}: "))
        numbers.append(number)

    X = int(input("Enter the integer X: "))

    if X in numbers:
        index = numbers.index(X) + 1
        print(index)
    else:
        print(-1)

if __name__ == "__main__":
    main()
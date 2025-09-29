def main():
    size = int(input("Enter the size of the pattern: "))

    row = 0
    while row < size:
        for _ in range(size):
            print("*", end="")
        print()
        row += 1

if __name__ == "__main__":
    main()

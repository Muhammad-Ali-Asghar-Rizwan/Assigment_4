def double(num:int) -> int:
    return num * 2


def main():
    num = int(input("Enter a number: "))
    print("The double of", num, "is", double(num))

if __name__ == "__main__":
    main()    
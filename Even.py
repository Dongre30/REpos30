def main():
    print(is_even(int(input("Enter a number: "))))

def is_even(k):
    k = abs(k)
    while k != 0:
        if k < 0:
            return False
        k -= 2
    return True

if __name__ == "__main__":
    main()

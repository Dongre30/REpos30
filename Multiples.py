

def main():
    a = int(input("Enter larger number: "))
    b = int(input("Enter smaller number: ")) 
    print(is_multiple(a,b))
    
def is_multiple(n, m):
    if n%m == 0:
        return True
    else: return False

if __name__ == "__main__":
    main()

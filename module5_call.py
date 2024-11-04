from module5_mod import inputClass

def main():
    inpInstance = inputClass()

    n = int(input("Enter positive integer N: "))
    
    for i in range(n):
        num = int(input(f"Enter number: "))
        inpInstance.addNum(num)
    
    target = int(input("Enter number X to search for: "))
    
    out = inpInstance.searchNum(target)
    if out == -1:
        print("-1")
    else:
        print(f"The number {target} is at position {out}.")

if __name__ == "__main__":
    main()
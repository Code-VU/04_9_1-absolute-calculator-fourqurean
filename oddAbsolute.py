def calculateAbsolute():
    
    # This first line is provided for you
    in_num  = int(input("Enter a number: "))

    if in_num > 21:
        ab_num = abs(in_num - 21) * 2
    else:
        ab_num = abs(in_num - 21)

    print("Result: ",ab_num)
    # end assignment

## If you want to test locally run > python payCalculator.py

if __name__ == "__main__":
    calculateAbsolute()

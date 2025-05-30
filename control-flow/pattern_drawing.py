# File: pattern_drawing.py

try:
    size = int(input("Enter the size of the pattern: "))
    
    if size <= 0:
        print("Please enter a positive integer.")
    else:
        row = 0
        while row < size:
            for col in range(size):
                print("*", end="")
            print()  # move to next line after printing a row
            row += 1

except ValueError:
    print("Please enter a valid integer.")

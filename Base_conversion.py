# TypeConversion from decimal with base 10
# to hexadecimal form with base 16
 
 
# Taking input from user >> an integer with base 10
number = int(input("Enter a number with base 10\n"))

print("a. Decimal to Hexadecimal ")
print("b. Decimal to Octal")
print("c. Decimal to Binary")
 
# taking user input
print("Enter your choice :- ")
choice = input()
 
# Running a variable choice
# Hexadecimal form if choice
# is set to 'a'
if choice =='a':
 
    # lstrip helps remove "0x" from the left
    # rstrip helps remove "L" from the right,
    # L represents a long number
    print("Hexadecimal form of " + str(number) +
        " is " + hex(number).lstrip("0x").rstrip("L"))
         
if choice == 'b':
    print("Octal form of " + str(number) +
        " is " + oct(number).lstrip("0o").rstrip("L"))
         
if choice == 'c':
    print("Binary form of " + str(number) +
        " is "+bin(number).lstrip("0b").rstrip("L"))

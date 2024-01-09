import math
number1 = int(input("Please enter the first side of the triangle:"))
number2 = int(input("Please enter the second side of the triangle:"))
number3 = int(input("Please enter the third side of the triangle:"))
semi_perimeter = (number1 + number2 + number3) / 2
print(math.sqrt(semi_perimeter * (semi_perimeter - number1) * (semi_perimeter - number2) * (semi_perimeter - number3)))
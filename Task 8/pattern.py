#For loop from 1 to 10, printing a number of *'s based on the current increment, split into the first 5 being one star per increment, then the last 4 being how many increments left.
for i in range(1,10):
    if i < 6:
        output = "*"*i
        print(output)
    else:
        output = "*"*(10-i)
        print(output)
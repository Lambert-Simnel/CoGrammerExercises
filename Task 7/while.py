#Start off with a value of 0 for the sum and number of numbers, ask for a number in
number_sum = 0
number_num = 0
number_in = int(input("Please enter an initial number or -1 to exit:"))
#Set up a while loop for while the input isn't -1
while number_in != -1:
    #increment sum and number of numbers
    number_sum += number_in
    number_num += 1
    #ask for new number
    number_in = int(input("Please enter a number or -1 to end the process:"))
#Program gets here if number in is -1, skipping adding the number -1 in
print(number_sum/number_num)
string_input = input("Please enter a sentence: ")
output_one = ""
i = 0
#Iterate over the input, adding the characters as either upper or lower to the output to alternate
for c in string_input:
    i += 1
    if i % 2 == 1:
        output_one += c.upper()
    else:
        output_one += c.lower()
print(output_one)
output_two = ""
input_words = string_input.split()
j = 0
#Iterate over a list of the input split into words, adding them as either upper or lower to the output as well as re-adding spaces
for w in input_words:
    j += 1
    if j % 2 == 1:
        output_two += w.lower()
    else:
        output_two += w.upper()
    output_two += " "
#Printing without the final unecessary space
print(output_two[:-1])
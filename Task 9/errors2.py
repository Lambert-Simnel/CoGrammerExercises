# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

#nameerror, needs quatation marks to define animal as a string of Lion otherwise it tries to define as an existing variable called Lion, also logical error should be lower case
animal = "lion"
#Logical error, Lions are not a type of cub
animal_type = "cat"
#logical error, Lions have 30 teeth
number_of_teeth = 30

#Logical error, needs a f in from of the string to output the variables, and has number_of_teeth and animal_type the wrong way round
full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"

#Syntaxerror missing parentheses
print(full_spec)


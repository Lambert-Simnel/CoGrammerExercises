# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

#Syntax errors in all prints, () required
print ("Welcome to the error program")
#Indentation error, between here and line 17
print ("\n")

# Variables declaring the user's age, casting the str to an int, and printing the result
#Name error, == is comparing rather than defining with =
age_Str = "24 years old" 
#Value error, can only convert the 24 part of the string into an int
age = int(age_Str[:2]) 
#TypeError, can only concatenate strings not ints
print("I'm " + str(age) + " years old.")

# Variables declaring additional years and printing the total years of age
years_from_now = 3
#TypeError, cannnot add a string to an int, changed years_from_now to an int
total_years = age + years_from_now

#name error, total_years not answer_years
print ("The total number of years:" + str(total_years))

# Variable to calculate the total amount of months from the total amount of years and printing the result
#name error, total used when it should be total_years
total_months = total_years * 12
#TypeError, can only concatenate strings not ints
#Logical error, didn't increase the total months by the 3 years 6 months
print ("In 3 years and 6 months, I'll be " + str(total_months + 42) + " months old")

#HINT, 330 months is the correct answer


import math
#Initial output
print("investment - to calculate the amount of interest you'll earn on your investment\nbond       - to calculate the amount you'll have to pay on a home loan\n")
investment_or_bond = input("Enter either 'investment' or 'bond' from the menu above to proceed:").upper()
#if bond is enetered
if investment_or_bond == "BOND":
    #Ask for house value, interest rate, length of time and type of interest
    house_value = int(input("Please enter how much your property is worth in GBP:"))
    monthly_interest_rate = int(input("Please enter the annual interest rate:"))/100/12
    num_months = int(input("Please enter how long you plan to repay the bond in months:"))
    #calculate monthly repayment and print result
    monthly_repayment = (monthly_interest_rate * house_value) / (1 - (1 + monthly_interest_rate)**(-num_months))
    print(f"You will have to pay back £{monthly_repayment:0.2f} per month for {num_months} months.")
#if investment is entered
elif investment_or_bond == "INVESTMENT":
    #Ask for amount of money, interest rate, length of time and type of interest
    money_in = int(input("Please enter how much you are looking to invest in GBP:"))
    interest_rate = int(input("Please enter the annual interest rate:"))/100
    num_years = int(input("Please enter how long you plan to invest for in years:"))
    interest = input("Please enter if the investment uses simple or compound interest:").upper()
    #Calculate rate if simple and print result
    if interest == "SIMPLE":
        money_out = money_in * (1 + interest_rate * num_years)
        print(f"You will have £{money_out:0.2f} by the end of the {num_years} years.")
    #Calculate rate if compound and print result
    if interest == "COMPOUND":
        money_out = money_in * math.pow((1 + interest_rate), num_years)
        print(f"You will have £{money_out:0.2f} by the end of the {num_years} years.")
    #if an invalid entry is entered
    else:
        print("Invalid input, please re-run")
#if an invalid entry is entered
else:
    print("Invalid input, please re-run")
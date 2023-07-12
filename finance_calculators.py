# Compulsory Task 1
# Capstone Project 1 - Variables and Control Structures

# make a financial calculators of which users can access two different path : an investment calculator and a home loan repayment calculator
# requires an option we use if-elif-else statement and if situation requires a condition in a condition we use a nested if-else statement
# I will use nested if-else statement as later on it will ask user more condition once followed one of the two path 
# multiple variables to store different values and assign them to a variable with an meaningful name
# the input() command to allow user to enter data that will be used in program
# for user to enter numbers, convert data type to either float or integer 
# To Allow user to enter data and how they capitalises them to not effect the program or lead to 'invalid input' or syntax error, use either logical operator (or - disjunction operation) or string methods (shown in comment below)
# Arithmetic operators will also be used to be able to do mathematical equations
# use whitespace and indentation and escape sequence to make code look more clean
# display output with print command



import math

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan \n")

user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

if user_choice.lower() == "investment":

    depositing_amount = float(input("Enter How much money you are depositing (type in ONLY the value): "))
    interest          = float(input("Enter (only the number) of the interest rate (as a percentage) eg. 8 : "))
    interest_rate     = interest/100
    years_investing   = float(input("Enter the number of years you plan on investing: "))
    simple_compound   = input("Enter 'simple' if you want simple interest, or enter 'compound' if you want compound interest: ")
    

    if simple_compound == "simple" or simple_compound == "Simple" or simple_compound == "SIMPLE":

        total_amount = depositing_amount*(1 + interest_rate*years_investing)

        print(f"""
                Depositing amount: £{depositing_amount} 
                Intrest rate: {interest}%
                Investment time Plan: {years_investing} years
                Intrest type: {simple_compound} """)

        print("\n                Total amount if chosen simple interest is: £",(round(total_amount, 2)))        

        
    elif simple_compound == "compound" or simple_compound == "Compound" or simple_compound == "COMPOUND":
    
        total_amount = depositing_amount * math.pow ((1 + interest_rate), years_investing)

        print(f"""
                Depositing amount:  £{depositing_amount} 
                Intrest rate:       {interest}%
                Years investing:    {years_investing}
                Intrest type:       {simple_compound} """)
        
        print("\n                Total amount if chosen compound interest is: £",(round(total_amount, 2)))

        
    else:
        print("Please Enter either 'simple' or 'compound' (check for any spelling error)")


elif user_choice == "Bond" or  user_choice =="bond" or user_choice == "BOND":

    present_house_value  = float(input("Enter your present value of the house (type in ONLY the value)eg. 1000: ")) 
    intrest_rate_bond    = float(input("Enter (only the number) of the interest rate (as a percentage) eg. 7: "))
    monthly_interst_rate = (intrest_rate_bond / 100) /12
    months_repay_bond    = int(input("Enter the number of months you plan to take to repay the bond. eg. 120: "))
    
    repayment = (monthly_interst_rate * present_house_value)/(1-(1 + monthly_interst_rate)**(-months_repay_bond))
    
    print(f"""
    House value:         £{present_house_value}
    Intrest rate:        {intrest_rate_bond}%
    Repayment plan:      {months_repay_bond} Months """)

    print("\n                Amount of money you have to repay each month is: £",(round(repayment, 2)))
    print(f"Amount of money you have to repay each month is: £{(round(repayment),2)}")

else:
    print("Please enter either 'investment' or 'bond' (check for any spelling errors)")

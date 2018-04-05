# Problem 1 - Paying Debt off in a Year

# (10/10 points)
# Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the
# credit card company each month.

# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal
# monthlyPaymentRate - minimum monthly payment rate as a decimal

# For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining
# balance. Be sure to print out no more than two decimal digits of accuracy - so print

# Remaining balance: 813.41
# instead of
# Remaining balance: 813.4141998135

# So your program only prints out one thing: the remaining balance at the end of the year in the format:
# Remaining balance: 4784.0

# A summary of the required math is found below:
# Monthly interest rate= (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)



# Paste your code into this box
def calc_year(bal, annual_interest_rate, monthly_payment_rate):
    nr_of_month = 0
    monthly_interest_rate = annual_interest_rate / 12.0

    while nr_of_month < 12:
        min_monthly_pay = monthly_payment_rate * bal
        unpaid_b = bal - min_monthly_pay
        bal = round(unpaid_b + (monthly_interest_rate * unpaid_b), 2)

        nr_of_month += 1

    return bal


print(calc_year(balance, annualInterestRate, monthlyPaymentRate))
# Correct

monthly_income = input("Enter your monthly income:")
monthly_expenses = input("Enter your total monthly expenses:")
monthly_inc_int = int(monthly_income)
monthly_exp_int = int(monthly_expenses)
monthly_savings = monthly_inc_int - monthly_exp_int

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
pInt = int(projected_savings)
print("Your monthly savings are ${}.".format(monthly_savings))
print("Projected savings after one year, with interest, is: ${}.".format(pInt))
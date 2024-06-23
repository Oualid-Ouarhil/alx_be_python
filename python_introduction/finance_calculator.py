monthly_income = input("Enter your monthly income:")
monthly_expenses = input("Enter your total monthly expenses:")

monthly_savings = float(monthly_income) - float(monthly_expenses)

interest_rate = monthly_savings * 12 * 0.05
annual_savings = monthly_savings * 12
projected_savings = annual_savings + interest_rate
pInt = float(projected_savings)

print("Your monthly savings are ${}.".format(monthly_savings))
print("Projected savings after one year, with interest, is: ${}.".format(pInt))

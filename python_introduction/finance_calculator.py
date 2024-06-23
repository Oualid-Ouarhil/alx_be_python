monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your total monthly expenses: ")

monthly_income_int = int(monthly_income)
monthly_expenses_int = int(monthly_expenses)

monthly_savings = monthly_income_int - monthly_expenses_int

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
projected_savings_int = int(projected_savings)

print("Your monthly savings are ${}.".format(monthly_savings))
print("Projected savings after one year, with interest, is: ${}.".format(projected_savings_int))

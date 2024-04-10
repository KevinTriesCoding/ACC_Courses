monthly_gross_income = float(input ("What is your monthly gross income: "))
paycheck_deductions = float(input ("How much is deducted from your paycheck each month: "))

net_monthly_income = monthly_gross_income - paycheck_deductions

gross_yearly_income = monthly_gross_income * 12
net_yearly_income = net_monthly_income * 12


print(f"Your monthly net income should be: ${net_monthly_income:,.2f}")
print(f"Your monthly net income should be: ${gross_yearly_income:,.2f}")
print(f"Your monthly net income should be: ${net_yearly_income:,.2f}")
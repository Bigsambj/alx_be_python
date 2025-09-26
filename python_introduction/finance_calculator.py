# finance_calculator.py
# Repo: alx_be_python
# Directory: python_introduction

# Prompt user for financial details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project annual savings with 5% interest
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)

# Display results
print(f"Your monthly savings are ${monthly_savings:.0f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.0f}.")
# This script calculates monthly savings and projects annual savings with interest.
# It prompts the user for their income and expenses, performs calculations, and displays the results.

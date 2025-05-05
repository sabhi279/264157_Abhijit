import math

def calculate_emi(principal, annual_rate, tenure_years):
    """
    Calculate monthly EMI
    """
    if principal <= 0 or annual_rate <= 0 or tenure_years <= 0:
        raise ValueError("All inputs must be positive.")
    monthly_rate = annual_rate / (12 * 100)
    months = tenure_years * 12
    emi = (principal * monthly_rate * pow(1 + monthly_rate, months)) / (pow(1 + monthly_rate, months) - 1)
    return round(emi, 2)

def calculate_net_worth(assets, liabilities):
    """
    Net worth = assets - liabilities
    """
    if assets < 0 or liabilities < 0:
        raise ValueError("Inputs must be non-negative.")
    return round(assets - liabilities, 2)

def calculate_sip(monthly_investment, annual_rate, years):
    """
    SIP Maturity = P * ((1 + r)^n - 1) * (1 + r)/r
    """
    if monthly_investment <= 0 or annual_rate <= 0 or years <= 0:
        raise ValueError("Inputs must be positive.")
    r = annual_rate / 12 / 100
    n = years * 12
    return round(monthly_investment * (((1 + r) ** n - 1) * (1 + r)) / r, 2)

def calculate_fd(principal, annual_rate, tenure_years):
    """
    Fixed Deposit Maturity = P * (1 + r/n)^(nt)
    """
    if principal <= 0 or annual_rate <= 0 or tenure_years <= 0:
        raise ValueError("Inputs must be positive.")
    rate_per_period = annual_rate / 100
    periods = tenure_years
    maturity_amount = principal * pow(1 + rate_per_period, periods)
    return round(maturity_amount, 2)

def calculate_rd(monthly_deposit, annual_rate, months):
    """
    Recurring Deposit Maturity = P * [(1 + r/n)^(nt) - 1] / (r/n)
    """
    if monthly_deposit <= 0 or annual_rate <= 0 or months <= 0:
        raise ValueError("Inputs must be positive.")
    r = annual_rate / 12 / 100
    n = months
    maturity_amount = monthly_deposit * ((pow(1 + r, n) - 1) / r)
    return round(maturity_amount, 2)

def estimate_retirement_corpus(current_savings, monthly_addition, annual_rate, years):
    """
    Future Retirement Savings Estimate = P * (1 + r)^n + PMT * ((1 + r)^n - 1) / r
    """
    if current_savings < 0 or monthly_addition < 0 or annual_rate < 0 or years <= 0:
        raise ValueError("Inputs must be non-negative.")
    r = annual_rate / 100
    n = years
    future_savings = current_savings * pow(1 + r, n) + monthly_addition * ((pow(1 + r, n) - 1) / r)
    return round(future_savings, 2)

def estimate_home_loan_eligibility(income, expenses, credit_score):
    """
    Estimate Home Loan Eligibility
    """
    if income <= 0 or expenses < 0 or credit_score < 300 or credit_score > 850:
        raise ValueError("Invalid input values.")
    loan_eligibility = (income - expenses) * 12 * credit_score / 850
    return round(loan_eligibility, 2)

def calculate_credit_card_balance(outstanding_balance, annual_rate, months):
    """
    Outstanding Credit Card Balance with minimum payment
    """
    if outstanding_balance < 0 or annual_rate <= 0 or months <= 0:
        raise ValueError("Inputs must be non-negative.")
    monthly_rate = annual_rate / 12 / 100
    balance = outstanding_balance * pow(1 + monthly_rate, months)
    return round(balance, 2)

def calculate_taxable_income(income, deductions):
    """
    Calculate Taxable Income = Income - Deductions
    """
    if income < 0 or deductions < 0:
        raise ValueError("Inputs must be non-negative.")
    return round(income - deductions, 2)

def plan_budget(income, expenses, savings_goal):
    """
    Budget Plan: Compare Income vs Expenses and suggest savings/investment plan
    """
    if income < 0 or expenses < 0 or savings_goal < 0:
        raise ValueError("Inputs must be non-negative.")
    balance = income - expenses
    savings_suggestion = savings_goal - balance
    if savings_suggestion > 0:
        suggestion = f"Increase savings by ₹{savings_suggestion} to meet your goal."
    else:
        suggestion = "You are already on track with your savings!"
    return suggestion

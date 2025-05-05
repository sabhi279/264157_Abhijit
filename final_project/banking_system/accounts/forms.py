from django import forms

class TransactionForm(forms.Form):
    amount = forms.DecimalField(label='Amount (₹)', min_value=1.0)

from django import forms

class EMIForm(forms.Form):
    principal = forms.FloatField(min_value=1, label="Loan Amount (₹)")
    annual_rate = forms.FloatField(min_value=0.1, label="Annual Interest Rate (%)")
    tenure_years = forms.IntegerField(min_value=1, label="Loan Tenure (Years)")

class NetWorthForm(forms.Form):
    assets = forms.FloatField(min_value=0, label="Total Assets (₹)")
    liabilities = forms.FloatField(min_value=0, label="Total Liabilities (₹)")

class SIPForm(forms.Form):
    monthly_investment = forms.FloatField(min_value=1, label="Monthly Investment (₹)")
    annual_rate = forms.FloatField(min_value=0.1, label="Annual Interest Rate (%)")
    years = forms.IntegerField(min_value=1, label="Investment Period (Years)")

class FdForm(forms.Form):
    principal = forms.FloatField(min_value=1, label="FD Amount (₹)")
    annual_rate = forms.FloatField(min_value=0.1, label="Annual Interest Rate (%)")
    tenure_years = forms.IntegerField(min_value=1, label="FD Tenure (Years)")

class RdForm(forms.Form):
    monthly_deposit = forms.FloatField(min_value=1, label="Monthly Deposit (₹)")
    annual_rate = forms.FloatField(min_value=0.1, label="Annual Interest Rate (%)")
    months = forms.IntegerField(min_value=1, label="Investment Period (Months)")

class RetirementForm(forms.Form):
    current_savings = forms.FloatField(min_value=0, label="Current Savings (₹)")
    monthly_addition = forms.FloatField(min_value=1, label="Monthly Addition (₹)")
    annual_rate = forms.FloatField(min_value=0.1, label="Annual Interest Rate (%)")
    years = forms.IntegerField(min_value=1, label="Years to Retirement")


class LoanEligibilityForm(forms.Form):
    age = forms.IntegerField(label='Age (years)', min_value=18, max_value=75)
    monthly_income = forms.IntegerField(label='Monthly Income (₹)', min_value=1000)
    credit_score = forms.IntegerField(label='Credit Score (300–850)', min_value=300, max_value=850)
    loan_tenure = forms.IntegerField(label='Loan Tenure (years)', min_value=1, max_value=30)
    existing_loan = forms.IntegerField(label='Existing Loan Amount (₹)', min_value=0)
    dependents = forms.IntegerField(label='Number of Dependents', min_value=0, max_value=10)


class CreditCardForm(forms.Form):
    outstanding_balance = forms.FloatField(min_value=0, label="Outstanding Balance (₹)")
    annual_rate = forms.FloatField(min_value=0.1, label="Annual Interest Rate (%)")
    months = forms.IntegerField(min_value=1, label="Months for Payment")

class TaxableIncomeForm(forms.Form):
    income = forms.FloatField(min_value=0, label="Total Income (₹)")
    deductions = forms.FloatField(min_value=0, label="Deductions (₹)")

class BudgetForm(forms.Form):
    income = forms.FloatField(min_value=1, label="Monthly Income (₹)")
    expenses = forms.FloatField(min_value=0, label="Monthly Expenses (₹)")
    savings_goal = forms.FloatField(min_value=0, label="Savings Goal (₹)")


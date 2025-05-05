from django.test import TestCase
from django.urls import reverse
from .forms import EMIForm, NetWorthForm, SIPForm, FdForm, RdForm, RetirementForm, LoanEligibilityForm, CreditCardForm, TaxableIncomeForm, BudgetForm

class FinancialToolsTests(TestCase):

    def test_emi_calculator(self):
        url = reverse('emi')
        data = {'principal': 500000, 'annual_rate': 7.5, 'tenure_years': 10}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Monthly EMI")

    def test_sip_calculator(self):
        url = reverse('sip')
        data = {'monthly_investment': 5000, 'annual_rate': 8, 'years': 10}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "SIP Maturity Amount")

    def test_fd_calculator(self):
        url = reverse('fd')
        data = {'principal': 100000, 'annual_rate': 7, 'tenure_years': 5}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "FD Maturity Amount")

    def test_rd_calculator(self):
        url = reverse('rd')
        data = {'monthly_deposit': 3000, 'annual_rate': 7, 'months': 60}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "RD Maturity Value")

    def test_retirement_calculator(self):
        url = reverse('retirement')
        data = {'current_savings': 500000, 'monthly_addition': 10000, 'annual_rate': 8, 'years': 30}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Projected Retirement Corpus")

    def test_loan_eligibility_calculator(self):
        url = reverse('loan_eligibility')
        data = {'income': 70000, 'expenses': 30000, 'credit_score': 750}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Estimated Loan Eligibility")

    def test_credit_card_calculator(self):
        url = reverse('credit_card')
        data = {'outstanding_balance': 20000, 'annual_rate': 18, 'months': 12}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Outstanding Balance with Interest")

    def test_taxable_income_calculator(self):
        url = reverse('taxable_income')
        data = {'income': 1000000, 'deductions': 150000}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Taxable Income")

    def test_budget_planner(self):
        url = reverse('budget')
        data = {'income': 50000, 'expenses': 30000, 'savings_goal': 10000}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Suggested Savings/Investment Plan")

    def test_networth_calculator(self):
        url = reverse('networth')
        data = {'assets': 1000000, 'liabilities': 400000}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your Net Worth")

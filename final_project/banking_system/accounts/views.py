from django.shortcuts import render, redirect
from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import BankAccount
from .forms import TransactionForm
from .finance_tools import (
    calculate_emi, calculate_net_worth, calculate_sip,
    calculate_fd, calculate_rd, estimate_retirement_corpus,
    estimate_home_loan_eligibility, calculate_credit_card_balance,
    calculate_taxable_income, plan_budget
)
from .forms import (
    EMIForm, NetWorthForm, SIPForm, FdForm, RdForm,
    RetirementForm, LoanEligibilityForm, CreditCardForm,
    TaxableIncomeForm, BudgetForm
)
from django.db import IntegrityError

from .forms import LoanEligibilityForm
import joblib
import os
from django.conf import settings



model_path = os.path.join(settings.BASE_DIR, 'accounts', 'ml_models', 'loan_model.pkl')

model = joblib.load(model_path)




def home(request):
    return render(request, 'accounts/home.html')


def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')

        try:
            user = User.objects.create_user(username=username, password=password)
            BankAccount.objects.create(user=user, balance=0.0)
            return redirect('login')
        except IntegrityError:
            messages.error(request, "Registration failed.")
            return redirect('register')

    return render(request, 'accounts/register.html')



def login_user(request):
    next_url = request.POST.get('next') or request.GET.get('next') or 'dashboard'

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            print("DEBUG: Login successful")
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'accounts/login.html', {'next': next_url})






def logout_user(request):
    logout(request)
    return redirect('home')

def dashboard(request):
    print("DEBUG: Is user authenticated?", request.user.is_authenticated)
    print("DEBUG: User:", request.user)
    context = {}
    if request.user.is_authenticated:
        try:
            context['balance'] = request.user.bankaccount.balance
        except BankAccount.DoesNotExist:
            context['balance'] = None
    return render(request, 'accounts/dashboard.html', context)




@login_required
def deposit(request):
    try:
        bank_account = BankAccount.objects.get(user=request.user)
    except BankAccount.DoesNotExist:
        messages.error(request, "No bank account found.")
        return redirect('dashboard')

    if request.method == "POST":
        try:
            amount = Decimal(request.POST['amount'])
            if amount > 0:
                bank_account.balance += amount
                bank_account.save()
                return redirect('account_balance')
            else:
                return render(request, 'accounts/deposit.html', {
                    'error': 'Invalid deposit amount',
                    'bank_account': bank_account
                })
        except:
            return render(request, 'accounts/deposit.html', {
                'error': 'Please enter a valid number for deposit',
                'bank_account': bank_account
            })

    return render(request, 'accounts/deposit.html', {'bank_account': bank_account})


@login_required
def withdraw(request):
    try:
        account = BankAccount.objects.get(user=request.user)
    except BankAccount.DoesNotExist:
        messages.error(request, "No bank account found.")
        return redirect('dashboard')

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            if account.balance >= amount:
                account.balance -= amount
                account.save()
                return redirect('dashboard')
            else:
                form.add_error(None, "Insufficient balance.")
    else:
        form = TransactionForm()

    return render(request, 'accounts/withdraw.html', {'form': form, 'balance': account.balance})


@login_required
def account_balance(request):
    try:
        bank_account = BankAccount.objects.get(user=request.user)
    except BankAccount.DoesNotExist:
        bank_account = None
    return render(request, 'accounts/account_balance.html', {'bank_account': bank_account})


def emi_calculator(request):
    emi = None
    if request.method == 'POST':
        form = EMIForm(request.POST)
        if form.is_valid():
            try:
                emi = calculate_emi(**form.cleaned_data)
            except Exception as e:
                return render(request, 'accounts/emi.html', {
                    'form': form,
                    'error': str(e)
                })
    else:
        form = EMIForm()
    return render(request, 'accounts/emi.html', {'form': form, 'emi': emi})



def networth_calculator(request):
    result = None
    if request.method == 'POST':
        form = NetWorthForm(request.POST)
        if form.is_valid():
            result = calculate_net_worth(**form.cleaned_data)
    else:
        form = NetWorthForm()
    return render(request, 'accounts/networth.html', {'form': form, 'result': result})


def sip_calculator(request):
    result = None
    if request.method == 'POST':
        form = SIPForm(request.POST)
        if form.is_valid():
            result = calculate_sip(**form.cleaned_data)
    else:
        form = SIPForm()
    return render(request, 'accounts/sip.html', {'form': form, 'result': result})


def fd_calculator(request):
    result = None
    if request.method == 'POST':
        form = FdForm(request.POST)
        if form.is_valid():
            result = calculate_fd(**form.cleaned_data)
    else:
        form = FdForm()
    return render(request, 'accounts/fd.html', {'form': form, 'result': result})


def rd_calculator(request):
    result = None
    if request.method == 'POST':
        form = RdForm(request.POST)
        if form.is_valid():
            result = calculate_rd(**form.cleaned_data)
    else:
        form = RdForm()
    return render(request, 'accounts/rd.html', {'form': form, 'result': result})


def retirement_calculator(request):
    result = None
    if request.method == 'POST':
        form = RetirementForm(request.POST)
        if form.is_valid():
            result = estimate_retirement_corpus(**form.cleaned_data)
    else:
        form = RetirementForm()
    return render(request, 'accounts/retirement.html', {'form': form, 'result': result})




def loan_eligibility_calculator(request):
    result = None
    if request.method == 'POST':
        form = LoanEligibilityForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            features = [[
                data['age'],
                data['monthly_income'],
                data['credit_score'],
                data['loan_tenure'],
                data['existing_loan'],
                data['dependents'],
            ]]
            prediction = model.predict(features)[0]
            result = round(prediction)
    else:
        form = LoanEligibilityForm()
    return render(request, 'accounts/loan_eligibility.html', {'form': form, 'result': result})



def credit_card_calculator(request):
    result = None
    if request.method == 'POST':
        form = CreditCardForm(request.POST)
        if form.is_valid():
            result = calculate_credit_card_balance(**form.cleaned_data)
    else:
        form = CreditCardForm()
    return render(request, 'accounts/credit_card.html', {'form': form, 'result': result})


def taxable_income_calculator(request):
    result = None
    if request.method == 'POST':
        form = TaxableIncomeForm(request.POST)
        if form.is_valid():
            result = calculate_taxable_income(**form.cleaned_data)
    else:
        form = TaxableIncomeForm()
    return render(request, 'accounts/taxable_income.html', {'form': form, 'result': result})


def budget_planner(request):
    result = None
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            result = plan_budget(**form.cleaned_data)
    else:
        form = BudgetForm()
    return render(request, 'accounts/budget.html', {'form': form, 'result': result})




#addition
from django.http import HttpResponse

def test_session(request):
    if request.user.is_authenticated:
        return HttpResponse(f"✅ Logged in as {request.user.username}")
    else:
        return HttpResponse("❌ Not logged in")
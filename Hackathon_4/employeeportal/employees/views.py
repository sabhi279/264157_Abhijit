from django.shortcuts import render
import random

def salary_form(request):
    return render(request, 'employees/salary_form.html')

# function for calculating the salary
def calculate_salary(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        company = request.POST.get('company')
        gross_salary = float(request.POST.get('gross_salary'))
        tax = float(request.POST.get('tax'))
        bonus = float(request.POST.get('bonus'))

        net_salary = gross_salary + (gross_salary * (bonus/100)) - (gross_salary * (tax/100))

        context = {
            'name': name,
            'net_salary': net_salary
        }
        return render(request, 'employees/salary_result.html', context)
    return render(request, 'employees/salary_form.html')


# function for JUMBLE WORD 
def jumble_word(request):
    jumbled = ''
    if request.method == 'POST':
        word = request.POST.get('word')
        jumbled = ''.join(random.sample(word, len(word)))

    return render(request, 'employees/jumble_word.html', {'jumbled': jumbled})

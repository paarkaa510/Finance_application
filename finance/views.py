from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from finance_application.forms import GoalForm, IncomeForm , ExpenseForm, SavingsForm
from finance.models import Goals,Income,Expenses,Savings
from django.db.models import Sum
from django.shortcuts import get_object_or_404

#goal app
@login_required
def create_goal(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('home')  
    else:
        form = GoalForm()
    return render(request, 'create_goal.html', {'form': form})


@login_required
def delete_goal(request, goal_id):
    goal = get_object_or_404(Goals, id=goal_id, user=request.user)
    goal.delete()
    return redirect('home')


#income app
@login_required
def create_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            user = request.user
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            incomes = Income.objects.filter(user=user)
            return render(request, 'incomes_home.html', {'incomes': incomes}) 
    else:
        form = IncomeForm()
    return render(request, 'create_income.html', {'form': form})

@login_required
def user_incomes(request):
    user = request.user
    incomes = Income.objects.filter(user=user)
    return render(request, 'incomes_home.html', {'incomes': incomes})

@login_required
def delete_income(request, income_id):
    income = get_object_or_404(Income, id=income_id, user=request.user)
    user = request.user
    user_id = user.id
    incomes = Income.objects.filter(user_id=user_id)
    if request.method == "POST":
        income.delete()
        return render(request, 'incomes_home.html', {'incomes':incomes})
    return render(request, 'incomes_home.html', {'incomes': incomes})

@login_required
def update_income(request, income_id):
    income = get_object_or_404(Income, id=income_id, user=request.user)
    user = request.user
    user_id = user.id
    incomes = Income.objects.filter(user_id=user_id)
    if request.method == 'POST':
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            return render(request, 'incomes_home.html', {'incomes': incomes})
    else:
        form = IncomeForm(instance=income)
    return render(request, 'update_income.html', {'form': form})

#expenses app
@login_required
def create_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            user = request.user
            expense = form.save(commit=False)
            expense.user = user
            expense.save()
            return redirect('home') 
    else:
        form = ExpenseForm()
        
    return render(request, 'create_expense.html', {'form': form})

@login_required
def user_expenses(request):
    user = request.user
    user_id = user.id
    expenses = Expenses.objects.filter(user_id=user_id)
    return render(request, 'expense_home.html', {'expenses': expenses})

@login_required
def delete_expense(request, expense_id):
    expense = get_object_or_404(Expenses, id=expense_id, user=request.user)
    user = request.user
    user_id = user.id
    expenses = Expenses.objects.filter(user_id=user_id)
    if request.method == "POST":
        expense.delete()
        return render(request, 'expense_home.html', {'expenses':expenses})
    return render(request, 'expense_home.html', {'expenses': expenses})

@login_required
def update_expense(request, expense_id):
    expense = get_object_or_404(Expenses, id=expense_id, user=request.user)
    user = request.user
    user_id = user.id
    expenses = Expenses.objects.filter(user_id=user_id)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return render(request, 'expense_home.html', {'expenses': expenses})
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'update_expense.html', {'form': form})



#savings app
@login_required
def create_savings(request):
    if request.method == 'POST':
        form = SavingsForm(request.POST)
        if form.is_valid():
            user = request.user
            savings = form.save(commit=False)
            savings.user = user
            savings.save()
            savings = Savings.objects.filter(user=user)
            return render(request, 'saving_home.html', {'savings': savings}) 
    else:
        form = SavingsForm()
    return render(request, 'create_saving.html', {'form': form})

@login_required
def user_savings(request):
    user = request.user
    savings = Savings.objects.filter(user=user)
    return render(request, 'saving_home.html', {'savings': savings})

@login_required
def delete_savings(request, saving_id):
    saving = get_object_or_404(Savings, id=saving_id, user=request.user)
    user = request.user
    user_id = user.id
    savings = Savings.objects.filter(user_id=user_id)
    if request.method == "POST":
        saving.delete()
        return render(request, 'saving_home.html', {'savings':savings})
    return render(request, 'saving_home.html', {'savings': savings})

@login_required
def update_saving(request, saving_id):
    saving = get_object_or_404(Savings, id=saving_id, user=request.user)
    user = request.user
    user_id = user.id
    savings = Savings.objects.filter(user_id=user_id)
    if request.method == 'POST':
        form = SavingsForm(request.POST, instance=saving)
        if form.is_valid():
            form.save()
            return render(request, 'saving_home.html', {'savings': savings})
    else:
        form = SavingsForm(instance=saving)
    return render(request, 'update_saving.html', {'form': form})


#GOALS
@login_required
def user_goals(request):
    user = request.user
    goals = Goals.objects.filter(user=user)
    total_income = Income.objects.filter(user=user).aggregate(Sum('monthly_salary'), Sum('other_income'))
    monthly_salary_sum = total_income['monthly_salary__sum']
    other_income_sum = total_income['other_income__sum']
    total_income_sum = (monthly_salary_sum if monthly_salary_sum else 0) + (other_income_sum if other_income_sum else 0)
    expenses = Expenses.objects.filter(user_id=user)
    return render(request, 'home.html', {'goals': goals, 'total_income_sum': total_income_sum,'expenses': expenses })


@login_required
def home(request):
    return render(request, 'home.html')
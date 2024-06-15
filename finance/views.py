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
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            return redirect('home')  
    else:
        form = IncomeForm()

    return render(request, 'create_income.html', {'form': form})

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


#savings app
@login_required
def create_saving(request):
    if request.method == 'POST':
        form = SavingsForm(request.POST)
        if form.is_valid():
            user = request.user
            savings = form.save(commit=False)
            savings.user = user
            savings.save()
            savings = Savings.objects.filter(user=user)
            return redirect('home') 
    else:
        form = SavingsForm()
    return render(request, 'create_saving.html', {'form': form})





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
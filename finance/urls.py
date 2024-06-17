from django.urls import path
from .views import *


app_name = 'finance'

urlpatterns = [
    path("", home, name="home"),
    path('user-goals/', user_goals, name='user-goals'), 
    path("create-goal/", create_goal, name="create_goal"),
    path('delete-goal/<int:goal_id>/', delete_goal, name='delete_goal'),
    path('update-goal/<int:goal_id>/', update_goal, name='update_goal'),

    path('user-income', user_incomes , name='user-income'),
    path("create-income/", create_income, name="create_income"),
    path('delete-income/<int:income_id>/', delete_income, name='delete_income'),
    path('update-income/<int:income_id>/', update_income, name='update_income'),


    path('user-expenses/', user_expenses, name='expense_home'),
    path("create-expense/", create_expense, name="create_expense"),
    path('delete-expense/<int:expense_id>/', delete_expense, name='delete_expense'),
    path('update-expense/<int:expense_id>/', update_expense, name='update_expense'),

    path('user-savings', user_savings , name='user-savings'),
    path('create-savings/', create_savings, name='create_saving'),
    path('delete-savings/<int:saving_id>/', delete_savings, name='delete_savings'),
    path('update-saving/<int:saving_id>/', update_saving, name='update_saving'),
]

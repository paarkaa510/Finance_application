
from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView  
from finance.views import *




urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("users.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    

    path("", user_goals, name="home"),

    path("create-goal/", create_goal, name="create_goal"),
    path('delete-goal/<int:goal_id>/', delete_goal, name='delete_goal'),

    path("create-income/", create_income, name="create_income"),

    path('user-expenses/', user_expenses, name='expense_home'),
    path("create-expense/", create_expense, name="create_expense"),
    path('delete-expense/<int:expense_id>/', delete_expense, name='delete_expense'),
    path('update-expense/<int:expense_id>/', update_expense, name='update_expense'),

    path("create-saving/", create_saving, name="create_saving"),
]

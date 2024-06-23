from django.test import TestCase
from django.contrib.auth.models import User
from finance.models import Goals, Income, Expenses, Savings
from decimal import Decimal
from datetime import date

class ModelsTestCase(TestCase):

    """
    Test case for testing the models in the finance application.

    This test case covers:
    - Creating and saving Goals, Income, Expenses, and Savings instances.
    - Ensuring that the fields are correctly saved.
    - Validating that negative amounts raise a ValueError.
    """


    def setUp(self):
        self.user = User.objects.create_user(username='testing1', password='%RDX$ESZ5rdx4esz')

    def test_goals_save(self):
        goal = Goals(user=self.user, name='Test Goal', target_amount=Decimal('100.00'), current_amount=Decimal('50.00'), target_date=date.today())
        goal.save()
        self.assertEqual(goal.name, 'Test Goal')

    def test_income_save(self):
        income = Income(user=self.user, monthly_salary=Decimal('5000.00'), other_income=Decimal('1000.00'))
        income.save()
        self.assertEqual(income.monthly_salary, Decimal('5000.00'))

    def test_expenses_save(self):
        expense = Expenses(user=self.user, amount=Decimal('200.00'), description='Test Expense', category='Test Category')
        expense.save()
        self.assertEqual(expense.description, 'Test Expense')

    def test_savings_save(self):
        saving = Savings(user=self.user, amount=Decimal('3000.00'))
        saving.save()
        self.assertEqual(saving.amount, Decimal('3000.00'))

    def test_negative_amounts(self):
        with self.assertRaises(ValueError):
            goal = Goals(user=self.user, name='Test Goal', target_amount=Decimal('-100.00'), current_amount=Decimal('50.00'), target_date=date.today())
            goal.save()

        with self.assertRaises(ValueError):
            income = Income(user=self.user, monthly_salary=Decimal('-5000.00'), other_income=Decimal('1000.00'))
            income.save()

        with self.assertRaises(ValueError):
            expense = Expenses(user=self.user, amount=Decimal('-200.00'), description='Test Expense', category='Test Category')
            expense.save()
        
        with self.assertRaises(ValueError):
            goal = Goals(name="Test", current_amount=-10, target_amount=100)
            goal.save()

from django.test import TestCase
from django.contrib.auth.models import User
from finance.models import Goals, Income, Expenses, Savings
from decimal import Decimal
from datetime import date, timedelta
from django.utils import timezone


class ModelsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testing1', password='%RDX$ESZ5rdx4esz')

    def test_goals_save(self):
        goal = Goals(user=self.user, name='Test Goal', target_amount=Decimal('100.00'), current_amount=Decimal('50.00'), target_date=date.today())
        goal.save()
        self.assertEqual(goal.name, 'Test Goal')

    def test_goals_target_amount(self):
        with self.assertRaises(ValueError):
            goal = Goals(user=self.user, name='Test Goal', target_amount=Decimal('100.00'), current_amount=Decimal('500.00'), target_date=date.today())
            goal.save()

    def test_goal_string_representation(self):
        goal = Goals.objects.create(
            user=self.user,
            name='Save for a car',
            target_amount=65000.00,
            current_amount=5000.00,
            target_date='2024-12-31'
        )
        self.assertEqual(str(goal), 'Save for a car')

    def test_income_save(self):
        income = Income(user=self.user, monthly_salary=Decimal('5000.00'), other_income=Decimal('1000.00'))
        income.save()
        self.assertEqual(income.monthly_salary, Decimal('5000.00'))

    def test_expenses_save(self):
        expense = Expenses(user=self.user, amount=Decimal('200.00'), description='Test Expense', category='Test Category')
        expense.save()
        self.assertEqual(expense.description, 'Test Expense')

    def test_expenses_updated_at_field(self):
        expense = Expenses(user=self.user, amount=100.0, description="Test Expense")
        expense.save()
        expense.amount = 150.0
        expense.save()
        updated_expense = Expenses.objects.get(id=expense.id)
        new_time = timezone.now()
        tolerance = timedelta(milliseconds=2)
        self.assertTrue(abs(updated_expense.updated_at - new_time) < tolerance, 
                        f"updated_at is not within the tolerance range. updated_at: {updated_expense.updated_at}, new_time: {new_time}")

    def test_expenses_string_representation(self):
        expense = Expenses.objects.create(
            user=self.user,
            amount=Decimal('15.00'),
            description='Dinner',
            category='Food',
            created_at=timezone.now(),
            updated_at=timezone.now()
        )
        self.assertEqual(str(expense), '$15.00 for Dinner')


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

from django.db import models 
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


#goals
class Goals(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2)
    percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0, blank=True, null=True)
    target_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        if not self.name:
            raise ValueError("There must be a name for the goal.")
        if self.current_amount < 0:
            raise ValueError("Current amount cannot be below $0.")
        if self.target_amount < 0:
            raise ValueError("Goal amount cannot be below $0.")
        if self.target_amount < self.current_amount:
            raise ValueError("Current amount cannot be greater than target amount")
        super(Goals, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

#income
class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    monthly_salary = models.DecimalField(max_digits=10, decimal_places=2)
    other_income = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.monthly_salary < 0:
            raise ValueError("Monthly salary cannot be below $0.")
        if self.other_income < 0:
            raise ValueError("Other income cannot be below $0.")
        super(Income, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username}'s income"
    
#expenses

CATEGORY_CHOICES = [
    ('Housing', 'Housing'),
    ('Utilities', 'Utilities'),
    ('Food', 'Food'),
    ('Loans', 'Loans'),
    ('Insurance', 'Insurance'),
    ('Subscription', 'Subscription'),
    ('Other', 'Other'),
]

class Expenses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.CharField(max_length=400)
    category = models.CharField(max_length=40, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.amount < 0:
            raise ValueError("Expense amount cannot be below $0.")
        super(Expenses, self).save(*args, **kwargs)
        
    def __str__(self):
        return f"${self.amount} for {self.description}"
    
#savings
class Savings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if isinstance(self.amount, str):
            try:
                self.amount = float(self.amount)
            except ValueError:
                raise ValidationError("Amount must be a number.")
        if self.amount < 0:
            raise ValueError("Savings amount cannot be below $0.")
        super(Savings, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username} - {self.amount:.2f}'


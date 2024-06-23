from django.db import models 
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


#goals
class Goals(models.Model):

    """
    Model to represent a financial goal for a user.
    
    Attributes:
        user (ForeignKey): The user who owns this goal.
        name (CharField): The name of the goal.
        target_amount (DecimalField): The target amount of money to be saved.
        current_amount (DecimalField): The current amount of money saved towards the goal.
        target_date (DateField): The date by which the goal should be achieved.
        created_at (DateTimeField): The timestamp when the goal was created.
        updated_at (DateTimeField): The timestamp when the goal was last updated.
    """
     
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2)
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
        super(Goals, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

#income
class Income(models.Model):

    """
    Model to represent a user's income.
    
    Attributes:
        user (ForeignKey): The user who owns this income record.
        monthly_salary (DecimalField): The user's monthly salary.
        other_income (DecimalField): Any other income of the user.
        created_at (DateTimeField): The timestamp when the income record was created.
        updated_at (DateTimeField): The timestamp when the income record was last updated.
    """

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
    ('Leisure', 'Leisure'),
    ('Other', 'Other'),
]

class Expenses(models.Model):

    """
    Model to represent a user's expense.
    
    Attributes:
        user (ForeignKey): The user who owns this expense record.
        amount (DecimalField): The amount of the expense.
        description (CharField): The description of the expense.
        category (CharField): The category of the expense.
        created_at (DateTimeField): The timestamp when the expense record was created.
        updated_at (DateTimeField): The timestamp when the expense record was last updated.
    """

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

    """
    Model to represent a user's savings.
    
    Attributes:
        user (ForeignKey): The user who owns this savings record.
        amount (DecimalField): The amount of the savings.
        created_at (DateTimeField): The timestamp when the savings record was created.
        updated_at (DateTimeField): The timestamp when the savings record was last updated.
    """

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


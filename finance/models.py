from django.db import models # type: ignore
from django.contrib.auth.models import User


#goals
class Goals(models.Model):
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
from django import forms
from finance.models import Goals,Income,Expenses,Savings
from datetime import date

#goals form
class GoalForm(forms.ModelForm):
    target_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'min': date.today().strftime('%Y-%m-%d')}),
        initial=date.today,
    )
    class Meta:
        model = Goals
        fields = ['name', 'target_amount', 'current_amount', 'target_date']

    def clean_target_date(self):
        target_date = self.cleaned_data['target_date']
        if target_date < date.today():
            raise forms.ValidationError("The target date cannot be in the past.")
        return target_date
#income form
class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['monthly_salary', 'other_income']

    def clean(self):
        cleaned_data = super().clean()
        monthly_salary = cleaned_data.get('monthly_salary')
        other_income = cleaned_data.get('other_income')

        if monthly_salary is not None and monthly_salary < 0:
            self.add_error('monthly_salary', "Monthly salary cannot be negative.")
        
        if other_income is not None and other_income < 0:
            self.add_error('other_income', "Other income cannot be negative.")

#expense form
class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ['amount', 'description', 'category']

#savings form
class SavingsForm(forms.ModelForm):
    class Meta:
        model = Savings
        fields = ['amount']
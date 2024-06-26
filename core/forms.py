from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['transaction_type', 'amount', 'description']
        widgets = {
            'transaction_type': forms.Select(attrs={'class': 'form-select  mt-1'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control mt-1', 'placeholder': 'Enter amount'}),
            'description': forms.TextInput(attrs={'class': 'form-control mt-1', 'placeholder': 'Enter description'}),
        }
        labels = {
            'transaction_type': 'Transaction Type',
            'amount': 'Amount',
            'description': 'Description',
        }
        help_texts = {
            'transaction_type': 'Select the type of transaction',
            'amount': 'Enter the amount for the transaction',
            'description': 'Provide a brief description of the transaction',
        }
"""
	def clean_amount(self):
		amount = self.cleaned_data.get('amount')
		if amount <= 0:
			raise forms.ValidationError('The amount must be greater than zero.')
		return amount

	"""

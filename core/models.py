from django.db import models
from django.contrib.auth.models import User

class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.username}'s Wallet"

class Transaction(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255)
    TRANSACTION_TYPES = [
        ('deposit', 'Deposit'),
        ('withdrawal', 'Withdrawal'),
    ]
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)

    def __str__(self):
        return f"{self.transaction_type} of {self.amount} on {self.timestamp}"



class Guard(models.Model):
    wallet = models.OneToOneField(Wallet, on_delete=models.CASCADE)
    max_transaction_limit = models.DecimalField(max_digits=10, decimal_places=2, default=1000.00)
    notification_email = models.EmailField()

    def __str__(self):
        return f"Guard settings for {self.wallet.user.username}'s Wallet"


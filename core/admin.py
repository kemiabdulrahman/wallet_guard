from django.contrib import admin
from core.models import Guard, Transaction, Wallet

admin.site.register(Wallet)
admin.site.register(Guard)
admin.site.register(Transaction)

from django.urls import path
from .views import wallet_detail, make_transaction

app_name = 'wallet'

urlpatterns = [
    path('wallet/', wallet_detail, name='wallet_detail'),
    path('wallet/transaction/', make_transaction, name='make_transaction'),
]


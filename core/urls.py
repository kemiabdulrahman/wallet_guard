from django.urls import path
from .views import wallet_detail, make_transaction, register # , update_profile, upgrade_tier, login_view

app_name = 'wallet'

urlpatterns = [

    path('create-user/', register, name='create-user'),
#    path('login/', login_view, name='login'),
#    path('update-profile/', update_profile, name='profile'),
#    path('upgrade-tier/', upgrade_tier, name='upgrade-tier'),
    path('wallet/', wallet_detail, name='wallet_detail'),
    path('wallet/transaction/', make_transaction, name='make_transaction'),
]

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Wallet, Transaction
from .forms import TransactionForm, RegisterForm


def register(request):
    form = RegisterForm(request.POST or None)
    data = {}
    if request.is_ajax:
        if form.is_valid():
            form.save()
            data['username'] = form.cleaned_data.get('username')
            return JsonResponse(data, status=200)
        else:
            return JsonResponse({'error': form.errors}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)


"""
def login_view(request):
    form = LoginForm(request.POST or None)
    data = {}
    if request.is_ajax:
        if form.is_valid():
            form.save()
            pass


def upgrade_tier(request):
    form = RegisterForm(request.POST or None)
    if request.is_ajax:
        if form.is_valid():
            form.save()
            pass

def update_profile(request):
    form = RegisterForm(request.POST or None)
    data = {}
    if request.is_ajax:
        if form.is_valid():
            form.save()
            data['username'] = form.cleaned_data.get('username')
            return JsonResponse(data, status=200)
        else:
            return JsonResponse({'error': form.errors}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)
"""

# @login_required
def wallet_detail(request):
    wallet = request.user.wallet
    form = TransactionForm()
    register_form = RegisterForm()
    transactions = Transaction.objects.filter(wallet=wallet).order_by('-timestamp')
    return render(request, 'home.html', {'wallet': wallet, 'transactions': transactions, 'form': form, 'register_form': register_form })


@login_required
def make_transaction(request):
        form = TransactionForm(request.POST or None)
        data = {}
        if request.is_ajax():
            if form.is_valid():
                transaction = form.save(commit=False)
                transaction.wallet = request.user.wallet
                if transaction.transaction_type == "deposit":
                    request.user.wallet.balance += transaction.amount
                    request.user.wallet.save()
                    transaction.save()
                    data["amount"] = form.cleaned_data.get('amount')
                    data["description"] = form.cleaned_data.get('description')
                    data["transaction_type"] = form.cleaned_data.get('transaction_type')
                    data["timestamp"] =  transaction.timestamp.strftime('%Y-%m-%d %H:%M:%S')
                    data["balance"] = request.user.wallet.balance
                    return JsonResponse(data, status=200)
                elif transaction.transaction_type == "withdrawal":
                    request.user.wallet.balance -= transaction.amount
                    request.user.wallet.save()
                    transaction.save()
                    data["amount"] = form.cleaned_data.get('amount')
                    data["description"] = form.cleaned_data.get('description')
                    data["transaction_type"] = form.cleaned_data.get('transaction_type')
                    data["timestamp"] =  transaction.timestamp.strftime('%Y-%m-%d %H:%M:%S')
                    data["balance"] = request.user.wallet.balance
                    return JsonResponse(data, status=200)
        else:
            return JsonResponse({'error': form.errors}, status=400)
        return JsonResponse({'error': 'Invalid request'}, status=400)


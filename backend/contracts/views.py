from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
import contracts
from utils import contract
from .models import Account

# Create your views here.
class IndexView(TemplateView):
    template_name = 'contracts/index.html'

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data()
        ether_price = contract.call_function('getThePrice()')
        tot_sup = contract.call_function('totalSupply()')

        context['ether_price'] = ether_price / 10 ** 8
        context['tot_sup'] = tot_sup / 10 ** 5

        accounts = []

        for account in Account.objects.all():
            account.ethers = contract.get_balance(account.address) / 10 ** 18
            account.tokens = contract.call_function('balanceOf(address)', account.address) / 10 ** 5
            accounts.append({
                'name': account.name,
                'ethers': account.ethers,
                'tokens': account.tokens
            })
            account.save()

        context['accounts'] = accounts
        
        return context

class TransactView(TemplateView):
    template_name = 'contracts/index.html'

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data()
        ether_price = contract.call_function('getThePrice()')
        tot_sup = contract.call_function('totalSupply()')

        context['ether_price'] = ether_price / 10 ** 8
        context['tot_sup'] = tot_sup / 10 ** 5

        contract.transact('deposit()')
        
        accounts = []
        for account in Account.objects.all():
            account.ethers = contract.get_balance(account.address) / 10 ** 18
            account.tokens = contract.call_function('balanceOf(address)', account.address) / 10 ** 5
            accounts.append({
                'name': account.name,
                'ethers': account.ethers,
                'tokens': account.tokens
            })
            account.save()

        context['accounts'] = accounts
        
        return context

from django.shortcuts import render
from django.views.generic import ListView
from .models import *

class AccountsListView(ListView):
	model = User
	template = 'accounts/accounts_list.html'

	def get_queryset(self):
		accounts = User.objects.filter(is_staff=False)
		return accounts
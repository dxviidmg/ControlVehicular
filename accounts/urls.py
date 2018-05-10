from .views import *
from django.urls import path

app_name = "accounts"

urlpatterns = [
	path('accounts/', AccountsListView.as_view(), name='accounts-list'),
]
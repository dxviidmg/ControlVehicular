from .views import *
from django.urls import path
from django.contrib.auth.views import login, logout

app_name = "accounts"

urlpatterns = [
	path('login/', login, name='login'),
	path('logout/', logout, name='logout'),
	path('accounts/', AccountsListView.as_view(), name='accounts-list'),
]
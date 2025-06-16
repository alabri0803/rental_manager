from django.urls import path
from .views import contract_list, add_contract

urlpatterns = [
  path('', contract_list, name='contract_list'),
  path('add/', add_contract, name='add_contract'),
]
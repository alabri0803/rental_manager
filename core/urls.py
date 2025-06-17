from django.urls import path

from .views import (
  add_contract,
  contract_delete,
  contract_detail,
  contract_edit,
  contract_list,
)

urlpatterns = [
  path('', contract_list, name='contract_list'),
  path('add/', add_contract, name='add_contract'),
  path('<int:pk>/', contract_detail, name='contract_detail'),
  path('<int:pk>/edit/', contract_edit, name='contract_edit'),
  path('<int:pk>/delete/', contract_delete, name='contract_delete'),
]
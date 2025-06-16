from django.shortcuts import render
from .models import RentalContract

def contract_list(request):
  contracts = RentalContract.objects.all()
  return render(request, 'core/contract_list.html', {'contracts': contracts})
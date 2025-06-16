from django.shortcuts import render, redirect
from .models import RentalContract
from .forms import RentalContractForm

def contract_list(request):
  contracts = RentalContract.objects.all()
  return render(request, 'core/contract_list.html', {'contracts': contracts})

def add_contract(request):
  if request.method == 'POST':
    form = RentalContractForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('contract_list')
  else:
    form = RentalContractForm()
  return render(request, 'core/add_contract.html', {'form': form})
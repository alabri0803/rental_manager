from typing import Counter

from django.contrib import messages
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import gettext as _

from .forms import RentalContractForm
from .models import PropertyType, RentalContract


def contract_list(request):
  contracts = RentalContract.objects.all()
  # عقود حسب النوع
  type_counts = contracts.values('property_type').annotate(count=Count('id'))
  types_data = {
    0: _('محل تجاري'),
    0: _('سكن'),
    0: _('شركة'),
  }
  for item in type_counts:
    label = dict(PropertyType.choices)[item['property_type']]
    types_data[label] += item['count']
  # عقود حسب الحالة
  status_counts = Counter(contract.status for contract in contracts)
  status_labels = {
    'active': _('نشط'),
    'near_expiry': _('قريب الانتهاء'),
    'expired': _('منتهي'),
  }
  status_data = {status_labels[k]: status_counts.get(k, 0) for k in ['active', 'near_expiry', 'expired']}
  context = {
    'contracts': contracts,
    'types_labels': list(types_data.keys()),
    'types_values': list(types_data.values()),
    'status_labels': list(status_data.keys()),
    'status_values': list(status_data.values()),
  }
  return render(request, 'core/contract_list.html', context)

def add_contract(request):
  if request.method == 'POST':
    form = RentalContractForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('contract_list')
  else:
    form = RentalContractForm()
  return render(request, 'core/add_contract.html', {'form': form})

def contract_detail(request, pk):
  contract = get_object_or_404(RentalContract, pk=pk)
  return render(request, 'core/contract_detail.html', {'contract': contract})

def contract_edit(request, pk):
  contract = get_object_or_404(RentalContract, pk=pk)
  if request.method == 'POST':
    form = RentalContractForm(request.POST, instance=contract)
    if form.is_valid():
      form.save()
      messages.success(request, "تم تعديل العقد بنجاح")
      return redirect('contract_list')
  else:
    form = RentalContractForm(instance=contract)
  return render(request, 'core/add_contract.html', {'form': form, 'contract': contract, 'edit': True})

def contract_delete(request, pk):
  contract = get_object_or_404(RentalContract, pk=pk)
  if request.method == 'POST':
    contract.delete()
    messages.success(request, "تم حذف العقد بنجاح")
    return redirect('contract_list')
  return render(request, 'core/contract_confirm_delete.html', {'contract': contract})
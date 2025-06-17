from django import forms
from django.utils.translation import gettext_lazy as _

from .models import RentalContract


class RentalContractForm(forms.ModelForm):
  class Meta:
    model = RentalContract
    fields = ['name', 'property_type', 'monthly_rent', 'start_date', 'end_date']
    labels = {
      'name': _('اسم المستأجر'),
      'property_type': _('نوع العقار'),
      'monthly_rent': _('الايجار الشهري'),
      'start_date': _('تاريخ بداية العقد'),
      'end_date': _('تاريخ نهاية العقد'),
    }
    widgets = {
      'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
      'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
      'name': forms.TextInput(attrs={'class': 'form-control'}),
      'property_type': forms.TextInput(attrs={'class': 'form-select'}),
      'monthly_rent': forms.NumberInput(attrs={'class': 'form-control'}),
    }
from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import date

class PropertyType(models.TextChoices):
  COMMERCIAL = 'commercial', _('محل تجاري')
  RESIDENTIAL = 'residential', _('سكن')
  COMPANY = 'company', _('شركة')

class RentalContract(models.Model):
  name = models.CharField(max_length=100, verbose_name=_('اسم المستأجر'))
  property_type = models.CharField(max_length=20, choices=PropertyType.choices, verbose_name=_('نوع العقار'))
  monthly_rent = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('الايجار الشهري'))
  start_date = models.DateField(verbose_name=_('تاريخ بداية العقد'))
  end_date = models.DateField(verbose_name=_('تاريخ نهاية العقد'))
  created_at = models.DateTimeField(auto_now_add=True)

  @property
  def total_fee(self):
    return (self.monthly_rent * 12 * 0.03) + 5 + 1

  @property
  def days_remaining(self):
    return (self.end_date - date.today()).days

  @property
  def status(self):
    if self.days_remaining > 0:
      return 'expired'
    elif self.days_remaining <= 30:
      return 'near_expiration'
    return 'active'

  def __str__(self):
    return f"{self.name} - {self.get_property_type_display()}"
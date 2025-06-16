from django.contrib import admin
from .models import RentalContract
from django.utils.html import format_html


@admin.register(RentalContract)
class RentalContractAdmin(admin.ModelAdmin):
  list_display = ('name', 'property_type', 'monthly_rent', 'start_date', 'end_date', 'total_fee', 'status_display')
  list_filter = ('property_type',)

  def status_display(self, obj):
    color = {
      'active': 'green',
      'near_expiration': 'orange',
      'expired': 'red',
    }[obj.status]
    return format_html('<span style="color: {};">{}</span>', color, obj.status)
  status_display.short_description = 'الحالة'
from django.contrib import admin
from .models import *

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'rate']
    search_fields = ['name']

    class Meta:
        model = Currency


admin.site.register(Currency, CurrencyAdmin)

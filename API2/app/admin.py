from django.contrib import admin
from .models import Company

class CommapnyAdmin(admin.ModelAdmin):
  list_display = ['company_name','location']

admin.site.register(Company, CommapnyAdmin)
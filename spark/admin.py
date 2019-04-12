from django.contrib import admin

from .models import Company, Analysis, Inputs

# Register your models here.
admin.site.register(Company)
admin.site.register(Analysis)
admin.site.register(Inputs)


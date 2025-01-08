from django.contrib import admin
from .models import CustomerModel

# Register your models here.


@admin.register(CustomerModel)
class CustomerModelAdmin(admin.ModelAdmin):
    pass
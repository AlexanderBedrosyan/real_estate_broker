from django.contrib import admin
from .models import CustomerModel, Contact

# Register your models here.


@admin.register(CustomerModel)
class CustomerModelAdmin(admin.ModelAdmin):
    pass

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass
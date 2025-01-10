from django.contrib import admin
from .models import Customer, Address, ContactNote

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'date_created')
    search_fields = ('first_name', 'last_name', 'email')

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('customer', 'city', 'state', 'country')

@admin.register(ContactNote)
class ContactNoteAdmin(admin.ModelAdmin):
    list_display = ('customer', 'note', 'date_created')

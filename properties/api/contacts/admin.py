from django.contrib import admin
from properties.api.contacts.models import ContactModel

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject', 'message')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'subject', 'message')
    list_per_page = 25

admin.site.register(ContactModel, ContactAdmin)

# Register your models here.

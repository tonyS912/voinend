from django.contrib import admin

from .models import Contacts


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'phone')


admin.site.register(Contacts, ContactsAdmin)

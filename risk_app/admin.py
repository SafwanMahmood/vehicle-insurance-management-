from django.contrib import admin

# Register your models here.

from .models import Person,Customer

admin.site.register(Person)
admin.site.register(Customer)
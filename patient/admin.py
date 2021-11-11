from django.contrib import admin

from .models import Animal, Breed, Patient
# Register your models here.
admin.site.register(Animal)
admin.site.register(Breed)
admin.site.register(Patient)

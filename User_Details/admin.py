from django.contrib import admin

# Register your models here.
from .models import CustomUser,StoredData

admin.site.register(CustomUser)
admin.site.register(StoredData)
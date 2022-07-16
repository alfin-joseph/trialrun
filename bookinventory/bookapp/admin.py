from django.contrib import admin
from .models import CustomUser,Store,Book

admin.site.register(CustomUser)
admin.site.register(Store)
admin.site.register(Book)

# Register your models here.

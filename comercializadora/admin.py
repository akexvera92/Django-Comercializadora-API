from django.contrib import admin
# Register your models here.
from .models import Cafeteria

class CafeteriaAdmin(admin.ModelAdmin):
    list_display = (
        "clasificacion",
        "producto",
        "marca",
        "precio",
        "image",
    )
admin.site.register(Cafeteria,CafeteriaAdmin)

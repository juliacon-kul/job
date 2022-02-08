from django.contrib import admin
from app.models import Element

# Register your models here.
@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):
    pass

# @admin.register(Data)
# class DataAdmin(admin.ModelAdmin):
#     pass







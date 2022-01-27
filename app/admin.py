from django.contrib import admin
from app.models import Element, ElementData

# Register your models here.
@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):
    pass


@admin.register(ElementData)
class ElementDataAdmin(admin.ModelAdmin):
    pass







from django.contrib import admin

from car.models import Car, Category, Manufacturer


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created", "updated")
    ordering = ["id"]


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("name", "created", "updated")
    ordering = ["id"]


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "created", "updated")
    ordering = ["id"]

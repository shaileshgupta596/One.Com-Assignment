from django.contrib import admin
from restaurent.models import Order, FoodItem

# Register your models here.

@admin.register(Order)
class OrderAdminForm(admin.ModelAdmin):
    pass


@admin.register(FoodItem)
class FoodItemAdminForm(admin.ModelAdmin):
    pass

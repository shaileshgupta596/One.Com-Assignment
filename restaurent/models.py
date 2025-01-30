import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class FoodItem(models.Model):

    class FoodType(models.TextChoices):
        INDIAN = "IN", "Indian"
        CHINESE = "CH", "Chinese"
        ITALIAN = "IT", 'Italian'

    name = models.CharField(max_length=50)
    food_type = models.CharField(max_length=50, choices=FoodType.choices)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name}"


class OrderItems(models.Model):
    item_id = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=0)

    def __str__(self):
        return f"{self.item_id}"
    

class Order(models.Model):

    class StatusChoices(models.TextChoices):
        PENDING = "PD", "Pending"
        INPROGESS = "IP", "Inprogess"
        COMPLETED = "CP", "Completed" 

    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    items = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    order_status = models.CharField(max_length=10, choices=StatusChoices.choices, default=StatusChoices.PENDING)
    # customer = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __repr__(self):
        return f"Order('{self.order_id}', {self.customer.username})"
    



    



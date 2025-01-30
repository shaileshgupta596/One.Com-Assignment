from django.urls import path
from restaurent.views import order_view

app_name = "restaurent"

urlpatterns = [
    path('', order_view, name="order")
]

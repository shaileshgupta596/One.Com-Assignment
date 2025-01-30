from django.shortcuts import render, HttpResponse

from restaurent.models import Order, FoodItem
from restaurent.forms import OrderModelForm

# Create your views here.

def order_view(request, *args, **kwargs):
    msg = ""
    items = FoodItem.objects.all()
    if request.method == "POST":
        form = OrderModelForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            form.save()
            msg = "Order Created Successfully"
    form = OrderModelForm()
    return render(request, "restaurent/orders.html", context={'items': items, 'form': form, 'msg':msg})

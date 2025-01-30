from django import forms
from restaurent.models import Order, OrderItems
from django.core.exceptions import ValidationError
from django.forms.models import inlineformset_factory


class OrderModelForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['items', 'quantity']


    def is_valid(self):
        quantity = self.data.get('quantity')
        if int(quantity) <= 0:
            raise ValidationError("Quantity Cannot be Negative.")
        return super().is_valid()
    

class OrderItemModelForm(forms.ModelForm):
    class Meta:
        model = OrderItems
        fields = '__all__'


# ItemCollectionForm = inlineformset_factory(Order, OrderItems, form=OrderItemModelForm, extra=1, can_delete=True)
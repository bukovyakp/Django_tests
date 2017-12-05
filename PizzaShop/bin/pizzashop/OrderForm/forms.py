#coding:utf-8

from django.forms import ModelForm
from models import PizzaOrder


class PizzaOrderForm(ModelForm):
    class Meta:
        model = PizzaOrder
        fields = ['order_user_phone', 'order_user_address', 'order_pizza_appearance',
                  'order_pizza_quantity']


#coding:utf-8

from django import forms
from models import PizzaOrder


TITLE_CHOICES = (
    ('', ''),
    ('Паперони', 'Паперони'),
    ('С сыром и ногтями', 'С сыром и ногтями'),
    ('С чипсами', 'С чипсами'),
)


class PizzaOrderForm(forms.ModelForm):
    """
    def __init__(self, *args, **kwargs):
        super(PizzaOrderForm, self).__init__(*args, **kwargs)
        self.fields['order_user_phone'].label = "Телефон"
        self.fields['order_user_address'].label = "Адресс"
        self.fields['order_pizza_appearance'].label = "Тип пицци"
        self.fields['order_pizza_quantity'].label = "Количество"
    """
    order_user_phone = forms.CharField(label='Телефон', max_length=20)
    order_user_address = forms.CharField(label='Адрес доставки', max_length=100)
    order_pizza_appearance = forms.CharField(label='Вид пицци',
                                             widget=forms.Select(choices=TITLE_CHOICES),
                                             max_length=100)
    order_pizza_quantity = forms.IntegerField(label='Количество' )

    class Meta:
        model = PizzaOrder
        fields = ['order_user_phone', 'order_user_address', 'order_pizza_appearance',
                  'order_pizza_quantity']

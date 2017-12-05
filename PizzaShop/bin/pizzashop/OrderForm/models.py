# coding:utf-8

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PizzaOrder(models.Model):
    """
    Таблиця, котра вміщує у собі базові дані форми замовлення піцци
    """
    class Meta():
        db_table = "pizza_order"

    order_user_phone = models.IntegerField()                # телефон замовника
    order_user_address = models.TextField(max_length=200)   # адреса доставки
    order_pizza_appearance = models.TextField()             # вид піци
    order_pizza_quantity = models.IntegerField(default=1)   # кількість
    order_date = models.DateTimeField()                     # дата та час замовлення
    order_state = models.IntegerField(default=0)            # статус заказу (0-сформовано, 1-доставлено)
    order_number = models.IntegerField()                    # номер заказу
    order_user = models.ForeignKey(User)

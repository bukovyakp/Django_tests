from django.contrib import admin
from OrderForm.models import PizzaOrder

# Register your models here.
class ArticleInline(admin.StackedInline):
    model = PizzaOrder
    extra = 2


class ArticleAdmin(admin.ModelAdmin):
    fields = ['order_user_phone', 'order_user_address', 'order_pizza_appearance',
              'order_pizza_quantity', 'order_date', 'order_state', 'order_number']
    # inlines = [ArticleInline]
    list_filter = ['order_date']

admin.site.register(PizzaOrder, ArticleAdmin)

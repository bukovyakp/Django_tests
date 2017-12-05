#coding:utf-8

import datetime
from django.shortcuts import render_to_response, redirect     # Рендер у відповідь відразу
from django.core.context_processors import csrf
from django.contrib import auth
from django.db.models import Max
from django.http.response import HttpResponse

import json
from django.core.serializers.json import DjangoJSONEncoder

from models import PizzaOrder
from forms import PizzaOrderForm

# Create your views here.
def orders(request):
    order_form = PizzaOrderForm(request.POST)
    args = {}
    args.update(csrf(request))
    args['form'] = order_form
    args['username'] = auth.get_user(request).username
    args['user_id'] = auth.get_user(request).id
    return render_to_response('orderform.html', args)


def orders_2(request, user_id):
    order_form = PizzaOrderForm(request.POST)
    args = {}
    args.update(csrf(request))
    args['form'] = order_form
    args['username'] = auth.get_user(request).username
    args['user_id'] = auth.get_user(request).id
    args['all_orders'] = PizzaOrder.objects.filter(order_user_id=user_id)
    return render_to_response('orderform.html', args)


def maxordernumber():
    max_num = PizzaOrder.objects.aggregate(Max('order_number'))
    max_num = max_num['order_number__max']
    max_num += 1
    return max_num


def makeorder(request, user_id):
    """
    функція реалізує вставлення запиту у базу даних
    :param request:
    :param user_id:

    """
    default_order_state = 0
    order_form = PizzaOrderForm(request.POST)
    if request.POST:
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.order_user_id = user_id
            order.order_state = default_order_state
            order.order_number = maxordernumber()
            order.order_date = datetime.datetime.now()
            order_form.save()
            # return redirect('/')
            return redirect('/orders/%s/' % user_id)
    args = {}
    args.update(csrf(request))
    args['form'] = order_form
    args['username'] = auth.get_user(request).username
    args['user_id'] = auth.get_user(request).id
    return render_to_response('makeorder.html', args)

"""
def ajax_test(request):
    results = {'success': False}
    if True:
        results = {'success': True, 'param1': 'Fuck', 'param2': 'YOU!!!'}
    return HttpResponse(json.dumps(results), content_type='application/json')
"""

# -*- coding: utf-8 -*-
import sys
import datetime
from django.shortcuts import render_to_response, redirect     # Рендер у відповідь відразу
from django.core.context_processors import csrf
from django.contrib import auth
from django.db.models import Max
from django.http.response import HttpResponse

import json
# from django.core.serializers.json import DjangoJSONEncoder

from models import PizzaOrder
from .forms import PizzaOrderForm

reload(sys)
sys.setdefaultencoding('utf8')                                 # Устанавливаем стандартную внешнюю кодировку = utf8

# Create your views here.
def orders(request):
    order_form = PizzaOrderForm(request.POST)
    args = {}
    args.update(csrf(request))
    args['form'] = order_form
    args['username'] = auth.get_user(request).username
    args['user_id'] = auth.get_user(request).id
    return render_to_response('AJAXorderform.html', args)


def orders_2(request, user_id):
    order_form = PizzaOrderForm(request.POST)
    args = {}
    args.update(csrf(request))
    args['form'] = order_form
    args['username'] = auth.get_user(request).username
    args['user_id'] = auth.get_user(request).id
    args['all_orders'] = PizzaOrder.objects.filter(order_user_id=user_id)
    return render_to_response('AJAXorderform.html', args)


def maxordernumber():
    """
    Функция генерирует номер заказа для вставки в БД
    :return: максимальный номер существующего в БД заказа + 1
    """
    max_num = PizzaOrder.objects.aggregate(Max('order_number'))
    max_num = max_num['order_number__max']
    max_num += 1
    return max_num


def makeorder(request, user_id):
    """
    Функция вставки данных по заказу в БД
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


def ajax_test(request):
    """
    Тестовая функция, возвращает пару полей с текстом
    и пару полей из данными из сесии
    :param request:
    :return:
    """
    user_name = request.session['username']
    user_id = request.session['user_id']
    if True:
        results = {'success': True, 'param1': 'Fuck', 'param2': 'YOU!!', 'param3': user_name, 'param4': user_id}
        return HttpResponse(json.dumps(results), content_type='application/json')
    else:
        return HttpResponse('You have a problem')


def get_all_orders(request):
    """
    Функция ответа на AJAX запрос (Мои Заказы), которая выбирает все активные заказы
    пользователя по статусу order_state = 0 конвертирует даные в utf-8 кодировку
    и возвращает готовый шаблон страници в строку.
    Данные пользователя user_id берем из сесии которая создается при успешной
    валидации пользователя во время входа на сайт.
    :param request:
    :return: шаблон HTML страници
    """
    res = []
    user_id = request.session['user_id']
    all_orders = PizzaOrder.objects.filter(order_user_id=user_id,
                                           order_state=0).values('order_number',
                                                                 'order_user_phone',
                                                                 'order_user_address',
                                                                 'order_pizza_appearance',
                                                                 'order_pizza_quantity',
                                                                 'order_state')

    # формируем сам шаблон отверта и конвертируем его в текстовую строку
    res.append('Актуальные заказы <p><--------------------------------------><br/>')
    for x in all_orders:
        for key, val in x.iteritems():
            if key == 'order_number':
                res.append('<b>' + key + '</b>: '
                           + '<font color="red">'                                       # номер заказа другим цветом
                           + str(val) + '</font>')
            else:
                res.append('<b>' + key + '</b>: ' + str(val))
                res.append('<br/>')
        res.append('<br/><--------------------------------------><br/><br/>')
    res.append('</p>')

    # res = ' '.join(res).encode('utf-8').strip()
    results = {'all_orders': str(' '.join(res).encode('utf-8').strip())}
    return HttpResponse(json.dumps(results), content_type='application/json')

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PizzaOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_user_phone', models.IntegerField()),
                ('order_user_address', models.TextField(max_length=200)),
                ('order_pizza_appearance', models.TextField()),
                ('order_pizza_quantity', models.IntegerField(default=1)),
                ('order_date', models.DateTimeField()),
                ('order_state', models.IntegerField(default=0)),
                ('order_number', models.IntegerField()),
                ('order_user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'pizza_order',
            },
            bases=(models.Model,),
        ),
    ]

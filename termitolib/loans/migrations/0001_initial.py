# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 13:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import loans.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0003_auto_20170725_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_date', models.DateTimeField(auto_now_add=True)),
                ('return_date', models.DateTimeField(default=loans.models.get_deadline)),
                ('active', models.BooleanField(default=True)),
                ('by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book')),
                ('to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['loan_date', 'return_date'],
            },
        ),
    ]

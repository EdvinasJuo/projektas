# Generated by Django 4.2.7 on 2023-12-13 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0015_customer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
    ]

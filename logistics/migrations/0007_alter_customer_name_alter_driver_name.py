# Generated by Django 4.2.7 on 2023-12-04 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0006_alter_customer_options_alter_customer_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(help_text='Įveskite užsakovo vardą ir pavardę', max_length=80, verbose_name='Vardas Pavarde'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='name',
            field=models.CharField(help_text='Įveskite vairuotojo vardą ir pavardę', max_length=80, verbose_name='Vardas Pavarde'),
        ),
    ]

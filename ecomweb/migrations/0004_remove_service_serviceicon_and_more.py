# Generated by Django 4.0.4 on 2022-05-26 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomweb', '0003_remove_order_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='serviceicon',
        ),
        migrations.RemoveField(
            model_name='service',
            name='serviceparagraph',
        ),
    ]

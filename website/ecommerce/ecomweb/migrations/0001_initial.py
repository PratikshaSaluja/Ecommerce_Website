# Generated by Django 4.0.4 on 2022-05-20 10:36

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='contacts',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=100)),
                ('subject', models.TextField()),
                ('msg', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='detail',
            fields=[
                ('pdetailid', models.AutoField(primary_key=True, serialize=False)),
                ('pimage', models.ImageField(upload_to='pics')),
                ('pcategory', models.CharField(max_length=100)),
                ('pclient', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('purl', models.CharField(max_length=100)),
                ('pheading', models.CharField(max_length=100)),
                ('pdescription', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceicon', models.CharField(max_length=50)),
                ('serviceheading', models.CharField(max_length=50)),
                ('serviceparagraph', models.TextField()),
                ('serviceimage', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('desc', models.TextField()),
                ('image', models.ImageField(upload_to='pics')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomweb.category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('address', models.CharField(blank=True, default='', max_length=50)),
                ('phone', models.CharField(blank=True, default='', max_length=50)),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('status', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomweb.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 2.0.2 on 2020-08-12 04:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_product_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='author',
        ),
        migrations.AlterField(
            model_name='product',
            name='hunter',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

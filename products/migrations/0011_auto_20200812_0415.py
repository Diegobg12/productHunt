# Generated by Django 2.0.2 on 2020-08-12 04:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20200812_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='hunter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

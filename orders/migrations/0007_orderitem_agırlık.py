# Generated by Django 2.0 on 2019-07-14 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20190714_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='agırlık',
            field=models.PositiveIntegerField(default=0, verbose_name='Ağırlık'),
        ),
    ]

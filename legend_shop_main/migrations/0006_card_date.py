# Generated by Django 4.0.2 on 2022-03-25 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legend_shop_main', '0005_alter_card_options_alter_healthy_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='Время'),
        ),
    ]

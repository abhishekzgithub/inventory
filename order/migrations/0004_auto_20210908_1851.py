# Generated by Django 3.2 on 2021-09-08 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20210908_1840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='order',
            name='updated',
        ),
    ]
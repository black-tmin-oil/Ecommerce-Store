# Generated by Django 2.2.12 on 2021-01-20 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20210107_2248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='digital',
        ),
    ]

# Generated by Django 2.2.5 on 2021-10-26 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer_manage', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id']},
        ),
    ]

# Generated by Django 3.2.16 on 2022-12-14 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_custumer_active'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Custumer',
            new_name='Customer',
        ),
        migrations.RenameField(
            model_name='document',
            old_name='custumer',
            new_name='customer',
        ),
    ]

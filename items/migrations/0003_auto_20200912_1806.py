# Generated by Django 3.1 on 2020-09-12 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20200912_1734'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='username',
            new_name='user_id',
        ),
    ]

# Generated by Django 3.1 on 2020-09-12 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_auto_20200912_1806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='item_id',
        ),
        migrations.AddField(
            model_name='item',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]

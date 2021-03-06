# Generated by Django 3.1 on 2020-09-12 12:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('buy_date', models.DateField()),
                ('expiry_date', models.DateField()),
                ('bill_url', models.URLField(blank=True)),
                ('company', models.CharField(max_length=100)),
                ('contact1', models.CharField(max_length=10)),
                ('contact2', models.CharField(blank=True, max_length=10)),
                ('shop', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 3.2.16 on 2022-11-21 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=14)),
                ('color', models.CharField(max_length=12)),
                ('img', models.CharField(max_length=255)),
            ],
        ),
    ]
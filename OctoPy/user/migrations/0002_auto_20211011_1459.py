# Generated by Django 3.1.8 on 2021-10-11 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

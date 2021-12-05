# Generated by Django 3.1.7 on 2021-12-03 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_accepted', models.DateField(auto_now=True)),
                ('child_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin_user', to='user.child')),
            ],
            options={
                'db_table': 'Administrator',
            },
        ),
    ]

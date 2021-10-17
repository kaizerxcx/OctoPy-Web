# Generated by Django 3.1.8 on 2021-10-17 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('feedback', models.CharField(max_length=1000)),
                ('date', models.DateField(auto_now=True)),
                ('isRead', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Feedback',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=6)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('date_registered', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'User',
            },
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='user.user')),
                ('child_id', models.AutoField(primary_key=True, serialize=False)),
                ('isAtLevel1', models.BooleanField(default=True)),
                ('isAtLevel2', models.BooleanField(default=False)),
                ('isAtLevel3', models.BooleanField(default=False)),
                ('isAtLevel4', models.BooleanField(default=False)),
                ('isAtLevel5', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Child',
            },
            bases=('user.user',),
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('request_id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(default='Pending', max_length=100)),
                ('date', models.DateField(auto_now=True)),
                ('content', models.CharField(max_length=100)),
                ('isRead', models.BooleanField(default=False)),
                ('child_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_request', to='user.child')),
            ],
            options={
                'db_table': 'Request',
            },
        ),
        migrations.CreateModel(
            name='Points',
            fields=[
                ('point_id', models.AutoField(primary_key=True, serialize=False)),
                ('dateAcquired', models.DateField(auto_now=True)),
                ('crazeOnPhonicPoints', models.IntegerField(default=0)),
                ('wordKitPoints', models.IntegerField(default=0)),
                ('alphaHopperPoints', models.IntegerField(default=0)),
                ('mazeCrazePoints', models.IntegerField(default=0)),
                ('readingSpreePoints', models.IntegerField(default=0)),
                ('child_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_points', to='user.child')),
            ],
            options={
                'db_table': 'Points',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('notification_id', models.AutoField(primary_key=True, serialize=False)),
                ('receiver', models.CharField(max_length=500)),
                ('content', models.CharField(max_length=500)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('isRead', models.BooleanField(default=False)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_sender', to='user.child')),
            ],
            options={
                'db_table': 'Notification',
            },
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('login_id', models.AutoField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('lastLogin', models.CharField(max_length=10)),
                ('child_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_login', to='user.child')),
            ],
            options={
                'db_table': 'Login',
            },
        ),
    ]

# Generated by Django 3.2.9 on 2021-11-04 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userId', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('parkingId', models.AutoField(primary_key=True, serialize=False)),
                ('slot', models.IntegerField(max_length=50)),
                ('lot', models.CharField(max_length=50)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ParkResApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('messageId', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.CharField(max_length=50)),
                ('parkingId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ParkResApp.parking')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ParkResApp.user')),
            ],
        ),
    ]

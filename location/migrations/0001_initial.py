# Generated by Django 3.2.18 on 2023-03-12 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('city', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['city'],
            },
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('number', models.IntegerField()),
                ('capacity', models.IntegerField(default=2)),
            ],
            options={
                'ordering': ['number'],
            },
        ),
    ]

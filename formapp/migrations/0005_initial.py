# Generated by Django 4.0.1 on 2022-01-25 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('formapp', '0004_delete_form'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('mobile', models.BigIntegerField()),
                ('address', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=40)),
            ],
        ),
    ]

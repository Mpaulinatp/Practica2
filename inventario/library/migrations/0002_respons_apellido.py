# Generated by Django 4.2.7 on 2023-11-28 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='respons',
            name='apellido',
            field=models.TextField(default='', max_length=80),
        ),
    ]

# Generated by Django 4.0.1 on 2022-01-29 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myquizapi', '0008_usersignup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='question',
            field=models.CharField(max_length=100),
        ),
    ]

# Generated by Django 2.0 on 2018-10-21 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_auto_20181021_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='text',
            field=models.CharField(max_length=200),
        ),
    ]

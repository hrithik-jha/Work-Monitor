# Generated by Django 2.0 on 2018-10-21 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_auto_20181021_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='text',
            field=models.CharField(default='', max_length=200),
        ),
    ]
# Generated by Django 3.2.7 on 2021-11-29 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='time_modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]

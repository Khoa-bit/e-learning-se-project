# Generated by Django 3.2.7 on 2021-11-28 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0009_announcement_time_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
# Generated by Django 3.2.7 on 2021-11-23 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0008_alter_classcontent_attached_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classcontent',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]

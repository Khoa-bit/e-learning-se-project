# Generated by Django 3.2.7 on 2021-12-02 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Classwork', '0004_alter_studenttest_is_overdue'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='test_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
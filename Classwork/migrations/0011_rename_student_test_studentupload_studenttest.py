# Generated by Django 3.2.7 on 2021-12-02 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Classwork', '0010_alter_studentupload_student_test'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentupload',
            old_name='student_test',
            new_name='studenttest',
        ),
    ]

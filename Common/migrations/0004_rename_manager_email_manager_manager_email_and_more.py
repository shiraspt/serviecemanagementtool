# Generated by Django 4.1.7 on 2023-03-23 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Common', '0003_alter_manager_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manager',
            old_name='Manager_email',
            new_name='manager_email',
        ),
        migrations.RenameField(
            model_name='manager',
            old_name='Manager_name',
            new_name='manager_name',
        ),
        migrations.RenameField(
            model_name='manager',
            old_name='Manager_password',
            new_name='manager_password',
        ),
        migrations.RenameField(
            model_name='manager',
            old_name='Manager_phone',
            new_name='manager_phone',
        ),
    ]

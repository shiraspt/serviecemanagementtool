# Generated by Django 4.1.7 on 2023-03-30 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0006_technician_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technician',
            name='location',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Manager.location'),
        ),
    ]
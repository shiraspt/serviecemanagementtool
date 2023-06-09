# Generated by Django 4.1.7 on 2023-03-27 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Manager', '0005_product_models'),
        ('Cce', '0004_alter_complaint_purchase_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work_report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_name', models.CharField(max_length=50)),
                ('description', models.CharField(default='', max_length=1000)),
                ('work_date', models.DateField(default='')),
                ('work_time', models.TimeField(default='')),
                ('serial_number', models.CharField(default='', max_length=50)),
                ('warrenty', models.CharField(max_length=50)),
                ('work_status', models.CharField(max_length=50)),
                ('serviece_charge', models.FloatField(default='')),
                ('travel_distance', models.FloatField(default='', max_length=50)),
                ('complaint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cce.complaint')),
                ('technician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manager.technician')),
            ],
            options={
                'db_table': 'workreport_tb',
            },
        ),
    ]

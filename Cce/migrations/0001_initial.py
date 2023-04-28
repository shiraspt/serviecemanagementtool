# Generated by Django 4.1.7 on 2023-03-26 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Manager', '0005_product_models'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=50)),
                ('customer_phone1', models.CharField(max_length=50)),
                ('customer_phone2', models.CharField(max_length=50)),
                ('customer_email', models.CharField(max_length=50)),
                ('customer_address', models.CharField(max_length=500)),
                ('customer_location', models.CharField(max_length=50)),
                ('category_name', models.CharField(max_length=50)),
                ('model_name', models.CharField(max_length=50)),
                ('complaint_des', models.CharField(max_length=50)),
                ('purchase_date', models.DateField()),
                ('complaint_date', models.DateTimeField(auto_now_add=True)),
                ('warrenty', models.CharField(max_length=50)),
                ('physical_damage', models.CharField(max_length=50)),
                ('technician_name', models.CharField(max_length=50)),
                ('work_status', models.CharField(default='new', max_length=50)),
                ('complaint_name', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manager.product_category')),
                ('cce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manager.cce')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manager.location')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manager.product_models')),
                ('technician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manager.technician')),
            ],
            options={
                'db_table': 'complaint_tb',
            },
        ),
    ]

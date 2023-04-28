# Generated by Django 4.1.7 on 2023-03-26 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0004_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_models',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=50)),
                ('warrenty', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manager.product_category')),
            ],
            options={
                'db_table': 'productmodels_tb',
            },
        ),
    ]

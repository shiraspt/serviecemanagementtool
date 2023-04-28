# Generated by Django 4.1.7 on 2023-03-25 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cce_name', models.CharField(max_length=50)),
                ('cce_phone', models.CharField(max_length=50)),
                ('cce_email', models.CharField(max_length=50)),
                ('cce_age', models.IntegerField()),
                ('cce_gender', models.CharField(max_length=50)),
                ('cce_Address', models.CharField(max_length=500)),
                ('cce_photo', models.ImageField(upload_to='cce/')),
                ('cce_jdate', models.DateField()),
                ('cce_password', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'cce_tb',
            },
        ),
    ]

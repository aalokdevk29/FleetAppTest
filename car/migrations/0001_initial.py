# Generated by Django 3.2.1 on 2021-05-04 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Date created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last updated')),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Date created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last updated')),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Manufacturer',
                'verbose_name_plural': 'Manufacturers',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Date created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last updated')),
                ('model', models.CharField(max_length=256, verbose_name='Model of the car')),
                ('powertrain', models.CharField(choices=[('Internal Combustion', 'Internal Combustion'), ('Hybrid', 'Hybrid'), ('Electric', 'Electric')], default='Internal Combustion', max_length=256, verbose_name='Type')),
                ('max_passenger', models.PositiveIntegerField(verbose_name='Maximum number of passengers')),
                ('manufacturing_year', models.CharField(max_length=256, verbose_name='Year of manufacture')),
                ('registration', models.CharField(max_length=256, verbose_name='Registration number')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cars', to='car.category')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='car.manufacturer', verbose_name='Manufacturer')),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
            },
        ),
    ]

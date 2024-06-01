# Generated by Django 5.0.6 on 2024-06-01 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_product_description_alter_product_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='age',
            field=models.IntegerField(default=None, verbose_name='Edad'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(default=None, max_length=254, verbose_name='Correo'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.IntegerField(default=None, verbose_name='Telefono'),
        ),
    ]

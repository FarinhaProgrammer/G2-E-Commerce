# Generated by Django 3.2.6 on 2021-09-17 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0002_auto_20210916_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
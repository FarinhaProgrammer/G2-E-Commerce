# Generated by Django 3.1.3 on 2021-10-14 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categoria',
            new_name='Categorias',
        ),
    ]

# Generated by Django 3.1.3 on 2021-09-21 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0004_auto_20210921_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='imagem',
            field=models.ImageField(default='Ecommerce\\media\\media\x08arbie2.jpg', upload_to='media/categorias/'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='imagem',
            field=models.ImageField(default='Ecommerce\\media\\media\x08arbie2.jpg', upload_to='media/tags/'),
        ),
    ]

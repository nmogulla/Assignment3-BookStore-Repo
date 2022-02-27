# Generated by Django 3.0.1 on 2022-02-26 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(default='images/default.png', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.FloatField(default=0.0),
        ),
    ]

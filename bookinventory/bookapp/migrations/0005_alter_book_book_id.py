# Generated by Django 4.0.6 on 2022-07-17 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0004_alter_store_store_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Book_id',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]

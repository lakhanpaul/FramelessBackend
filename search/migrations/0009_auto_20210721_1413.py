# Generated by Django 3.2.3 on 2021-07-21 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0008_auto_20210719_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='opportunitydescriptioncard',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='opportunitydescriptioncardfeature',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-27 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perevod_app', '0003_alter_translation_en_alter_translation_uk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translation',
            name='en',
            field=models.CharField(max_length=50, unique=True, verbose_name='Англійська'),
        ),
        migrations.AlterField(
            model_name='translation',
            name='uk',
            field=models.CharField(max_length=50, unique=True, verbose_name='Українська'),
        ),
    ]

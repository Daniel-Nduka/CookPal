# Generated by Django 2.1.5 on 2024-03-14 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20240313_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='Image',
            field=models.ImageField(blank=True, upload_to='recipe_images/'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='Image',
            field=models.ImageField(blank=True, upload_to='recipe_images/'),
        ),
    ]

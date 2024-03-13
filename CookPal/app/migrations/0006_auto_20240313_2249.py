# Generated by Django 2.1.5 on 2024-03-13 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20240313_0629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favourites',
            name='Recipes',
        ),
        migrations.RemoveField(
            model_name='favourites',
            name='User',
        ),
        migrations.AddField(
            model_name='useraccount',
            name='Favourites',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Recipe'),
        ),
        migrations.DeleteModel(
            name='Favourites',
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-20 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0002_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
# Generated by Django 4.2.2 on 2023-06-20 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('usertype', models.CharField(blank=True, max_length=250, null=True)),
                ('image', models.FileField(upload_to='')),
            ],
        ),
    ]
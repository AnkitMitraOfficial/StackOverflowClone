# Generated by Django 3.1 on 2020-10-24 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.TextField(max_length=500),
        ),
    ]

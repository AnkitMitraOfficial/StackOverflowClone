# Generated by Django 3.1 on 2020-10-24 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contact', '0007_auto_20201024_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.TextField(max_length=122),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=22),
        ),
    ]

# Generated by Django 3.2.23 on 2024-07-04 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20240703_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sleepmatsummary',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sleepmatsummary',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
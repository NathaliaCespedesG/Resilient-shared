# Generated by Django 5.0.4 on 2024-04-29 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='type',
            field=models.CharField(default='global', max_length=20),
        ),
    ]
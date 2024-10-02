# Generated by Django 5.0.4 on 2024-04-25 05:55

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('device_hash', models.CharField(max_length=100)),
                ('device_type', models.CharField(max_length=100)),
                ('mac_address', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('path', models.CharField(max_length=300)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=100)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('password_hash', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Scale',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('weight', models.FloatField()),
                ('muscle_mass', models.FloatField()),
                ('bone_mass', models.FloatField()),
                ('fat_mass', models.FloatField()),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scales', to='api.device')),
            ],
        ),
        migrations.CreateModel(
            name='ScanWatchIntraActivity',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('heart_rate', models.FloatField()),
                ('date_heart_rate', models.FloatField()),
                ('steps', models.FloatField()),
                ('date_steps', models.FloatField()),
                ('calories', models.FloatField()),
                ('date_calories', models.FloatField()),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scanwatch_intraactivity', to='api.device')),
            ],
        ),
        migrations.CreateModel(
            name='ScanWatchSummary',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('average_heart_rate', models.FloatField()),
                ('calories', models.FloatField()),
                ('steps', models.FloatField()),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scanwatch_summary', to='api.device')),
            ],
        ),
        migrations.CreateModel(
            name='SleepmatIntraActivity',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('start_date', models.FloatField()),
                ('end_date', models.FloatField()),
                ('sleep_state', models.IntegerField()),
                ('date_heart_rate', models.FloatField()),
                ('heart_rate', models.FloatField()),
                ('date_respiration_rate', models.FloatField()),
                ('respiration_rate', models.FloatField()),
                ('date_snoring', models.FloatField()),
                ('snoring', models.FloatField()),
                ('date_sdnn_1', models.FloatField()),
                ('sdnn_1', models.FloatField()),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sleepmat_intraactivity', to='api.device')),
            ],
        ),
        migrations.CreateModel(
            name='SleepmatSummary',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('breathing_disturbances', models.IntegerField()),
                ('deep_sleep_duration', models.FloatField()),
                ('duration_to_sleep', models.FloatField()),
                ('duration_to_wakeup', models.FloatField()),
                ('average_heart_rate', models.FloatField()),
                ('light_sleep_duration', models.FloatField()),
                ('rem_sleep_duration', models.FloatField()),
                ('average_rr', models.IntegerField()),
                ('sleep_score', models.FloatField()),
                ('wakeup_count', models.FloatField()),
                ('wakeup_duration', models.FloatField()),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sleepmat_summary', to='api.device')),
            ],
        ),
        migrations.CreateModel(
            name='Usage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('scanwatch_usage_level', models.CharField(max_length=10)),
                ('scanwatch_battery', models.FloatField()),
                ('scanwatch_last_date', models.DateField()),
                ('sleepmat_usage_level', models.CharField(max_length=10)),
                ('sleepmat_battery', models.FloatField()),
                ('sleepmat_last_date', models.DateField()),
                ('scale_usage_level', models.CharField(max_length=10)),
                ('scale_battery', models.FloatField()),
                ('scale_last_date', models.DateField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report_usages', to='api.report')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usages', to='api.user')),
            ],
        ),
        migrations.AddField(
            model_name='report',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='api.user'),
        ),
        migrations.AddField(
            model_name='device',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='api.user'),
        ),
    ]
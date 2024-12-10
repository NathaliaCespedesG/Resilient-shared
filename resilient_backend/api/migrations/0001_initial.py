# Generated by Django 3.2.23 on 2024-12-10 05:54

from django.db import migrations, models
import django.db.models.deletion
import uuid


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
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=100)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('password_hash', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=True)),
                ('withings_connected', models.BooleanField(default=False)),
                ('withings_credentials_path', models.CharField(blank=True, max_length=300, null=True)),
                ('scale_device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scale_device_id', to='api.device')),
                ('scanwatch_device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scanwatch_device_id', to='api.device')),
                ('sleepmat_device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sleepmat_device_id', to='api.device')),
            ],
        ),
        migrations.CreateModel(
            name='Usage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('scanwatch_usage_level', models.CharField(blank=True, max_length=10, null=True)),
                ('scanwatch_battery', models.CharField(blank=True, max_length=10, null=True)),
                ('scanwatch_last_date', models.DateField(blank=True, null=True)),
                ('sleepmat_usage_level', models.CharField(blank=True, max_length=10, null=True)),
                ('sleepmat_battery', models.CharField(blank=True, max_length=10, null=True)),
                ('sleepmat_last_date', models.DateField(blank=True, null=True)),
                ('scale_usage_level', models.CharField(blank=True, max_length=10, null=True)),
                ('scale_battery', models.CharField(blank=True, max_length=10, null=True)),
                ('scale_last_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usages', to='api.user')),
            ],
        ),
        migrations.CreateModel(
            name='SleepmatSummary',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('breathing_disturbances', models.IntegerField(blank=True, null=True)),
                ('deep_sleep_duration', models.FloatField(blank=True, null=True)),
                ('duration_to_sleep', models.FloatField(blank=True, null=True)),
                ('duration_to_wakeup', models.FloatField(blank=True, null=True)),
                ('average_heart_rate', models.FloatField(blank=True, null=True)),
                ('hr_max', models.FloatField(blank=True, null=True)),
                ('hr_min', models.FloatField(blank=True, null=True)),
                ('light_sleep_duration', models.FloatField(blank=True, null=True)),
                ('rem_sleep_duration', models.FloatField(blank=True, null=True)),
                ('average_rr', models.IntegerField(blank=True, null=True)),
                ('rr_max', models.FloatField(blank=True, null=True)),
                ('rr_min', models.FloatField(blank=True, null=True)),
                ('sleep_score', models.FloatField(blank=True, null=True)),
                ('wakeup_count', models.FloatField(blank=True, null=True)),
                ('wakeup_duration', models.FloatField(blank=True, null=True)),
                ('total_sleep_time', models.FloatField(blank=True, null=True)),
                ('total_time_in_bed', models.FloatField(blank=True, null=True)),
                ('awake_in_bed', models.FloatField(blank=True, null=True)),
                ('apnea', models.FloatField(blank=True, null=True)),
                ('out_of_bed_count', models.FloatField(blank=True, null=True)),
                ('hr_date_af', models.DateField(blank=True, null=True)),
                ('hr_af', models.FloatField(blank=True, null=True)),
                ('hr_date_rr', models.DateField(blank=True, null=True)),
                ('hr_rr', models.FloatField(blank=True, null=True)),
                ('snoring_episodes', models.FloatField(blank=True, null=True)),
                ('snoring_time', models.FloatField(blank=True, null=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sleepmat_summary', to='api.device')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sleepmat_summary_user', to='api.user')),
            ],
        ),
        migrations.CreateModel(
            name='SleepmatIntraActivity',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('start_date', models.FloatField(blank=True, null=True)),
                ('end_date', models.FloatField(blank=True, null=True)),
                ('sleep_state', models.IntegerField(blank=True, null=True)),
                ('date_heart_rate', models.FloatField(blank=True, null=True)),
                ('heart_rate', models.FloatField(blank=True, null=True)),
                ('date_respiration_rate', models.FloatField(blank=True, null=True)),
                ('respiration_rate', models.FloatField(blank=True, null=True)),
                ('date_snoring', models.FloatField(blank=True, null=True)),
                ('snoring', models.FloatField(blank=True, null=True)),
                ('date_sdnn_1', models.FloatField(blank=True, null=True)),
                ('sdnn_1', models.FloatField(blank=True, null=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sleepmat_intraactivity', to='api.device')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sleepmat_intraactivity_user', to='api.user')),
            ],
        ),
        migrations.CreateModel(
            name='ScanWatchSummary',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True, null=True)),
                ('average_heart_rate', models.FloatField(blank=True, null=True)),
                ('calories', models.FloatField(blank=True, null=True)),
                ('steps', models.FloatField(blank=True, null=True)),
                ('hr_max', models.FloatField(blank=True, null=True)),
                ('hr_min', models.FloatField(blank=True, null=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scanwatch_summary', to='api.device')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scanwatch_summary_user', to='api.user')),
            ],
        ),
        migrations.CreateModel(
            name='ScanWatchIntraActivity',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('heart_rate', models.FloatField(blank=True, null=True)),
                ('date_heart_rate', models.FloatField(blank=True, null=True)),
                ('steps', models.FloatField(blank=True, null=True)),
                ('date_steps', models.FloatField(blank=True, null=True)),
                ('calories', models.FloatField(blank=True, null=True)),
                ('date_calories', models.FloatField(blank=True, null=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scanwatch_intraactivity', to='api.device')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scanwatch_intraactivity_user', to='api.user')),
            ],
        ),
        migrations.CreateModel(
            name='Scale',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('weight', models.FloatField(blank=True, null=True)),
                ('muscle_mass', models.FloatField(blank=True, null=True)),
                ('bone_mass', models.FloatField(blank=True, null=True)),
                ('fat_mass', models.FloatField(blank=True, null=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scales', to='api.device')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scales_user', to='api.user')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('path', models.CharField(max_length=300)),
                ('type', models.CharField(default='aggegated', max_length=20)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='api.user')),
            ],
        ),
    ]

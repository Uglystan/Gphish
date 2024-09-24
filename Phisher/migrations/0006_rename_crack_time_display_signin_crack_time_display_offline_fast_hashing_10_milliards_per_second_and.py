# Generated by Django 4.2.15 on 2024-09-06 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Phisher', '0005_signin_crack_time_display_signin_guesses'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signin',
            old_name='crack_time_display',
            new_name='crack_time_display_offline_fast_hashing_10_milliards_per_second',
        ),
        migrations.AddField(
            model_name='signin',
            name='crack_time_display_offline_slow_hashing_10000_per_second',
            field=models.CharField(default='zer', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signin',
            name='crack_time_display_online_10_per_seconde',
            field=models.CharField(default='aze', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signin',
            name='crack_time_display_online_throttling_100_per_hour',
            field=models.CharField(default='aze', max_length=100),
            preserve_default=False,
        ),
    ]
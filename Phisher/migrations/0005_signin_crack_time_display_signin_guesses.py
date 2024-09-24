# Generated by Django 4.2.15 on 2024-09-06 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Phisher', '0004_remove_signin_password_signin_feedback_suggestions_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='signin',
            name='crack_time_display',
            field=models.CharField(default='azeae', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signin',
            name='guesses',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=10),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.2.4 on 2024-01-18 05:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('officeapp', '0016_checkinout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkinout',
            name='UserId',
        ),
        migrations.RemoveField(
            model_name='checkinout',
            name='UserName',
        ),
        migrations.AddField(
            model_name='checkinout',
            name='user_profile',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='checkins', to='officeapp.userprofile'),
            preserve_default=False,
        ),
    ]
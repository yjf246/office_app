# Generated by Django 4.2.4 on 2024-01-27 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('officeapp', '0036_alter_task_markasdone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chetbox',
            fields=[
                ('Chetid', models.AutoField(primary_key=True, serialize=False)),
                ('Message', models.CharField(max_length=1000)),
                ('Attachments', models.FileField(blank=True, null=True, upload_to='Attachments/')),
                ('Userprofile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='officeapp.userprofile')),
            ],
        ),
    ]

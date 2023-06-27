# Generated by Django 4.2 on 2023-06-13 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('ongoing', 'Ongoing'), ('complete', 'Complete')], default='pending', max_length=20),
        ),
    ]
# Generated by Django 5.1 on 2024-08-13 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0007_accounts_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accounts',
            name='users',
        ),
    ]

# Generated by Django 5.1 on 2024-08-13 17:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0006_alter_plantedtree_tree'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='users',
            field=models.ManyToManyField(related_name='accounts', to=settings.AUTH_USER_MODEL),
        ),
    ]

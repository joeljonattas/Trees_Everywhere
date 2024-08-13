# Generated by Django 5.1 on 2024-08-13 12:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0005_alter_plantedtree_account_alter_plantedtree_tree'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantedtree',
            name='tree',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planted_tree_tree', to='trees.tree'),
        ),
    ]

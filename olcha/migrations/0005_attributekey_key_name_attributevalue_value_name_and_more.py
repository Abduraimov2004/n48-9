# Generated by Django 5.1.1 on 2024-09-26 12:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olcha', '0004_alter_product_users_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='attributekey',
            name='key_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='attributevalue',
            name='value_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='productattribute',
            name='attr_key',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='olcha.attributekey'),
        ),
        migrations.AddField(
            model_name='productattribute',
            name='attr_value',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='olcha.attributevalue'),
        ),
        migrations.AddField(
            model_name='productattribute',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='olcha.product'),
        ),
        migrations.AlterField(
            model_name='image',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='olcha.product'),
        ),
    ]
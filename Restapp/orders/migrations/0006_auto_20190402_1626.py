# Generated by Django 2.1.5 on 2019-04-02 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_product_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Product'),
        ),
    ]

# Generated by Django 4.2.5 on 2024-02-02 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Olsi_App', '0003_alter_product_db_prdt_benefits_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=5000)),
                ('answer', models.TextField(max_length=10000)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Olsi_App.product_db')),
            ],
        ),
    ]

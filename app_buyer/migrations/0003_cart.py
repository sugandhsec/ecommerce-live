# Generated by Django 4.1.7 on 2023-04-18 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_seller', '0002_product'),
        ('app_buyer', '0002_user_profilepic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_seller.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_buyer.user')),
            ],
        ),
    ]

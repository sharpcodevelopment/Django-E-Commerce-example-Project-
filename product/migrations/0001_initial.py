# Generated by Django 5.1.2 on 2024-11-22 22:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('keywords', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('images', models.ImageField(blank=True, upload_to='images/')),
                ('status', models.CharField(choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=20)),
                ('slug', models.SlugField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('upload_at', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='product.category')),
            ],
        ),
    ]

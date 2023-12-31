# Generated by Django 5.0 on 2023-12-28 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_alter_bookingmodel_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='photoesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'image',
                'verbose_name_plural': 'imaages',
            },
        ),
    ]

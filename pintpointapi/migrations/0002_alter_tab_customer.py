# Generated by Django 4.1.3 on 2022-12-08 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pintpointapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tab',
            name='customer',
            field=models.CharField(default='Eric', max_length=100),
            preserve_default=False,
        ),
    ]

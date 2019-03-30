# Generated by Django 2.1.7 on 2019-03-30 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20190330_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='vessel',
            name='fleet_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vessel',
            name='vessel_name',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='event',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
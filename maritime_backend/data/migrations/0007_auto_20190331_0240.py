# Generated by Django 2.1.7 on 2019-03-31 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_auto_20190330_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='vessel_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Vessel'),
        ),
    ]

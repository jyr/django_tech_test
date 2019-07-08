# Generated by Django 2.1.2 on 2019-07-05 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='id',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='id',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='stations', to='stations.Location'),
        ),
    ]

# Generated by Django 3.1.1 on 2020-09-15 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0011_auto_20200915_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='facebook',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='google',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='instagram',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='twitter',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
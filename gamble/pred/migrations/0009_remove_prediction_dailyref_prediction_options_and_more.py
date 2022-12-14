# Generated by Django 4.0.5 on 2022-07-08 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pred', '0008_alter_prediction_bundleref_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prediction',
            name='dailyRef',
        ),
        migrations.AddField(
            model_name='prediction',
            name='options',
            field=models.CharField(blank=True, choices=[('toptenRef', 'toptenRef'), ('bundleRef', 'bundleRef'), ('overOneRef', 'overOneRef'), ('tipsRef', 'tipsRef'), ('tennisRef', 'tennisRef'), ('dailyRef', 'dailyRef'), ('expertsRef', 'expertsRef')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='bundleRef',
            field=models.CharField(blank=True, choices=[('Bundle One', 'Bundle One'), ('Bundle Two', 'Bundle Two'), ('Bundle Four', 'Bundle Four'), ('Bundle Three', 'Bundle Three')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='expertsRef',
            field=models.CharField(blank=True, choices=[('Harrison', 'Harrison'), ('Jeje', 'Jeje'), ('Olaolu', 'Olaolu')], max_length=50, null=True),
        ),
    ]

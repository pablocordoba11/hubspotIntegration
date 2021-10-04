# Generated by Django 3.2 on 2021-10-03 21:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integration', '0003_rename_deals_deal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deal',
            old_name='name',
            new_name='dealname',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='colse_date',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='deal_type',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='id',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='stage',
        ),
        migrations.AddField(
            model_name='deal',
            name='closedate',
            field=models.DateField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AddField(
            model_name='deal',
            name='dealId',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='deal',
            name='dealstage',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='deal',
            name='dealtype',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.DeleteModel(
            name='DealType',
        ),
    ]

# Generated by Django 3.2 on 2021-10-03 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integration', '0004_auto_20211003_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='dealId',
            field=models.CharField(default=1, max_length=150, primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 5.1.3 on 2024-11-13 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miawaccounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
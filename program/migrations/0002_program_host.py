# Generated by Django 4.0.3 on 2022-08-06 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='host',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
# Generated by Django 3.1.3 on 2022-08-26 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circlelist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
    ]

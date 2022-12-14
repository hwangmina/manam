# Generated by Django 3.1.3 on 2022-08-06 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0002_auto_20220806_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cate_1', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('lat', models.CharField(max_length=50)),
                ('lng', models.CharField(max_length=50)),
                ('dong', models.CharField(max_length=50)),
                ('cate_2', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('url', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Facilities',
        ),
    ]

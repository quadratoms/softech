# Generated by Django 3.1.7 on 2021-04-09 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('combo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=22)),
                ('short', models.CharField(max_length=2)),
            ],
        ),
    ]
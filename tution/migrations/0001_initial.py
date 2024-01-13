# Generated by Django 5.0 on 2024-01-13 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TutionClassModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TutionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('weekly_day', models.IntegerField()),
                ('daily_time', models.IntegerField()),
                ('location', models.CharField(max_length=200)),
                ('fee', models.IntegerField()),
                ('tution_status', models.CharField(choices=[('Running', 'Running'), ('Completed', 'Completed')], default='Running', max_length=30)),
                ('tutionclass', models.ManyToManyField(to='tution.tutionclassmodel')),
            ],
        ),
    ]

# Generated by Django 2.2 on 2019-04-11 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateField(verbose_name='date created')),
                ('year', models.PositiveSmallIntegerField(choices=[(2016, '2016'), (2017, '2017'), (2018, '2018'), (2019, '2019'), (2020, '2020'), (2021, '2021')])),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Inputs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0)),
                ('consumption', models.FloatField(default=0)),
                ('month', models.PositiveSmallIntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')])),
                ('period', models.CharField(choices=[('Ponta', 'Ponta'), ('Cheia', 'Cheia'), ('Vazio', 'Vazio'), ('SuperVazio', 'SuperVazio')], max_length=20)),
                ('analysis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spark.Analysis')),
            ],
        ),
        migrations.AddField(
            model_name='analysis',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spark.Company'),
        ),
    ]

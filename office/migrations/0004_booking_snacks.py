# Generated by Django 2.2.2 on 2019-06-08 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0003_auto_20190608_2141'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('department', models.CharField(choices=[('tech', 'Tech'), ('mplab', 'Mplab'), ('acadmey', 'Acadmey')], default='DEFAULT VALUE', max_length=50)),
                ('mettingroom', models.CharField(choices=[('t0', 'T0'), ('a0', 'A1'), ('a1', 'A1')], default='DEFAULT VALUE', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='snacks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('department', models.CharField(choices=[('tech', 'Tech'), ('mplab', 'Mplab'), ('acadmey', 'Acadmey')], default='DEFAULT VALUE', max_length=50)),
                ('drinks', models.CharField(choices=[('tea', 'Tea'), ('coffee', 'Coffee')], default='DEFAULT VALUE', max_length=50)),
                ('sugar', models.CharField(choices=[('sugar', 'Sugar'), ('nosugar', 'Nosugar')], default='DEFAULT VALUE', max_length=50)),
            ],
        ),
    ]

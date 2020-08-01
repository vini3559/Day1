# Generated by Django 3.0.8 on 2020-07-21 16:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='installments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Installments', models.IntegerField()),
                ('Date', models.DateField(default=django.utils.timezone.now)),
                ('Registration_id_imo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='shg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Activity', models.CharField(max_length=20)),
                ('Amount', models.IntegerField()),
                ('Woman_beneficiaries', models.IntegerField()),
                ('Location', models.TextField()),
                ('TimePeriod', models.DecimalField(decimal_places=2, max_digits=4)),
                ('Rate', models.DecimalField(decimal_places=2, max_digits=4)),
                ('Registration_id_imo', models.CharField(max_length=10)),
            ],
        ),
    ]
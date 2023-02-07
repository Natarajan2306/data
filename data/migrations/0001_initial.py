# Generated by Django 3.2.16 on 2023-01-31 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companiesname', models.CharField(max_length=40)),
                ('count', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Financial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companiesname', models.CharField(max_length=40)),
                ('firstname', models.CharField(max_length=40)),
                ('lastname', models.CharField(max_length=40)),
                ('Title', models.CharField(max_length=40)),
                ('Email', models.CharField(max_length=40)),
                ('url', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Financial_Count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companiesname', models.CharField(max_length=40)),
                ('count', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Leadfedder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companiesname', models.CharField(max_length=40)),
                ('firstname', models.CharField(max_length=40)),
                ('lastname', models.CharField(max_length=40)),
                ('Title', models.CharField(max_length=40)),
                ('Email', models.CharField(max_length=40)),
                ('url', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Leadfedder_Count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companiesname', models.CharField(max_length=40)),
                ('count', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Mastersheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companiesname', models.CharField(max_length=40)),
                ('firstname', models.CharField(max_length=40)),
                ('lastname', models.CharField(max_length=40)),
                ('Title', models.CharField(max_length=40)),
                ('Email', models.CharField(max_length=40)),
                ('url', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Retail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companiesname', models.CharField(max_length=40)),
                ('firstname', models.CharField(max_length=40)),
                ('lastname', models.CharField(max_length=40)),
                ('Title', models.CharField(max_length=40)),
                ('Email', models.CharField(max_length=40)),
                ('url', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Retail_Count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companiesname', models.CharField(max_length=40)),
                ('count', models.CharField(max_length=40)),
            ],
        ),
    ]
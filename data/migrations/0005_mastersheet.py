# Generated by Django 3.2.16 on 2023-02-06 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_delete_mastersheet'),
    ]

    operations = [
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
    ]

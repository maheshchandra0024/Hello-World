# Generated by Django 2.1.5 on 2019-01-20 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bandi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Year', models.CharField(max_length=60)),
                ('Make', models.CharField(max_length=60)),
                ('Model', models.CharField(max_length=60)),
            ],
        ),
    ]

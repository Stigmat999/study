# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-23 08:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublishingHouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('year_of_foundation', models.IntegerField(null=True)),
                ('short_description', models.CharField(max_length=300, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='author',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='basic_genre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='hometown',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='year_of_birth',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='publishing_house',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.PublishingHouse'),
        ),
        migrations.AlterField(
            model_name='book',
            name='year_of_publication',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='number_of_books',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='popularity',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.DeleteModel(
            name='Publishing_house',
        ),
    ]

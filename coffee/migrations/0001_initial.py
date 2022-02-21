# Generated by Django 3.1.7 on 2022-02-21 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoffeeReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('number', models.CharField(blank=True, max_length=100, null=True)),
                ('message', models.TextField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
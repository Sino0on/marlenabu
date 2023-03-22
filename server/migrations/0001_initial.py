# Generated by Django 4.1.7 on 2023-03-22 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=123)),
                ('description', models.TextField()),
                ('author', models.CharField(max_length=123)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateTimeField()),
                ('likes', models.IntegerField(blank=True, default=0)),
            ],
        ),
    ]

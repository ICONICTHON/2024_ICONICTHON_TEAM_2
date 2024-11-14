# Generated by Django 4.2.16 on 2024-11-14 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=30)),
                ('starttime', models.DateField()),
                ('finishtime', models.DateField()),
                ('name', models.CharField(max_length=30)),
                ('body', models.CharField(max_length=500)),
            ],
        ),
    ]
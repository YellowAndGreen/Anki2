# Generated by Django 3.0.4 on 2022-02-28 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0012_auto_20220227_2009'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('headword', models.CharField(max_length=2000)),
                ('item', models.CharField(max_length=200000)),
            ],
        ),
    ]

# Generated by Django 3.0.4 on 2022-01-29 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0007_auto_20220129_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='cid',
            field=models.PositiveIntegerField(null=True, unique=True),
        ),
    ]

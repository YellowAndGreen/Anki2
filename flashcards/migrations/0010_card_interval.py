# Generated by Django 3.0.4 on 2022-02-27 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0009_auto_20220224_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='interval',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
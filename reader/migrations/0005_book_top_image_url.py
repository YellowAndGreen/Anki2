# Generated by Django 3.0.4 on 2022-03-07 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0004_auto_20220307_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='top_image_url',
            field=models.CharField(default='none', max_length=200),
        ),
    ]

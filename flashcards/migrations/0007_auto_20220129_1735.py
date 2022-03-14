# Generated by Django 3.0.4 on 2022-01-29 17:35

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
        ('flashcards', '0006_wordlist_len_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='card',
            name='cid',
            field=models.PositiveIntegerField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='wordlist',
            name='len_list',
            field=models.PositiveIntegerField(default=50),
        ),
    ]

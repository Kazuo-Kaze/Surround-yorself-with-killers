# Generated by Django 4.1.7 on 2023-02-19 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_mailmessage_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailmessage',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=255),
        ),
    ]

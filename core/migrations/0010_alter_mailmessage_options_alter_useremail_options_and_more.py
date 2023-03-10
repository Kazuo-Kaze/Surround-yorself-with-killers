# Generated by Django 4.1.7 on 2023-02-19 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_mailmessage_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailmessage',
            options={'ordering': ['-date'], 'verbose_name_plural': 'Message'},
        ),
        migrations.AlterModelOptions(
            name='useremail',
            options={'ordering': ['-date'], 'verbose_name_plural': 'Email'},
        ),
        migrations.AddField(
            model_name='mailmessage',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]

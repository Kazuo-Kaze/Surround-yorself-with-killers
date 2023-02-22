# Generated by Django 4.1.7 on 2023-02-15 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_useremail_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('first_para', models.TextField(null=True)),
                ('second_para', models.TextField(null=True)),
                ('third_para', models.TextField(null=True)),
                ('fourth_para', models.TextField(null=True)),
                ('fifth_para', models.TextField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Message',
            },
        ),
    ]
# Generated by Django 3.2 on 2021-04-24 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_delete_resetpassword'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_verified_at',
            field=models.DateTimeField(null=True, verbose_name='email_verified_at'),
        ),
    ]

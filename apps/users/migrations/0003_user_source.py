# Generated by Django 4.2.13 on 2024-07-11 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_user_create_time_user_update_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="source",
            field=models.CharField(default="LOCAL", max_length=10, verbose_name="来源"),
        ),
    ]

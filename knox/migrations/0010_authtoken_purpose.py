# Generated by Django 4.1.1 on 2023-06-20 22:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("knox", "0009_extend_authtoken_field"),
    ]

    operations = [
        migrations.AddField(
            model_name="authtoken",
            name="purpose",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

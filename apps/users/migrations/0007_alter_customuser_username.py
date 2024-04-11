# Generated by Django 4.2 on 2024-04-10 18:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0006_alter_customuser_phone_alter_customuser_role_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="username",
            field=models.CharField(
                blank=True, max_length=254, unique=True, verbose_name="Имя пользователя"
            ),
        ),
    ]

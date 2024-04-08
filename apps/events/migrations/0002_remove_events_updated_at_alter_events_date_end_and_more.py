# Generated by Django 4.2 on 2024-04-05 11:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="events",
            name="updated_at",
        ),
        migrations.AlterField(
            model_name="events",
            name="date_end",
            field=models.DateField(
                db_index=True, default=None, verbose_name="дата окончания мероприятия"
            ),
        ),
        migrations.AlterField(
            model_name="events",
            name="date_start",
            field=models.DateField(
                db_index=True, default=None, verbose_name="дата начала мероприятия"
            ),
        ),
        migrations.AlterField(
            model_name="events",
            name="registration_close",
            field=models.DateTimeField(
                db_index=True, default=None, verbose_name="дата закрытия регистрации"
            ),
        ),
        migrations.AlterField(
            model_name="events",
            name="registration_open",
            field=models.DateTimeField(
                db_index=True, default=None, verbose_name="дата открытия регистрации"
            ),
        ),
    ]

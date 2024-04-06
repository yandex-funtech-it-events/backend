# Generated by Django 4.2 on 2024-04-06 08:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_customuser_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(max_length=15, unique=True, verbose_name='Номер телефона пользователя'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('attendee', 'Участник'), ('organizer', 'Организатор'), ('moderator', 'Модератор')], default='attendee', max_length=150, verbose_name='Пользовательская роль'),
        ),
        migrations.AlterField(
            model_name='customuserfilter',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='filter', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='customuserinfo',
            name='experience',
            field=models.CharField(choices=[('0-1', '0-1 год'), ('1-3', '1-3 года'), ('3-5', '3-5 лет'), ('5-10', '5-10 лет'), ('10+', 'Больше 10 лет')], default='0-1', max_length=20, verbose_name='Опыт работы'),
        ),
    ]

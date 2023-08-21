# Generated by Django 4.2.4 on 2023-08-21 22:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AI_HealthTrainer', '0003_remove_workout_user_workout_goal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='goal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
# Generated by Django 3.0.5 on 2020-05-03 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0004_auto_20200503_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='entre',
            name='idea_title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_app.Idea'),
        ),
    ]

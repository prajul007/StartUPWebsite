# Generated by Django 3.0.4 on 2020-05-06 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0007_auto_20200503_2333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entre',
            name='idea_title',
        ),
        migrations.AlterField(
            model_name='entre',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entre_profile', to='user_app.Userp'),
        ),
    ]
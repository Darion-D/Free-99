# Generated by Django 4.1.2 on 2022-10-12 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'ordering': ['name']},
        ),
        migrations.RenameField(
            model_name='game',
            old_name='title',
            new_name='name',
        ),
    ]
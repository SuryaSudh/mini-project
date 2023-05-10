# Generated by Django 4.0.4 on 2023-05-10 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('macares', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='place',
            new_name='district',
        ),
        migrations.AddField(
            model_name='user',
            name='cmp',
            field=models.CharField(default=13, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='occupation',
            field=models.CharField(default=13, max_length=20),
            preserve_default=False,
        ),
    ]

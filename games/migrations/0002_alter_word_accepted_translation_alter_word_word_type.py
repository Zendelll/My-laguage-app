# Generated by Django 5.0.6 on 2024-05-30 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='accepted_translation',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='word',
            name='word_type',
            field=models.CharField(max_length=11),
        ),
    ]

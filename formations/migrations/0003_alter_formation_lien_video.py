# Generated by Django 5.1.3 on 2024-11-28 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formations', '0002_alter_formation_lien_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formation',
            name='lien_video',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

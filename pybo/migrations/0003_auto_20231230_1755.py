# Generated by Django 3.1.7 on 2023-12-30 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0002_auto_20231229_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

# Generated by Django 3.0.2 on 2020-01-27 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('occurrences', '0002_auto_20200127_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occurrencemodel',
            name='updated_date',
            field=models.DateTimeField(auto_created=True, blank=True, null=True),
        ),
    ]

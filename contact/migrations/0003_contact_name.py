# Generated by Django 3.1.5 on 2021-02-20 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20210220_0231'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
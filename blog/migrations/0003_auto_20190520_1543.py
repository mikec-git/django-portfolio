# Generated by Django 2.2.1 on 2019-05-20 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190518_1359'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='pubDate',
            new_name='pub_date',
        ),
    ]
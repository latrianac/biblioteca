# Generated by Django 2.1.1 on 2018-11-16 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0006_auto_20181116_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='link_imagen',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]

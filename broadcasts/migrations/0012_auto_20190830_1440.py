# Generated by Django 2.1.5 on 2019-08-30 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broadcasts', '0011_auto_20190830_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='broadcast',
            name='broadcast_type',
            field=models.CharField(choices=[('voice', 'Voice'), ('SMS', 'SMS'), ('Both', 'Both')], default='voice', max_length=30),
        ),
    ]

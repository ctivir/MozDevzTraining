# Generated by Django 3.2.6 on 2021-08-20 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mozdevzsite', '0004_auto_20210812_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='team',
            field=models.CharField(choices=[('Administrator', 'Admin'), ('Alumni', 'Alumni'), ('Embassador', 'Embassador')], default='Embassador', max_length=30),
        ),
    ]
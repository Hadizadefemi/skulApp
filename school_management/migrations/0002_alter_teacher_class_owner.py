# Generated by Django 4.2.4 on 2023-08-05 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='class_owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='school_management.class'),
        ),
    ]
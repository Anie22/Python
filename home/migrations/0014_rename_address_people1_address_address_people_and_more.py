# Generated by Django 4.0.4 on 2022-06-05 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_address_address_people1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='address_people1',
            new_name='address_people',
        ),
        migrations.RenameField(
            model_name='bio',
            old_name='bio_people3',
            new_name='bio_people',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='doctor_people2',
            new_name='doctor_people',
        ),
    ]
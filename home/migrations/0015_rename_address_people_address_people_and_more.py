# Generated by Django 4.0.4 on 2022-06-05 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_rename_address_people1_address_address_people_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='address_people',
            new_name='people',
        ),
        migrations.RenameField(
            model_name='bio',
            old_name='bio_people',
            new_name='people',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='doctor_people',
            new_name='people',
        ),
    ]

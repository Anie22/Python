# Generated by Django 4.0.4 on 2022-06-05 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_bio_bio_people_alter_doctor_doctor_people'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='address_people',
            new_name='address_people1',
        ),
        migrations.RenameField(
            model_name='bio',
            old_name='bio_people',
            new_name='bio_people3',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='doctor_people',
            new_name='doctor_people2',
        ),
    ]

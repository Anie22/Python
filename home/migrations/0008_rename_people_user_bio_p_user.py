# Generated by Django 4.0.4 on 2022-06-04 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_rename_people_address_people_input_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bio',
            old_name='people_user',
            new_name='P_user',
        ),
    ]

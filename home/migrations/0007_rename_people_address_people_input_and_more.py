# Generated by Django 4.0.4 on 2022-06-04 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_people_author_address_people_bio_people_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='people',
            new_name='people_input',
        ),
        migrations.RenameField(
            model_name='bio',
            old_name='people',
            new_name='people_user',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='people',
            new_name='people_id',
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='address',
            name='street_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='address',
            name='street_number',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='people',
            name='Last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='people',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
    ]
# Generated by Django 4.0.4 on 2022-06-05 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_rename_address_people_address_address_people1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_people1',
            field=models.ForeignKey(default=' ', on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='home.people'),
        ),
    ]

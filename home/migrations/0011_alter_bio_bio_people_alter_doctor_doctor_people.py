# Generated by Django 4.0.4 on 2022-06-05 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_bio_bio_people_alter_doctor_doctor_people'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bio',
            name='bio_people',
            field=models.ForeignKey(default=' ', on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='home.people'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='doctor_people',
            field=models.ForeignKey(default=' ', on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='home.people'),
        ),
    ]
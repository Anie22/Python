# Generated by Django 4.0.4 on 2022-06-05 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_remove_address_people_input_remove_bio_p_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bio',
            name='bio_people',
            field=models.ForeignKey(default=' ', on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='home.doctor'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='doctor_people',
            field=models.ForeignKey(default=' ', on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='home.address'),
        ),
    ]
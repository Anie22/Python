# Generated by Django 4.0.4 on 2022-06-05 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_rename_people_user_bio_p_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='people_input',
        ),
        migrations.RemoveField(
            model_name='bio',
            name='P_user',
        ),
        migrations.RemoveField(
            model_name='bio',
            name='email',
        ),
        migrations.RemoveField(
            model_name='bio',
            name='name',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='email',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='people_id',
        ),
        migrations.AddField(
            model_name='address',
            name='address_people',
            field=models.OneToOneField(default=' ', on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='home.people'),
        ),
        migrations.AddField(
            model_name='bio',
            name='bio_people',
            field=models.OneToOneField(default=' ', on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='home.people'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='doctor_people',
            field=models.OneToOneField(default=' ', on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='home.people'),
        ),
    ]

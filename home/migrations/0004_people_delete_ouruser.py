# Generated by Django 4.0.4 on 2022-06-04 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_bio_product_rename_people_ouruser_alter_address_city_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='people',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=1000)),
                ('Last_name', models.CharField(max_length=1000)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.address')),
            ],
        ),
        migrations.DeleteModel(
            name='ouruser',
        ),
    ]

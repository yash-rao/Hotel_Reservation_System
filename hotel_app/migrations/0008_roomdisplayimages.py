# Generated by Django 3.0.7 on 2020-09-10 15:52

from django.db import migrations, models
import django.db.models.deletion
import hotel_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0007_remove_room_display_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomDisplayImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_images', models.ImageField(upload_to=hotel_app.models.room_display_images_upload_path)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel_app.Room')),
            ],
        ),
    ]

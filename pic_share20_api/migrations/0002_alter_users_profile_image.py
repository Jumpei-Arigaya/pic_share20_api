# Generated by Django 4.1.4 on 2022-12-15 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pic_share20_api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="users",
            name="profile_image",
            field=models.ImageField(default="defaultUserIcon.png", upload_to="images/"),
        ),
    ]

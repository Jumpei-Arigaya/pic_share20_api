# Generated by Django 4.1.4 on 2022-12-15 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pic_share20_api", "0003_alter_users_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="users",
            name="profile_image",
            field=models.ImageField(
                default="images/defaultUserIcon_brgqfq", upload_to="images/"
            ),
        ),
    ]

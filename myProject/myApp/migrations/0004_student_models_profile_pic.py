# Generated by Django 4.2.6 on 2023-11-24 09:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myApp", "0003_library_model"),
    ]

    operations = [
        migrations.AddField(
            model_name="student_models",
            name="profile_pic",
            field=models.ImageField(null=True, upload_to="media/profile_pic"),
        ),
    ]

# Generated by Django 3.2.23 on 2023-11-12 13:08

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20231111_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(null=True, upload_to=core.models.get_recipe_image_file_path),
        ),
    ]
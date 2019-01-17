# Generated by Django 2.1.5 on 2019-01-17 10:42

from django.db import migrations, models
import yashoes.model.variant
import yashoes.models


class Migration(migrations.Migration):

    dependencies = [
        ('yashoes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image_profile',
            field=models.ImageField(blank=True, max_length=50000, null=True, upload_to=yashoes.models.get_image_path),
        ),
        migrations.AlterField(
            model_name='variant',
            name='image_link',
            field=models.ImageField(blank=True, max_length=50000, null=True, upload_to=yashoes.model.variant.get_image_path),
        ),
    ]

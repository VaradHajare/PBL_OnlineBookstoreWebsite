# Generated by Django 5.0.1 on 2024-04-09 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_book_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='email',
            field=models.CharField(default=None, max_length=100),
        ),
    ]

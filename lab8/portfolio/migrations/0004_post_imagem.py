# Generated by Django 4.0.4 on 2022-05-16 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_remove_post_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagem',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]

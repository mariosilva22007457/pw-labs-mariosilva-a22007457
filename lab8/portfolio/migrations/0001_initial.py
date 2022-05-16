# Generated by Django 4.0.4 on 2022-05-16 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=100)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.CharField(max_length=500)),
                ('link', models.URLField()),
                ('imagem', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]

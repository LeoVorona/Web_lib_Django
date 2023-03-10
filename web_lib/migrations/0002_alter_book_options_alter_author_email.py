# Generated by Django 4.0.6 on 2022-07-25 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_lib', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'get_latest_by': 'publisherd', 'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Электронная почта'),
        ),
    ]

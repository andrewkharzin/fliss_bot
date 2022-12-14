# Generated by Django 4.1.1 on 2022-10-12 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0007_station'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='airport_e',
            field=models.CharField(default='', max_length=50, verbose_name='Airport E'),
        ),
        migrations.AddField(
            model_name='station',
            name='airport_r',
            field=models.CharField(default='', max_length=50, verbose_name='Airport R'),
        ),
        migrations.AddField(
            model_name='station',
            name='city_e',
            field=models.CharField(default='', max_length=50, verbose_name='City E'),
        ),
        migrations.AddField(
            model_name='station',
            name='city_r',
            field=models.CharField(default='', max_length=50, verbose_name='Sity R'),
        ),
        migrations.AddField(
            model_name='station',
            name='comment_eng',
            field=models.CharField(default='', max_length=50, verbose_name='Comment Eng'),
        ),
        migrations.AddField(
            model_name='station',
            name='comment_rus',
            field=models.CharField(default='', max_length=50, verbose_name='Comment Rus'),
        ),
        migrations.AddField(
            model_name='station',
            name='country',
            field=models.CharField(default='', max_length=50, verbose_name='Country'),
        ),
        migrations.AddField(
            model_name='station',
            name='region',
            field=models.CharField(default='', max_length=50, verbose_name='Region'),
        ),
        migrations.AddField(
            model_name='station',
            name='rus',
            field=models.CharField(default='', max_length=5, verbose_name='Rus'),
        ),
    ]

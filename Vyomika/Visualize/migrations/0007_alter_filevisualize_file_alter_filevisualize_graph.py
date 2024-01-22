# Generated by Django 5.0.1 on 2024-01-22 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Visualize', '0006_filevisualize_plottype_filevisualize_xlabelfile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filevisualize',
            name='file',
            field=models.FileField(default='', upload_to='media/files'),
        ),
        migrations.AlterField(
            model_name='filevisualize',
            name='graph',
            field=models.ImageField(default='', upload_to='files/graphs'),
        ),
    ]

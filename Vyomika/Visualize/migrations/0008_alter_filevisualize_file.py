# Generated by Django 5.0.1 on 2024-01-22 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Visualize', '0007_alter_filevisualize_file_alter_filevisualize_graph'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filevisualize',
            name='file',
            field=models.FileField(default='', upload_to='files'),
        ),
    ]

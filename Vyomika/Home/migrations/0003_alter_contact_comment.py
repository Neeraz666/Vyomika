# Generated by Django 4.2.2 on 2023-06-22 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_alter_contact_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='comment',
            field=models.TextField(),
        ),
    ]
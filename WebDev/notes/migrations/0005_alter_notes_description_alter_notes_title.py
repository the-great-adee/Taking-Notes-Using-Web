# Generated by Django 4.0.6 on 2022-10-11 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_alter_notes_description_alter_notes_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='notes',
            name='title',
            field=models.TextField(),
        ),
    ]

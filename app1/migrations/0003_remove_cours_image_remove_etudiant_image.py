# Generated by Django 4.2.1 on 2023-07-02 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_cours'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cours',
            name='image',
        ),
        migrations.RemoveField(
            model_name='etudiant',
            name='image',
        ),
    ]

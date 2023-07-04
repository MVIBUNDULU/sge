# Generated by Django 4.2.1 on 2023-06-24 22:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=60)),
                ('prenom', models.CharField(max_length=60)),
                ('niveau', models.CharField(max_length=60)),
                ('option', models.CharField(max_length=60)),
                ('adresse', models.CharField(max_length=60)),
                ('tel', models.CharField(max_length=60)),
                ('matricule', models.CharField(max_length=60)),
                ('courssuivi', models.CharField(max_length=60)),
                ('date_naiss', models.DateField()),
                ('image', models.ImageField(upload_to='images/')),
                ('secrete_key', models.UUIDField(default=uuid.uuid4)),
            ],
        ),
    ]
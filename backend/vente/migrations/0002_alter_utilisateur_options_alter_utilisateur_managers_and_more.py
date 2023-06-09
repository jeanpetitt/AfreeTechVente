# Generated by Django 4.1.7 on 2023-03-31 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vente', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='utilisateur',
            options={'verbose_name': 'User'},
        ),
        migrations.AlterModelManagers(
            name='utilisateur',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='username',
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='email',
            field=models.EmailField(max_length=200, unique=True, verbose_name='Email adress'),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='first_name',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='last_name',
            field=models.CharField(max_length=10, null=True),
        ),
    ]

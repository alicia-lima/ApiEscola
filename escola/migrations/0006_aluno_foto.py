# Generated by Django 5.0.1 on 2024-02-16 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0005_aluno_ativo_aluno_celular_aluno_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='foto',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]

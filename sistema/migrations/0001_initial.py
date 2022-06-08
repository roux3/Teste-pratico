# Generated by Django 4.0.5 on 2022-06-04 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.IntegerField(max_length=8)),
                ('endereco', models.TextField()),
                ('numero', models.IntegerField(max_length=6)),
                ('complemento', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=255)),
                ('cidade', models.CharField(max_length=255)),
                ('uf', models.CharField(max_length=2)),
                ('descricao', models.TextField()),
            ],
        ),
    ]
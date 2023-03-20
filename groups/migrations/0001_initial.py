# Generated by Django 4.1.3 on 2022-11-08 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apprenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Brief',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=35)),
                ('url', models.URLField(max_length=100)),
                ('nb_appr_par_nome', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Nome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_nom', models.CharField(max_length=100)),
                ('apprenants', models.ManyToManyField(to='groups.apprenant')),
                ('id_brief', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.brief')),
            ],
        ),
    ]
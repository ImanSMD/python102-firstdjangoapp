# Generated by Django 4.2.7 on 2023-12-21 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_bio_userprofile_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True)),
                ('position', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('userprofile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile')),
            ],
        ),
    ]

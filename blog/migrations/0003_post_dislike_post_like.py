# Generated by Django 4.2.7 on 2023-12-15 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_bio_userprofile_picture'),
        ('blog', '0002_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dislike',
            field=models.ManyToManyField(related_name='dislike', to='accounts.userprofile'),
        ),
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(related_name='like', to='accounts.userprofile'),
        ),
    ]

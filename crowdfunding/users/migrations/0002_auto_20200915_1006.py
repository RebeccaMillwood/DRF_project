# Generated by Django 3.0.8 on 2020-09-15 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='about_me',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.TextField(default='https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/golden-retriever-royalty-free-image-506756303-1560962726.jpg'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='location',
            field=models.TextField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.TextField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.TextField(blank=True, max_length=30),
        ),
    ]

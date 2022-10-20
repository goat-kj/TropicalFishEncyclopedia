# Generated by Django 4.1 on 2022-10-18 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encyclopedia', '0004_rename_acount_staff_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=50)),
                ('details', models.TextField()),
            ],
        ),
    ]

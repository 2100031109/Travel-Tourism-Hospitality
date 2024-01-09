# Generated by Django 4.1.7 on 2023-05-05 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_signupdata_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='packages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pid', models.IntegerField(max_length=10, unique=True)),
                ('price', models.IntegerField(max_length=100)),
                ('imgurl', models.CharField(max_length=100)),
                ('des', models.CharField(max_length=200)),
            ],
        ),
    ]

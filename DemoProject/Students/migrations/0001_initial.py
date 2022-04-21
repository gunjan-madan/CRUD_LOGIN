# Generated by Django 4.0.3 on 2022-04-18 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentID', models.IntegerField()),
                ('studentName', models.CharField(max_length=60)),
                ('studentClass', models.CharField(max_length=20)),
                ('studentSection', models.CharField(max_length=20)),
                ('studentCity', models.CharField(default='NA', max_length=20)),
            ],
        ),
    ]

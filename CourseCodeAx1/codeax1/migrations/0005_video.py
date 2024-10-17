# Generated by Django 4.2.1 on 2023-09-19 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codeax1', '0004_rename_prerequiste_prerequisite'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('video_id', models.CharField(max_length=20)),
                ('isPreview', models.BooleanField(default=False)),
                ('serial_number', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codeax1.course')),
            ],
        ),
    ]

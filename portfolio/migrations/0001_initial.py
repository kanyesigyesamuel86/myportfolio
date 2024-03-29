# Generated by Django 5.0.1 on 2024-02-07 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_field', models.EmailField(max_length=254)),
                ('tel', models.TextField(max_length=200)),
                ('message_field', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program', models.CharField(max_length=255)),
                ('school_or_university', models.CharField(max_length=255)),
                ('grade', models.FloatField()),
                ('year_started', models.IntegerField(blank=True, null=True)),
                ('year_ended', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('work_done', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('area_of_study', models.CharField(max_length=255)),
                ('contact_number_1', models.CharField(max_length=20)),
                ('contact_number_2', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('github_url', models.URLField()),
                ('summary', models.TextField()),
                ('achievements', models.ManyToManyField(to='portfolio.achievement')),
                ('education', models.ManyToManyField(to='portfolio.education')),
                ('hobby', models.ManyToManyField(to='portfolio.hobby')),
                ('project', models.ManyToManyField(to='portfolio.project')),
                ('skills', models.ManyToManyField(to='portfolio.skill')),
                ('work_experiences', models.ManyToManyField(to='portfolio.workexperience')),
            ],
        ),
    ]

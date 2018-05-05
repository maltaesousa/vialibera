# Generated by Django 2.0.5 on 2018-05-05 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('datetime_start', models.DateTimeField()),
                ('datetime_end', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Enrolment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enrolments.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('address', models.TextField()),
                ('zipcode', models.IntegerField()),
                ('city', models.TextField()),
                ('mail', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('birthdate', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='enrolment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enrolments.Student'),
        ),
    ]

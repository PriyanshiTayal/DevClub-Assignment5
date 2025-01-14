# Generated by Django 4.0.6 on 2022-08-06 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0004_remove_course_instructor_id_alter_course_course_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc', models.FileField(upload_to='Docs')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.subject')),
            ],
        ),
    ]

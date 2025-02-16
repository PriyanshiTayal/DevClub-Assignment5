# Generated by Django 4.0.6 on 2022-08-07 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0007_alter_session_end_year_alter_session_start_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstructorFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField()),
                ('feedback_reply', models.TextField(default='')),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
                ('instructor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.instructor')),
            ],
        ),
    ]

# Generated by Django 4.0.6 on 2022-08-06 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_student_course_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='address',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='student',
            name='course_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='users.course'),
        ),
    ]

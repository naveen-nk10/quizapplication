# Generated by Django 3.1.1 on 2021-05-20 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz_question',
            name='quiz_quest',
        ),
        migrations.AddField(
            model_name='quiz_question',
            name='quiz_quest',
            field=models.ManyToManyField(to='quizapp.Quizname'),
        ),
    ]

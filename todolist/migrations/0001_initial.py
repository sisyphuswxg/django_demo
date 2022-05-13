# Generated by Django 4.0.4 on 2022-05-11 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Username',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('date_of_creation', models.DateTimeField(auto_now_add=True)),
                ('priority', models.CharField(choices=[('adanger', 'Priority High'), ('bwarning', 'Priority Medium'), ('csuccess', 'Priority Low')], default='adanger', max_length=30)),
                ('complete', models.IntegerField(default=0)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todolist.username')),
            ],
        ),
    ]

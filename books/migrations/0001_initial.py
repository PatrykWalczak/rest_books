# Generated by Django 3.2.4 on 2021-06-06 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('published_date', models.IntegerField()),
                ('average_rating', models.FloatField(null=True)),
                ('rating_count', models.IntegerField(null=True)),
                ('thumbnail', models.URLField(max_length=150)),
                ('authors', models.ManyToManyField(to='books.Author')),
                ('categories', models.ManyToManyField(to='books.Category')),
            ],
        ),
    ]

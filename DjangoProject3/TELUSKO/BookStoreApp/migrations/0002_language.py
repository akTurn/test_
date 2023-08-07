# Generated by Django 4.2.3 on 2023-07-20 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookStoreApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)", max_length=200)),
            ],
        ),
    ]
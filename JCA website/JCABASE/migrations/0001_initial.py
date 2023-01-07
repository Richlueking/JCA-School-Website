# Generated by Django 4.1.4 on 2023-01-07 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_pic', models.ImageField(default='', null=True, upload_to='')),
                ('writer', models.CharField(max_length=200)),
                ('blog_title', models.CharField(max_length=200)),
                ('paragraph', models.TextField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_pic', models.ImageField(default='', null=True, upload_to='')),
                ('news_title', models.CharField(max_length=200)),
                ('news_content', models.TextField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Parents_review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_pic', models.ImageField(default='', null=True, upload_to='')),
                ('parent_name', models.CharField(max_length=200, null=True)),
                ('remark', models.TextField(null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_pic', models.ImageField(default='', null=True, upload_to='')),
                ('teacher_name', models.CharField(max_length=200, null=True)),
                ('teacher_title', models.CharField(max_length=200)),
                ('date_join', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_join'],
            },
        ),
    ]
# Generated by Django 4.1.3 on 2022-11-18 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blog_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='categories',
            field=models.ManyToManyField(related_name='getBlogs', to='blog.category', verbose_name='Categorías'),
        ),
    ]

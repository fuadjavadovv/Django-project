# Generated by Django 3.2.6 on 2021-09-14 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='courses/images.jfif', null=True, upload_to='', verbose_name='Meqaleye sekil yukleyin...'),
        ),
    ]
# Generated by Django 4.1.7 on 2023-04-06 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_testimonials_student_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutcard',
            options={'verbose_name_plural': 'About Card'},
        ),
        migrations.AlterModelOptions(
            name='accreditations',
            options={'verbose_name_plural': 'Accreditations'},
        ),
        migrations.AlterModelOptions(
            name='ceomessage',
            options={'verbose_name_plural': 'Ceo Message'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name_plural': 'Contact'},
        ),
        migrations.AlterModelOptions(
            name='courseprovide',
            options={'verbose_name_plural': 'Course Provide'},
        ),
        migrations.AlterModelOptions(
            name='moments',
            options={'verbose_name_plural': 'Moments'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name_plural': 'Service'},
        ),
        migrations.AlterModelOptions(
            name='servicingcountries',
            options={'verbose_name_plural': 'Servicing Countries'},
        ),
        migrations.AlterModelOptions(
            name='testimonials',
            options={'verbose_name_plural': 'Testimonials'},
        ),
        migrations.AlterModelOptions(
            name='university',
            options={'verbose_name_plural': 'University'},
        ),
    ]

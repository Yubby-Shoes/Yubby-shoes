# Generated by Django 3.1.2 on 2020-11-06 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(default='Dhangadhi', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='default_size',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(default='Anjal Bam', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(default='9866967971', max_length=10, unique=True),
            preserve_default=False,
        ),
    ]
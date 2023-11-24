# Generated by Django 4.1 on 2023-11-24 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SliderImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/%Y/%m')),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('sort', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ('sort',),
            },
        ),
    ]

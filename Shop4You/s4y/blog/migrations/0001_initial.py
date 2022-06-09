# Generated by Django 3.1.7 on 2022-01-11 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('post_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=100)),
                ('Head_0', models.CharField(max_length=2000)),
                ('Content_Head_0', models.CharField(max_length=2000)),
                ('Head_1', models.CharField(max_length=2000)),
                ('Content_Head_1', models.CharField(max_length=2000)),
                ('Head_2', models.CharField(max_length=2000)),
                ('Content_Head_2', models.CharField(max_length=1000)),
                ('published_date', models.DateField()),
                ('thumbnail', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]

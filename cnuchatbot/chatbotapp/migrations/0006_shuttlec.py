# Generated by Django 3.1.7 on 2022-03-02 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbotapp', '0005_auto_20220227_1706'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShuttleC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction', models.CharField(max_length=30, null=True, verbose_name='방향')),
                ('departureTime', models.TimeField(max_length=30, null=True, verbose_name='c노선 출발시간')),
            ],
        ),
    ]
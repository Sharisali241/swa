# Generated by Django 3.1 on 2023-01-26 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SEOAnalyzer', '0003_auto_20230113_1223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('String_data', models.CharField(max_length=50)),
                ('Int_data', models.IntegerField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Content_Analysis',
        ),
    ]

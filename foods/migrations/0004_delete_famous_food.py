# Generated by Django 4.1.3 on 2022-11-30 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0003_remove_famous_food_description'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Famous_Food',
        ),
    ]

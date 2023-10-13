# Generated by Django 4.1.3 on 2022-11-30 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Famous_Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام')),
                ('description', models.CharField(max_length=500, verbose_name='توضیحات')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('time', models.IntegerField(verbose_name='زمان لازم')),
                ('photo', models.ImageField(upload_to='famous_foods/', verbose_name='عکس')),
                ('type_food', models.CharField(choices=[('breakfast', 'صبحانه'), ('lunch', 'ناهار'), ('dinner', 'شام')], default='lunch', max_length=10, verbose_name='نوع غذا')),
            ],
            options={
                'verbose_name': 'محبوب ترین غذا',
                'verbose_name_plural': 'محبوب ترین غذاها',
            },
        ),
    ]

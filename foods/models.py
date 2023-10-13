from django.db import models
from django.utils.translation import gettext as _
# Create your models here.


class Food(models.Model):
    class Meta:
        verbose_name = 'غذا'
        verbose_name_plural = 'غذا'
    FOOD_TYPE = [
        ("breakfast","صبحانه"),
        ("lunch","ناهار"),
        ("dinner","شام"),
    ]
    name = models.CharField(_("نام"),max_length=100)
    description = models.CharField(_("توضیحات"),max_length=500)
    price = models.IntegerField(_("قیمت"),)
    time = models.IntegerField(_("زمان لازم"))
    photo = models.ImageField(_("عکس"),upload_to = "foods/")
    type_food = models.CharField(_("نوع غذا"),max_length=10,choices=FOOD_TYPE,default="lunch")
    
    def __str__(self):
        return self.name




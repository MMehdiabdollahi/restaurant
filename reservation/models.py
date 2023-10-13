from django.db import models
from django.utils.translation import gettext as _
# Create your models here.

class RangeTime(models.Model):
    class Meta:
        verbose_name = 'بازه زمانی'
        verbose_name_plural = 'بازه زمانی'
    RangeTime_id = models.IntegerField(_("آیدی"),primary_key=True)
    title = models.CharField(_("عنوان"),max_length=40)

    def __str__(self):
        return self.title


class RestaurantTable(models.Model):
    class Meta:
        verbose_name = 'میز'
        verbose_name_plural = 'میز'
    
    frangetime = models.ForeignKey(RangeTime, on_delete=models.CASCADE)
    RestaurantTable_id = models.IntegerField(_("آیدی میز رستوران"),primary_key=True)

    def __str__(self):
        return self.RestaurantTable_id


class Reservation(models.Model):
    class Meta:
        verbose_name = 'رزرو'
        verbose_name_plural = 'رزرو'
    name = models.CharField(_("نام و نام خانوادگی"),max_length=200)
    email = models.EmailField(_("ایمیل"),max_length=254)
    phone = models.CharField(_("تلفن"),max_length=20)
    number = models.IntegerField(_("تعداد نفرات"))
    date = models.DateField(_("تاریخ"),auto_now=False,auto_now_add=False)
    time = models.TimeField(_("ساعت"),auto_now=False,auto_now_add=False)

    def __str__(self):
        return self.name
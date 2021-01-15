from django.db import models

# Create your models here.


class City_list(models.Model):
    # i want multiple cities so i make a table in db from which the city names will come and city_name is the field of class city_list
    city_name = models.CharField(max_length=200)

    def __str__(self):
        return self.city_name

    class Meta:
        verbose_name_plural = 'cities'  # city's plural form is cities

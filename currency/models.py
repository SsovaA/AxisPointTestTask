from django.db import models

class Currency(models.Model):
    id = models.CharField(primary_key=True, max_length=100, verbose_name="ID", default="")
    name = models.CharField(max_length=100, verbose_name="Название", default="")
    rate = models.FloatField(default=0, verbose_name="Курс по отношению к рублю")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Курс валют"
        verbose_name_plural = "Курс валют"

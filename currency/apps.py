from django.apps import AppConfig


class CurrencyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'currency'
    verbose_name = "Курс валют"
    verbose_name_plural = "Курс валют"

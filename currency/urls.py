from django.urls import path

from .views import GetCurrencyByIdAPIView, GetAllAPIView

app_name = 'currency'
urlpatterns = [
    path('currency/', GetCurrencyByIdAPIView.as_view()),
    path('currencies/', GetAllAPIView.as_view()),
]
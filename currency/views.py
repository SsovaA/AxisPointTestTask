from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class GetCurrencyByIdAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        data = Currency.objects.get(id = request.query_params.get('id'))
        currency_serializer = CurrencySerializer(data)
        return Response(currency_serializer.data, status=status.HTTP_200_OK)

class GetAllAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):

        data = Currency.objects.all()

        paginator = Paginator(data, 10)
        page = request.GET.get('page')

        try:
            response = paginator.page(page)
        except PageNotAnInteger:
            response = paginator.page(1)
        except EmptyPage:
            response = paginator.page(paginator.num_pages)
        currency_serializer = CurrencySerializer(response, many=True)
        return Response(currency_serializer.data, status=status.HTTP_200_OK)

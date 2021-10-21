from django.core.management.base import BaseCommand
from lxml import etree
import requests
from currency.serializers import CurrencySerializer

from locale import *
setlocale(LC_NUMERIC, '')

url = "http://www.cbr.ru/scripts/XML_daily.asp"

class Command(BaseCommand):

    def handle(self, *args, **options):
        xml = requests.get(url)

        curr_now = {}
        root = etree.fromstring(xml.content)
        for curr in root.getchildren():
            
            #print(curr.get("ID"))
            curr_now['id'] = curr.get("ID")

            for elem in curr.getchildren():
                if elem.tag == "Name":
                    curr_now['name'] = elem.text
                if elem.tag == "Value":
                    curr_now['rate'] = atof(elem.text)

            #print(curr_now)

            currency_serializer = CurrencySerializer(data=curr_now)
            #currency_serializer.is_valid(raise_exception=True)
            if currency_serializer.is_valid():
                currency_serializer.save()

            
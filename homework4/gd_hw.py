import requests
import xml.etree.ElementTree as ET
from decimal import Decimal


def currency_rates(valut):

    requests_xml = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    print('Update Time:', requests_xml.headers['Date'])

    tree_xml_set = ET.fromstring(requests_xml.content)

    valut_id = None
    if valut == 'USD':
        valut_id = './/Valute[@ID="R01235"]/Value'
    elif valut == 'EUR':
        valut_id = './/Valute[@ID="R01239"]/Value'

    currency_withdrawal = None
    for pan in tree_xml_set.findall(valut_id):
        currency = pan.text
        currency_withdrawal = Decimal(str(currency.replace(',', '.')))

    print(f'Курс {valut} {currency_withdrawal.quantize(Decimal("1.00"))}')

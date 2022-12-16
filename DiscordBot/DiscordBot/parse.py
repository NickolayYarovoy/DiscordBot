import requests
import xml.etree.ElementTree as ET 

def get_currencies(cur: str) -> str:
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    xml = ET.fromstring(response.text)
    for child in xml:
        print(child.find('CharCode').text)
        if child.find('CharCode').text == cur.upper():
            return f"{child.find('Nominal').text} {child.find('Name').text} стоит {child.find('Value').text} рублей на {xml.get('Date')}"

    return 'Валюта не найдена'








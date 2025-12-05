import requests
import xml.etree.ElementTree as ET

CBR_API_URL = "https://www.cbr.ru/scripts/XML_daily.asp"

def get_all_currencies():
    """
    Возвращает список всех валют ЦБ РФ + RUB.
    """
    response = requests.get(CBR_API_URL)
    response.raise_for_status()

    tree = ET.fromstring(response.content)

    currencies = [{"code": "RUB", "name": "Российский рубль"}]

    for valute in tree.findall("Valute"):
        code = valute.find("CharCode").text
        name = valute.find("Name").text
        currencies.append({"code": code, "name": name})

    return currencies


def get_rate(currency_code: str) -> float:
    currency_code = currency_code.upper()

    # Рубль — базовая валюта
    if currency_code == "RUB":
        return 1.0

    response = requests.get(CBR_API_URL)
    response.raise_for_status()
    tree = ET.fromstring(response.content)

    for valute in tree.findall("Valute"):
        code = valute.find("CharCode").text
        if code == currency_code:
            value = valute.find("Value").text.replace(',', '.')
            nominal = valute.find("Nominal").text
            return float(value) / float(nominal)

    raise ValueError(f"Валюта не найдена: {currency_code}")
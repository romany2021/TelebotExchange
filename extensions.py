import requests
import json
from config import keys


class APIException(Exception):
    pass


class Converter:
    @staticmethod
    def get_price(quote, base, amount):
        try:
            quote_key = keys[base.lower()]
        except KeyError:
            raise APIException(f"Ошибка ввода волюты {quote}")

        try:
            base_key=keys[base.lower()]
        except KeyError:
            raise APIException(f"Ошибка ввода волюты {base}")

        if quote_key == base_key:
            raise APIException(f'Oдинаковые валюты {quote}!')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Ошибка в количестве: {amount}!')

        r = requests.get(f"https://api.exchangeratesapi.io/latest?base={quote_key}&symbols={base_key}")
        resp = json.loads(r.content)
        new_price = resp['rates'][base_key] * amount
        new_price = round(new_price, 3)
        message = f"Цена {amount} {quote} в {base} : {new_price}"
        return message
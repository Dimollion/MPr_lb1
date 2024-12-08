import requests
import json

r = requests.get('https://bank.gov.ua/NBU_Exchange/exchange_site?start=20241202&end=20241206&valcode=eur&json')

r_js = json.loads(r.text)
table_dict = {}
for i in r_js:
    table_dict[i['exchangedate']] = i['rate']
print(table_dict)
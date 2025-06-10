import json


def parsing_contragen_json():
    with open('contragent.json', 'r', encoding='utf-8') as file:
        data_contragent_json = json.load(file)
        return data_contragent_json


def parsing_user_json():
    with open('user.json', 'r', encoding='utf-8') as file:
        data_user_json = json.load(file)
        return data_user_json

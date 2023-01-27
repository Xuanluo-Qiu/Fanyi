import requests
import json

api = "http://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i="

def get_word(word):
    get_data = requests.get(api+word)
    json_data = get_data.json()
    text_data = json_data.get("translateResult")
    return text_data[0][0]["tgt"]

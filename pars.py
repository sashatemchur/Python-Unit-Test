import requests
from fastapi import FastAPI
import json


class Pars:
    
    def __init__(self):
        ...
        
    def pars(self):
        app = FastAPI()
        api = "https://dummyjson.com/products"
        output = requests.get(api)
        output = output.json()
        with open("data.json", "w", encoding="UTF-8") as data: 
            json.dump(output, data, indent=4)
            
    def api(self):
        app = FastAPI()
        api = "https://dummyjson.com/products"
        output = requests.get(api)
        output = output.json()
        with open("data.json", "r", encoding="UTF-8") as data: 
            output_data = json.load(data)
        return output_data

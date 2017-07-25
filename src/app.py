from datetime import time
from time import *
import requests
import time
from bs4 import BeautifulSoup
from flask import Flask
from Busca import hunting


app = Flask(__name__)


@app.route('/')
def main():
    return hunt()


def hunt():
    while True:
        print("Iniciando as buscas... " + strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        print("Busca no HardMob...")
        request = requests.get("http://www.hardmob.com.br/promocoes/")
        content = request.content
        soup = BeautifulSoup(content, "html.parser")
        element = soup.find_all("a", {"class": "title"})
        hunting(element, "Monitor")
        hunting(element, "Z2")

        print("Busca no promobit")
        request = requests.get("https://www.promobit.com.br/")
        content = request.content
        soup = BeautifulSoup(content, "html.parser")
        element = soup.find_all("a", {"itemprop": "name", "class": "access_url "})
        hunting(element, "Monitor")
        hunting(element, "Z2")

        print("Executado em:" + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "\n")
        time.sleep(60*5)

if __name__ == '__main__':
    hunt()



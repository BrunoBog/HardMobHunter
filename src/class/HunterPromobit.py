import requests
from bs4 import BeautifulSoup

from src.models import produto, Pessoa, produto


class HunterPromobit(object):
    lista = []

    @classmethod
    def busca(cls, procura, nome, email):
        request = requests.get("https://www.promobit.com.br/")
        content = request.content
        soup = BeautifulSoup(content, "html.parser")

        promocao = soup.find_all("div", {"itemscope": "", "class": "pr-tl-card"})
        for x in promocao:
            i = soup.find("a", {"itemprop": "name", "class": "access_url "})
            l = soup.find("span", {"itemprop": "lowPrice"})
            link = "https://www.promobit.com.br/" + i.attrs['href']
            prod = produto(nome=i.text, preco=l.text, link=link)
            cls.verifica_produto(prod, procura, nome, email)

    @classmethod
    def verifica_produto(cls,produto, procura, nome, email):
        if not cls.lista.__contains__(produto):
            if produto.is_procurado(procura):
                pessoa = Pessoa(nome=nome, email=email,produto=produto)
                pessoa.send_hunt_mail()
                cls.lista.append(produto)

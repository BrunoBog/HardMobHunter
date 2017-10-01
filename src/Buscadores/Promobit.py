import requests
from bs4 import BeautifulSoup
from src.models.Pessoa import Pessoa
from src.models.produto import Produto


class Promobit(object):
    def __init__(self):
        self.lista = []

    def busca(self, procura, nome, email):
        request = requests.get("https://www.promobit.com.br/")
        content = request.content
        soup = BeautifulSoup(content, "html.parser")

        promocao = soup.find_all("div", {"itemscope": "", "class": "pr-tl-card"})
        for x in promocao:
            i = soup.find("a", {"itemprop": "name", "class": "access_url "})
            promo = soup.find("span", {"itemprop": "lowPrice"})
            link = "https://www.promobit.com.br/" + i.attrs['href']
            prod = Produto(nome=i.text, preco=promo.text, link=link)
            self.verifica_produto(produto=prod, procura=procura, nome=nome, email=email)

    def verifica_produto(self, produto, procura, nome, email):
        if not any(x.nome == produto.nome for x in self.lista):
            if produto.is_procurado(procura):
                pessoa = Pessoa(nome=nome, email=email, produto=produto)
                pessoa.send_hunt_mail()

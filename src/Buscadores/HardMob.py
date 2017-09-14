import requests
from bs4 import BeautifulSoup

from src.models.Pessoa import Pessoa
from src.models.produto import Produto


class HardMob(object):
    lista = []

    @classmethod
    def busca(cls, procura, nome, email):
        request = requests.get("http://www.hardmob.com.br/promocoes/")
        content = request.content
        soup = BeautifulSoup(content, "html.parser")

        soup = BeautifulSoup(content, "html.parser")
        element = soup.find_all("a", {"class": "title"})
        for i in element:
            preco = i.text[i.text.find("$")-1::]
            link = i.attrs['href']
            nome = i.text
            prod = Produto(nome=nome, preco=preco, link=link)
            cls.verifica_produto(produto=prod,
                                 procura=procura,
                                 nome=nome,
                                 email=email)

    @classmethod
    def verifica_produto(cls, produto, procura, nome, email):
        if not cls.lista.__contains__(produto):
            if produto.is_procurado(procura):
                pessoa = Pessoa(nome=nome, email=email, produto=produto)
                pessoa.send_hunt_mail()
                cls.lista.append(produto)
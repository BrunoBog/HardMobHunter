# -*- coding: utf-8 -*-
from time import strftime, gmtime
import time
from src.Buscadores.HardMob import HardMob
from src.Buscadores.Promobit import Promobit
from src.database.firebase import DbFirebase
from src.models import Desejos
db = DbFirebase()


def adicionar_desejos(collection):
    desejos = Desejos.Desejos("items")
    desejos.adicionarItem("more items")
    pedido = Desejos.Pedidos(nome="Nome da pessoa", email="teste@gmail.com", desejos=desejos)
    db.incluir(collection, pedido.json())


def buscar_desejos():
    hardmob = HardMob()
    promobit = Promobit()
    while True:
        desejo = Desejos.Desejos()
        pedido = db.buscar_todos("hardHunter")

        for p in pedido.each(): #qui tenho cada pessoa
            for desejo in p.val()['desejos']: # aqui cada item a procurar

                promobit.busca(procura=desejo,
                               nome=p.val()['nome'],
                               email=p.val()['email'])

                hardmob.busca(procura=desejo,
                              nome=p.val()['nome'],
                              email=p.val()['email'])

    print("\n Executado em:" + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "\n")
    time.sleep(60 * 5)


if __name__ == '__main__':
    buscar_desejos()

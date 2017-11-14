# -*- coding: utf-8 -*-
import time
import datetime
from src.Buscadores.HardMob import HardMob
from src.Buscadores.Promobit import Promobit
from src.database.firebase import DbFirebase
from src.models import Desejos


db = DbFirebase()


def buscar_desejos():

    hardmob = HardMob()
    promobit = Promobit()
    db.refresh_token()
    pedido = db.buscar_todos("hardHunter")
    while True:
        print("\nIniciando em:" + str(datetime.datetime.now()))
        for p in pedido.each():  # qui tenho cada pessoa
            for desejo in p.val()['desejos']:  # aqui cada item a procurar
                print("procurando " + desejo)  # + " Em: " + strftime("%Y-%m-%d %H:%M:%S", gmtime()))
                promobit.busca(procura=desejo, nome=p.val()['nome'], email=p.val()['email'])
                hardmob.busca(procura=desejo, nome=p.val()['nome'], email=p.val()['email'])

        print("\nExecutado em:" + str(datetime.datetime.now()))
        print("proxima exec em 5 minutos")
        time.sleep(60 * 5)


def adicionar_desejos(collection):
    desejos = Desejos.Desejos("Painel")
    # desejos.adicionar_item("Outro item")
    pedido = Desejos.Pedidos(nome="Bruno", email="bog906@gmail.com", desejos=desejos)
    db.incluir2(collection, pedido.json())


if __name__ == '__main__':
    # buscar_desejos()
    adicionar_desejos("hardHunter")

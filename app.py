# -*- coding: utf-8 -*-
import time
import datetime
from src.Buscadores.HardMob import HardMob
from src.Buscadores.Promobit import Promobit
from src.database.firebase import DbFirebase
from src.models import Desejos


tempo_refresh = datetime.datetime.now()

def buscar_desejos():

    if int(tempo_refresh.hour - datetime.datetime.now().hour) > 0:
        DbFirebase.refresh_token()

    pedido = DbFirebase.buscar_todos("hardHunter")
    return pedido


def procurar_desejos():

    hardmob = HardMob()
    promobit = Promobit()
    pedido = buscar_desejos()
    while True:


        print("\nIniciando em:" + str(datetime.datetime.now()))
        for p in pedido.each():  # qui tenho cada pessoa
            for desejo in (p.val()['desejos']):  # aqui cada item a procurar
                if desejo is not None:
                    print("procurando " + desejo + " para o " + p.val()['nome'] )  # + " Em: " + strftime("%Y-%m-%d %H:%M:%S", gmtime()))
                    promobit.busca(procura=desejo, nome=p.val()['nome'], email=p.val()['email'])
                    hardmob.busca(procura=desejo, nome=p.val()['nome'], email=p.val()['email'])

        print("\nExecutado em:" + str(datetime.datetime.now()))
        print("proxima exec em 5 minutos")
        time.sleep(60 * 5)

def adicionar_desejos(collection):
    desejos = Desejos.Desejos()
    desejos.adicionar_item("item")
    pedido = Desejos.Pedidos(nome="Nome", email="name@gmail.com", desejos=desejos)
    DbFirebase.incluir(collection, pedido.json())


if __name__ == '__main__':
    procurar_desejos()
    # adicionar_desejos("hardHunter")

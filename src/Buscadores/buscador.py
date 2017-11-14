import datetime

import time

from src.Buscadores.HardMob import HardMob
from src.Buscadores.Promobit import Promobit
from src.database.firebase import DbFirebase
from src.models.Desejos import Desejos

class buscador(object):

    def __init__(self):
        self.db = DbFirebase
        self.db.inicialisar()
        self.data_inicio = datetime.datetime.now()
        self.ultimo_refresh = self.data_inicio.hour

    def verifica_data(self):
        data_atual = datetime.datetime.now()
        if self.data_inicio.day != data_atual.day:
            self.data_inicio = datetime.datetime.now()
            self.db.refresh()
            self.ultimo_refresh = self.data_inicio.hour
            return True

        if self.ultimo_refresh < data_atual.hour:
            self.db.refresh()
            self.ultimo_refresh = data_atual.hour
            return True


    def buscar_desejos(self):
        lista = []
        hardmob = HardMob()
        promobit = Promobit()
        pedido = self.db.buscar_todos("hardHunter")

        while True:
            if self.verifica_data():
                pedido = self.db.buscar_todos("hardHunter")

            print("\nIniciando em:" + str(datetime.datetime.now()))
            for p in pedido.each():  # qui tenho cada pessoa
                for desejo in p.val()['desejos']:  # aqui cada item a procurar
                    if desejo is not None:
                        print("procurando " + desejo + " para o " + p.val()['nome'])
                        # + " Em: " + strftime("%Y-%m-%d %H:%M:%S", gmtime()))
                        lista = promobit.busca(procura=desejo, nome=p.val()['nome'], email=p.val()['email'],
                                               lista=lista)
                        lista = hardmob.busca(procura=desejo, nome=p.val()['nome'], email=p.val()['email'], lista=lista)

            print("\nExecutado em:" + str(datetime.datetime.now()))
            print("proxima exec em 5 minutos")
            time.sleep(60 * 5)

    def adicionar_desejos(self,collection):
        desejos = Desejos.Desejos("Item")
        desejos.adicionar_item("Outro item")
        pedido = Desejos.Pedidos(nome="Nome", email="name@gmail.com", desejos=desejos)
        db.incluir(collection, pedido.json())


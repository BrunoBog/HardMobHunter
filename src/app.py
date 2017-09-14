# -*- coding: utf-8 -*-
from time import strftime, gmtime

import time

from src.Buscadores.HardMob import HardMob
from src.Buscadores.Promobit import Promobit


def hunt():
    while True:
        print("Busca no promobit")
        promobit = Promobit
        promobit.busca(procura="cama", nome="Senhor", email="teste@gmail.com")
        promobit.busca(procura="k10", nome="Senhor", email="teste@gmail.com")

        print("Busca no HardMob")
        hardmob = HardMob
        hardmob.busca(procura="Havaiana", nome="Senhor", email="teste@gmail.com")
        hardmob.busca(procura="Havaiana", nome="Senhor", email="teste@teste")
        print("Executado em:" + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "\n")
        time.sleep(60*5)


if __name__ == '__main__':
    hunt()


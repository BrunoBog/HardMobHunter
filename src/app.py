# -*- coding: utf-8 -*-
from time import strftime, gmtime, time

from src.Buscadores.Promobit import Promobit


def hunt():
    while True:
        print("Busca no promobit")
        promobit = Promobit
        promobit.busca(procura=" ", nome="Bruno", email="email@gmail.com")

        print("Executado em:" + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "\n")
        time.sleep(60*5)


if __name__ == '__main__':
    hunt()



# -*- coding: utf-8 -*-
import time
import datetime
from src.Buscadores.HardMob import HardMob
from src.Buscadores.Promobit import Promobit
from src.Buscadores.buscador import buscador
from src.database.firebase import DbFirebase
from src.models import Desejos

if __name__ == '__main__':
    buscar = buscador()
    buscar.buscar_desejos()
    # buscar.adicionar_desejos("hardHunter")

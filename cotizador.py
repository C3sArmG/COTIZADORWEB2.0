# cotizador.py
from datetime import datetime
import pandas as pd

# Dependiendo su kilometraje, se le resta un valor
#Necesito revisar el valor kiloemtraje, recordar que varia según la rotación.
def calcular_valor_kilometraje(kilometraje,rotacion):
    rotacion == 'Alta'
    if kilometraje <= 30000:
        return 0 
    elif kilometraje <= 60000:
        return 300  
    elif kilometraje <= 100000:
        return 750  
    else:
        return 1000
    rotacion == 'Media'
    if kilometraje <= 30000:
        return 300 
    elif kilometraje <= 60000:
        return 500  
    elif kilometraje <= 100000:
        return 1000  
    else:
        return 2000
    rotacion == 'Baja'
    if kilometraje <= 30000:
        return 500 
    elif kilometraje <= 60000:
        return 1000  
    elif kilometraje <= 100000:
        return 2000  
    else:
        return 4000

def calcular_tipo_auto(kilometraje, tipo_auto):
    tipo_auto == 'Comercial'
    if kilometraje <= 30000:
        return 200 
    elif kilometraje <= 60000:
        return 350  
    elif kilometraje <= 100000:
        return 500  
    else:
        return 700

    tipo_auto == 'Lujo'
    if kilometraje <= 30000:
        return 400 
    elif kilometraje <= 60000:
        return 700  
    elif kilometraje <= 100000:
        return 1500  
    else:
        return 2500

# En esta parte defino, la utilidad teniendo en cuenta su rotación (baja, media, alta)
def calcular_utilidad_estimada(pvp_mercado, rotacion):
    rango = [
        {"min": 1,    "max": 6000, "baja": 2000, "media": 1500, "alta": 1000},
        {"min": 6001, "max": 10000, "baja": 2500, "media": 2000, "alta": 1500},
        {"min": 10001, "max": 13000, "baja": 2800, "media": 2200, "alta": 1700},
        {"min": 13001, "max": 17000, "baja": 3500, "media": 2400, "alta": 1900},
        {"min": 17001, "max": 21000, "baja": 3600, "media": 2600, "alta": 2100},
        {"min": 21001, "max": 25000, "baja": 3900, "media": 2900, "alta": 2400},
        {"min": 25001, "max": 30000, "baja": 4400, "media": 3400, "alta": 2900},
        {"min": 30001, "max": 35000, "baja": 5000, "media": 4000, "alta": 3500},
        {"min": 35001, "max": 40000, "baja": 55000, "media": 4500, "alta": 4000},
        {"min": 40001, "max": 45000, "baja": 6000, "media": 5000, "alta": 4500},
        {"min": 45001, "max": 50000, "baja": 7000, "media": 6000, "alta": 5500},
        {"min": 50001, "max": 55000, "baja": 9000, "media": 8000, "alta": 6500},
        {"min": 55001, "max": 60000, "baja": 10000, "media": 9000, "alta": 7500},
        {"min": 60001, "max": 65000, "baja": 11000, "media": 10000, "alta": 8500},
        {"min": 65001, "max": 70000, "baja": 12000, "media": 11000, "alta": 9500},
        {"min": 70001, "max": 85000, "baja": 13000, "media": 12000, "alta": 11000},
    ]
    
    for r in rango:
        if r["min"] <= pvp_mercado <= r["max"]:
            return r[rotacion]
    
# Hago los cálculos teniendo en cuento el kilometraje que es ingresado por el usuario, y en este caso también ingresabamos el pvp_mercado
def cotizar_auto(pvp_mercado, kilometraje, rotacion, tipo_auto):
    valor_por_kilometraje = calcular_valor_kilometraje(kilometraje,rotacion)
    valor_por_tipo_de_auto = calcular_tipo_auto(kilometraje, tipo_auto)
    utilidad_estimada = calcular_utilidad_estimada(pvp_mercado, rotacion)
    valor_final = pvp_mercado - utilidad_estimada - valor_por_kilometraje - valor_por_tipo_de_auto
    return valor_final

def valor_partepago (valor_final):
    valor_partepago = valor_final * 1.02
    return valor_partepago

def valor_partepago2(valor_final):
    valor_partepago2 = valor_final * 1.04
    return valor_partepago2

def valor_oferta_maxima(valor_final):
    valor_oferta_maxima = valor_final * 1.05
    return valor_oferta_maxima

    
    
 


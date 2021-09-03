#!/bin/python3

"""
    Blinky en Python para puerto GPIO22

    Enciende y apaga el puerto GPIO22

    Autor: Daniel M. Barrera Leguizamón
"""

import wiringpi

wiringpi.wiringPiSetup()                # Inicializamos la configuración de la librería
wiringpi.wiringPiSetupSys()             # Inicializamos la confiuración del sistema
wiringpi.wiringPiSetupGpio()            # Inicializamos los puertos
wiringpi.pinMode(22,1)                  # Configuramos el puerto GPIO22 como salida 1->OUTPUT 0->INPUT


while 1:
    wiringpi.digitalWrite(22,1)         # Encendemos el puerto GPIO22
    wiringpi.digitalWrite(22,0)         # Apagamos el puerto GPIO22
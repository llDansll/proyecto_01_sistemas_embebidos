#!/bin/bash

#       Blinky en Bash para puerto GPIO22
#
#       Enciende y apaga el puerto GPIO22
#
#       Autor: Daniel M. Barrera Leguizamón

#Inicializamos la configuación del puerto
sleep 1
#Creamos el directorio para la manipulación del GPIO22
echo "22" > /sys/class/gpio/export
sleep 1
#Configuramos el puerto GPIO22 como salida
echo "out" > /sys/class/gpio/gpio22/direction
sleep 1

while [ 1 ]
do
#Encendemos el puerto GPIO22
    echo "1" > /sys/class/gpio/gpio22/value
#Apagamos el puerto GPIO22
    echo "0" > /sys/class/gpio/gpio22/value
done
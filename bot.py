#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telebot
#from libs.keyboard import *
import private as tk
from libs import user_funcs as user
import random
import time

#CONFIGURACIÓN DE TELEGRAM
token = tk.tk()
bot = telebot.TeleBot(token)


#Simplifica el enviar
def send(m, message_text):
    bot.send_message(m.chat.id, message_text)

def sendMarkdownMessage(cid, message_text):
    bot.send_message(cid, message_text, parse_mode="Markdown")


#Funciones de inicio y cierre del bot
@bot.message_handler(commands=['start'])
def start(m):
	cid = m.chat.id
	uid = m.from_user.id
	uname = m.from_user.first_name
	#Guardará información del usuario para enviarle datos posteriormente
	if not user.existe_user(cid):
		user.save_user(cid, uid, uname)
		send(m, "Hola, bienvenido a Marte")
		send(m, "A partir de ahora empezarás a recibir información sobre Marte, si quieres dejar de recibirla usa el comando /stop")
	else:
		send(m, "Ya estás inscrito")

@bot.message_handler(commands=['stop'])
def stop(m):
	cid = m.chat.id
	uid = m.from_user.id
	#Borra por completo los datos del usuario
	if user.existe_user(cid):
		user.delete_user(cid, uid)
		send(m, "Hasta la vista joven astronauta")
	else:
		send(m, "No te has inscrito todavia")

#Funcion que entra en el modo secreto
@bot.message_handler(commands=['secret'])
def secret(m):
	cid = m.chat.id
	uid = m.from_user.id
	uname = m.from_user.first_name

	#Otro posible comienzo para el reto que me libra de historia
	send(m, "Felicidades, has pasado la primera prueba")
	time.sleep(2)
	send(m, "Ahora ya sé que eres digno de aceptar mi reto")
	time.sleep(2)
	send(m, "Resuelve mis acertijos hasta llegar al final de la prueba")
	time.sleep(2)
	send(m, "Lo puedes intentar solo o acompañado")
	time.sleep(2)
	send(m, "Pero recuerda")
	time.sleep(2)
	send(m, "Solo los mejores llegarán al final")

	user.delete_user(cid, uid)
	#infl.save_infl(cid, uid)

'''
	#Pequeña secuencia de conexion (Posiblemente se cambie)
	send(m, "Entrando en el modo de desarrollo")
	send(m, "Esperando conexión")
	for i in range(3):
		time.sleep(1)
		send(m, "...")
	send(m, "Conexión establecida con servidor central")

	#Genera una id aleatoria para el usuario y la guarda 
	n = random.randint(1,700)
	user.save_id(cid, n)
	send(m, "ID: %i" %(n))
	user.delete_user(cid, uid)
	#infl.save_infl(cid, uid)

'''

bot.polling()
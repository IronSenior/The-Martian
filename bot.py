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
	#Guardará información del usuario para enviarle datos posteriormente
	user.save_user(cid, uid)
	send(m, "Hola, bienvenido a Marte")
	send(m, "A partir de ahora empezarás a recibir información sobre Marte, si quieres dejar de recibirla usa el comando /stop")

@bot.message_handler(commands=['stop'])
def stop(m):
	cid = m.chat.id
	uid = m.from_user.id
	#Borra por completo los datos del usuario
	user.delete_user(cid, uid)
	send(m, "Hasta la vista joven astronauta")

bot.polling()
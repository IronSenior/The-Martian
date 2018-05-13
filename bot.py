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

	#It saves user data to send the photos later on
	if not user.is_user(cid):
		user.save_user(cid, uid, uname)
		send(m, "Hello, welcome to the Martian")
		send(m, "The Marcian will send you pictures every day, if you don't want to recieve photos anymore use /stop")
	else:
		send(m, "You are already subscribed")

@bot.message_handler(commands=['stop'])
def stop(m):
	cid = m.chat.id
	uid = m.from_user.id

	#It deletes an user who doesn't want to recieve photos anymore
	if user.is_user(cid):
		user.delete_user(cid, uid)
		send(m, "See you later young astronaut")
		send(m, "If you want to recieve pictures again, use /start")
	else:
		send(m, "You have not subscribed yet")



bot.polling()
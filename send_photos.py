#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telebot
#from libs.keyboard import *
import private as tk
from libs import user_funcs
from libs import info_funcs as info
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


def send_info():
	users = user_funcs.get_users()
	photo = info.get_photo()

	for user in users:
		bot.send_message(user, "Una foto de Marte nueva cada día")
		bot.send_photo(user, photo)
	time.sleep(10)#(86400)
	send_info()

send_info()
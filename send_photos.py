#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telebot
#from libs.keyboard import *
import private as tk
from libs import user_funcs
from libs import info_funcs as info
import random
import requests 
import time
import json

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
	nasa_api = requests.get("https://api.nasa.gov/planetary/apod?api_key=mxDbxnbvRcDo3mrclKtKlUypkjdK65P80GJLmBQZ")
	nasa_info = json.loads(nasa_api.content)
	photo = nasa_info["url"]
	print (photo)


	for user in users:
		bot.send_message(user, "Una foto del espacio nueva cada día")
		bot.send_photo(user, photo)
	time.sleep(86400)
	send_info()

send_info()
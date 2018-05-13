#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telebot
from libs import private as tk
from libs import user_funcs as user
from libs import send_photos as photo
import random
import time

#TELEGRAM CONFIGURATION
token = tk.tk()
bot = telebot.TeleBot(token)


#Send_message simplified
def send(m, message_text):
    bot.send_message(m.chat.id, message_text)


#Start and stop commands
@bot.message_handler(commands=['start'])
def start(m):
	cid = m.chat.id
	uid = m.from_user.id
	uname = m.from_user.first_name

	#It saves user data to send the photos later on
	if not user.is_user(cid):
		user.save_user(cid, uid, uname)
		send(m, "Hello, welcome to the Martian")
		send(m, "The Martian will send you pictures every day, if you don't want to recieve photos anymore use /stop")
		photo.send_first_picture(cid)
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
		send(m, "You are not subscribed")



bot.polling()
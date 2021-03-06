#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telebot
import private as tk
import user_funcs
import requests 
import time
import json

#TELEGRAM CONFIGURATION
token = tk.tk()
bot = telebot.TeleBot(token)

#API CONFIGURATION
key = tk.key()
url = "https://api.nasa.gov/planetary/apod?api_key=%s"%(key)

def get_photo():
	#It uses the oficial api of "Astronomy Picture of the day"
	nasa_api = requests.get(url)
	nasa_info = json.loads(nasa_api.content)
	photo = nasa_info["url"]
	title = nasa_info["title"]
	explanation = nasa_info["explanation"]

	return photo, title, explanation

def send_info():
	users = user_funcs.get_users()

	photo, title, explanation = get_photo()

	#It sends all users the photo of the day
	for user in users:
		#bot.send_message(user, "Una foto del espacio nueva cada día")
		bot.send_photo(user, photo)
		bot.send_message(user, title)
		bot.send_message(user, explanation)
	time.sleep(86400)
	send_info()

def send_first_picture(cid):
	photo, title, explanation = get_photo()

	bot.send_photo(cid, photo)
	bot.send_message(cid, title)
	bot.send_message(cid, explanation)


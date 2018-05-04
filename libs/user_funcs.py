#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import shutil

db_path = "/home/pepe/Escritorio/Mis proyectos/Software/El_Marciano/DB/"

def save_user(cid, uid, uname):
	#Guarda a un usuario en la base de datos
	with open('%susers.json'%(db_path), 'r') as jsonfile:
		users = json.load(jsonfile)
		users["users"].append(cid)

	with open('%susers.json'%(db_path), 'w') as outfile:
		json.dump(users, outfile, indent=3)

	#Crea una carpeta para guardar información sobre el usuario
	path = db_path + str(cid)
	os.mkdir(path)

	with open('%s/basic_info.json'%(path), 'w') as outfile:
		data = {
			"uid": uid,
			"id": 0,
			"uname": uname
			}
		json.dump(data, outfile, indent=3)

def delete_user(cid, uid):
	#Borra a un usario de la base de datos para que no se le envie más información
	with open('%susers.json'%(db_path), 'r') as jsonfile:
		users = json.load(jsonfile)

		for user in users["users"]:
			if user == cid:
				users["users"].remove(cid)

	with open('%susers.json'%(db_path), 'w') as jsonfile:
		json.dump(users, jsonfile, indent=3)

def get_users():
	#Devuelve una lista con todos los usuarios inscritos
	with open('%susers.json'%(db_path), 'r') as jsonfile:
		users = json.load(jsonfile)

		return users["users"]

def existe_user(cid):
	#Devuelve True si el usuario está inscritos
	with open('%susers.json'%(db_path), 'r') as jsonfile:
		users = json.load(jsonfile)

		user_list = users["users"]

		if cid in user_list:
			return True

		return False

def save_id(cid, user_id):
	path = db_path + str(cid)
	with open('%s/basic_info.json'%(path), 'r') as jsonfile:
		info = json.load(jsonfile)

		info["id"] = user_id

	with open('%s/basic_info.json'%(path), 'w') as outfile:
		json.dump(info, outfile, indent=3)



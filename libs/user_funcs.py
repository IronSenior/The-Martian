#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import shutil

db_path = "/home/pepe/Escritorio/Mis proyectos/Software/Marciano/DB/"

def save_user(cid, uid):
	#Guarda a un usuario en la base de datos
	with open('%susers.json'%(db_path), 'r') as jsonfile:
		users = json.load(jsonfile)
		users["users"].append(cid)

	with open('%susers.json'%(db_path), 'w') as jsonfile:
		json.dump(users, jsonfile, indent=3)

	#Crea una carpeta para guardar información sobre el usuario
	path = db_path + str(cid)
	os.mkdir(path)



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
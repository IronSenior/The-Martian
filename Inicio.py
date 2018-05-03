#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json

db_path = "/home/pepe/Escritorio/Mis proyectos/Software/Marciano/DB/"

def inicio_bot():
	os.mkdir("DB")

	with open('./DB/users.json', 'w') as outfile:
		data = {"users": []}
		json.dump(data, outfile)

	print "Carpeta y archivo de inicio creados"

inicio_bot()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import shutil

db_path = "/home/pepe/Escritorio/Mis proyectos/Software/Marciano/DB/"

def save_user(cid, uid):
	with open('%susers.json'%(db_path), 'r') as jsonfile:
		users = json.load(jsonfile)
		users["users"].append(cid)

	with open('%susers.json'%(db_path), 'w') as jsonfile:
		json.dump(users, jsonfile, indent=3)


def delete_user(cid, uid):
	with open('%susers.json'%(db_path), 'r') as jsonfile:
		users = json.load(jsonfile)

		for user in users["users"]:
			if user == cid:
				users["users"].remove(cid)

	with open('%susers.json'%(db_path), 'w') as jsonfile:
		json.dump(users, jsonfile, indent=3)
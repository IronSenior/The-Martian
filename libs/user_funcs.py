#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os

#DB CONFIGURATION
db_path = "" 

def save_user(cid, uid, uname):
	#It saves the user id in order to send the photos later on
	with open('%susers.json'%(db_path), 'r') as jsonfile:
		users = json.load(jsonfile)
		users["users"].append(cid)

	with open('%susers.json'%(db_path), 'w') as outfile:
		json.dump(users, outfile, indent=3)

'''
	#It creates a new directory in order to save more user data in the furture
	path = db_path + str(cid)
	os.mkdir(path)

	with open('%s/basic_info.json'%(path), 'w') as outfile:
		data = {
			"uid": uid,
			"id": 0,
			"uname": uname
			}
		json.dump(data, outfile, indent=3)
'''

def delete_user(cid, uid):
	#It deletes an user from the DB
	with open('%susers.json'%(db_path), 'r') as jsonfile:
		users = json.load(jsonfile)

		for user in users["users"]:
			if user == cid:
				users["users"].remove(cid)

	with open('%susers.json'%(db_path), 'w') as jsonfile:
		json.dump(users, jsonfile, indent=3)

def get_users():
	#It returns all users' id
	with open('%susers.json'%(db_path), 'r') as jsonfile:
		users = json.load(jsonfile)

		return users["users"]

def is_user(cid):
	#It returns True if an user is subscribed
	with open('%susers.json'%(db_path), 'r') as jsonfile:
		users = json.load(jsonfile)

		user_list = users["users"]

		if cid in user_list:
			return True

		return False

'''
def save_id(cid, user_id):
	path = db_path + str(cid)
	with open('%s/basic_info.json'%(path), 'r') as jsonfile:
		info = json.load(jsonfile)

		info["id"] = user_id

	with open('%s/basic_info.json'%(path), 'w') as outfile:
		json.dump(info, outfile, indent=3)
'''


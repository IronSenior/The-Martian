#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json


def create_bot():
	os.mkdir("DB")

	with open('./DB/users.json', 'w') as outfile:
		data = {"users": []}
		json.dump(data, outfile)

	print "Directory and file created"

create_bot()

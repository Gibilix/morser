#!/usr/bin/env python3

from random import randint
from partition import partition

dct = {
	".-":"A", "-...":"B", "-.-.":"C", "-..":"D", ".":"E", "..-.":"F", "--.":"G", "....":"H", "..":"I", ".---":"J", "-.-":"K", ".-..":"L", "--":"M", "-.":"N", "---":"O", ".--.":"P", "--.-":"Q", ".-.":"R", "...":"S", "-":"T", "..-":"U", "...-":"V", ".--":"W", "-..-":"X", "-.--":"Y", "--..":"Z"
}

def morsed(x):
	result = ""
	lst = x.split(" ")
	for y in lst:
		if y.strip() in dct:
			result += dct[y.strip()]
		elif y.strip() == "/":
			result += " "
	return result

inpt = input("")
if morsed(inpt) != "":
	print(morsed(inpt))
else:
	log = []
	try:
		while len(log) < len(partition(2 * (len(inpt)-1)-1)):
			randnum = randint(1, len(inpt))
			munip = list(inpt)
			for i in range(randnum):
				randchoice = randint(1, len(munip)-1)
				if munip[randchoice] != " ":
					munip.insert(randchoice, " ")
			munip = ''.join(munip)
			if morsed(munip) not in log and morsed(munip) != "":
				log.append(morsed(munip))
				print(morsed(munip))
	except KeyboardInterrupt:
		print("\n")
		exit()


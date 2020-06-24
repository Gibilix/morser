#!/usr/bin/env python3

from random import randint # figured it would be easier to randomly generate spaces between dits and dahs for a while rather than litteratly trying to try every single combination. Though I could imagine uneccary random generations taking up run-time.
from partition import partition

dct = {
	".-":"A", "-...":"B", "-.-.":"C", "-..":"D", ".":"E", "..-.":"F", "--.":"G", "....":"H", "..":"I", ".---":"J", "-.-":"K", ".-..":"L", "--":"M", "-.":"N", "---":"O", ".--.":"P", "--.-":"Q", ".-.":"R", "...":"S", "-":"T", "..-":"U", "...-":"V", ".--":"W", "-..-":"X", "-.--":"Y", "--..":"Z"
}

# function for morse-code with spaces (and slashes for words)
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
		# while loop until all possible combinations are created. I sort of guessed at the way to calculate the total number from noticing a pattern similar to that of partitions so if anyone knows how to find the true total please edit.
		while len(log) < len(partition(2 * (len(inpt)-1)-1)):
			# creates a random number of blank inserts
			randnum = randint(1, len(inpt))
			# "munip" is short for "munipulate" or "manipulatable"
			munip = list(inpt)
			# for loop inserts a random number randnum times. 'morsed' takes care of the rest.
			for i in range(randnum):
				randchoice = randint(1, len(munip)-1)
				munip.insert(randchoice, " ")
			munip = ''.join(munip)
			if morsed(munip) not in log and morsed(munip) != "":
				log.append(morsed(munip))
				print(morsed(munip))
	except KeyboardInterrupt:
		print("\n")
		exit()


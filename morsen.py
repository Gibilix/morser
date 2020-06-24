#!/usr/bin/env python3

dct = {
	"A":".-", "B":"...", "C":"-.-.", "D":"-..", "E":".", "F":"..-.", "G":"--.", "H":"....", "I":"..", "J":".---", "K":"-.-", "L":".-..", "M":"--", "N":"-.", "O":"---", "P":".--.", "Q":"--.-", "R":".-.", "S":"...", "T":"-", "U":"..-", "V":"...-", "W":".--", "X":"-..-", "Y":"-.--", "Z":"--..", " ":"/"
}

def morsen(x):
	result = ""
	for y in x:
		if y.upper() in dct:
			result += dct[y.upper()] + " "
	return result


inpt = input("")
print(morsen(inpt))


#!/bin/bash

case $1 in
-d)
	echo $2 | morsed.py
	;;
-e)
	echo $2 | morsen.py
	;;
*)
	echo "Usage: morse [OPTION]... PATTERN"
	;;
esac

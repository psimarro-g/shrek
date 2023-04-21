import time
import pyautogui
import sys

def SendScript(filename: str):
	time.sleep(4) # este numero es el tiempo en segundos que tienes para hacer click en el chat que quieras petar, si eres lento de cojones pon mas tiempo
	with open(filename) as f:
		lines = f.readlines()
	n = 0
	for line in lines:
		if line.strip() != "":
			for word in line.split():
				pyautogui.typewrite(word)
				pyautogui.press('enter')
				n += 1
		"""
		codigo opcional para parar de escribir 
		mas o menos cuando el numero de palabras sea mayor 
		que el n especificado en el if statement (digo mas o menos porq hace la comprobacion cada linea no cada palabra para que vaya mas rapido)
		"""
		if n >= 200: # puedes cambiar el valor de n aqui
			re = input('continue y/n: ')
			if re == 'y':
				n = 0
				time.sleep(4)#este numero cambialo tambien si quieres mas tiempo 
			else:
				sys.exit()

SendScript("script.txt") # aqui puedes cambiar el texto para spamear, pero tiene que estar guardado en la misma carpeta que este codigo.
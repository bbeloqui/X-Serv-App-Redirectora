#!/usr/bin/python
# -*- coding: utf-8 -
import webapp  #para no tener que hacer socket
import random
class aleatorioServidor(webapp.webApp):
	def process(self, parsedRequest):
		return ("307 Temporary Redirect" + "\n" 
						+ "Location: http://localhost:1234/" 
						+ str(random.randrange(999999)), "")

if __name__ == "__main__":
	servaleat = aleatorioServidor("localhost", 1234)

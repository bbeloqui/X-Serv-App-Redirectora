
#!/usr/bin/python
# -*- coding: utf-8 -*-

import webapp
import random

class aleatApp(webapp.webApp):


    def process(self, parsedRequest):
        num = random.randint(0,9999999)
        return ("301 Moved Permanently", "<html><head><body><meta> "
                + "url=http://" +"localhost" + ":1234/ " + str(num)
                + "</body></html>"
                + "<h1><body><html>"
                +"<a href='" + str(num)
				+ "'>Dame otra</a>" + "</html></body></h1>")

if __name__ == "__main__":

	testWebApp = aleatApp('localhost', 1234)

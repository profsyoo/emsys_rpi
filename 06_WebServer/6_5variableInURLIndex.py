#dht11 import & use it
from flask import Flask

import dht11_lgpio as dht11

app = Flask(__name__)

body_html = """
    <h1>How to use</h1>
    <a href = "http://192.168.137.84:8080/str">http://192.168.137.84:8080/str</a>: you can use any 'str'<br>
    <a href = "http://192.168.137.84:8080/temp">http://192.168.137.84:8080/temp</a>: Temperature?<br>
    <a href = "http://192.168.137.84:8080/humid">http://192.168.137.84:8080/humid</a>: Humidity?<br>
    """

@app.route('/')
def root_url():
	return """<html>
    <head><title>Intro to my Raspberry Pi</title></head>
    <body>
    """ + body_html + """
    </body>
    </html>
    """


@app.route('/<name>/')
def hello(name):
	if name == 'kitae':
		rstr = "<h2>Hello, Kitae!!!!!</h2>"
	elif name == 'jmlee':
		rstr = "<h2>Hello, Jmlee!!!!!</h2>"
	elif name == 'temp':
		humidity, temperature = dht11.read(dht11.handle)
		rstr = "<h2>Temperature is '"+str(temperature)+"°C'</h2>"
	elif name == 'humid':
		humidity, temperature = dht11.read(dht11.handle)
		rstr = "<h2>Humidity is '"+str(humidity)+"%'</h2>"
	else:
		rstr = "<h2>Your Input String is '"+name+"'</h2>" # 'name'변수값
	return rstr+body_html

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)
	print("Ending")
	dht11.close()

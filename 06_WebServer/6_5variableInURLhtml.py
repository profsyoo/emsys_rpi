from flask import Flask

app = Flask(__name__)


@app.route('/')
def root_url():
	return """
    <html>
    <head><title>Intro to my Raspberry Pi</title></head>
    <body>
    <h1>How to use</h1>
    <a href = "http://192.168.137.84:8080/str">http://192.168.137.84:8080/str</a>: you can use any 'str'<br>
    <a href = "http://192.168.137.84:8080/temp">http://192.168.137.84:8080/temp</a>: Temperature?<br>
    <a href = "http://192.168.137.84:8080/temp">http://192.168.137.84:8080/humid</a>: Humidity?<br>
    </body>
    </html>

    """

@app.route('/<name>/')
def hello(name):
	if name == 'kitae':
		str = "<h2>Hello, Kitae!!!!!</h2>"
	elif name == 'jmlee':
		str = "<h2>Hello, Jmlee!!!!!</h2>"
	else:
		str = "<h2>Your Input String is '"+name+"'</h2>" # 'name'변수값
	return str

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)
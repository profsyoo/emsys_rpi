from flask import Flask
#
#default directory for the static contents.: ./static
#http://IP:8080/static/image.jpg 
#ex)    http://192.168.137.200:8080/static/image.jpg
#

app = Flask(__name__)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)

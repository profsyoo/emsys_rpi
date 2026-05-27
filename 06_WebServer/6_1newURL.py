from flask import Flask

app = Flask(__name__)

#new url: http://192.168.137.200/hello/
@app.route('/hello/')
def hello( ):
	return """
		<!DOCTYPE html>
		<html>
			<body>
				<h2>Hello, Raspberry Pi</h2>
			</body>
		</html>
		"""

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)

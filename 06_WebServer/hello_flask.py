from flask import Flask

app = Flask(__name__) # Flask 객체 생성

@app.route('/') # 다음 2라인이 라우팅 테이블에 ['/':home]를 저장하도록 함 
def home(): 
	return '<h2>Hello, Flask</h2>'

if __name__ == '__main__':	# 이 프로그램이 독립적으로 실행되는 경우
	app.run(host='0.0.0.0', port=8080, debug=True) # app.run() 함수 실행

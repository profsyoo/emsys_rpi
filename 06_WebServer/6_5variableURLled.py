import time
import lgpio

from flask import Flask


# Configuration
LED = 6
chip = lgpio.gpiochip_open(0)

# Claim the GPIO pin for output
lgpio.gpio_claim_output(chip, LED)


app = Flask(__name__)

@app.route('/<name>/')
def hello(name):
        
	str = "<h2>Your Input String is '"+name+"'</h2>" 
	if name == 'on':
		str = str + "<br><h2>You're trying turning on the LED</h2>"
		lgpio.gpio_write(chip, LED, 1)
	elif name == 'off':
		str = str + "<br><h2>You're trying turning off the LED</h2>"
		lgpio.gpio_write(chip, LED, 0)
	else:
		str = str + "<br><h2>Undefined command: "+name+"</h2>"

	
	return str

if __name__ == '__main__':
	print("Before")
#	app.run(host='0.0.0.0', port=8080, debug=True)
	app.run(host='0.0.0.0', port=8080, debug=False)

	print("Ending")

	print("\nProgram stopped by user")
	lgpio.gpio_write(chip, LED, 0)
	lgpio.gpiochip_close(chip)


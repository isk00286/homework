import RPi.GPIO as GPIO
import time

def led_dark(val):
	global bright_value
	global pwm_led
	if(bright_value > 0):
		bright_value -= 10
	pwm_led.ChangeDutyCycle(bright_value)
	print(val+str(bright_value))

def led_bright(val):
	global bright_value
	global pwm_led
	if(bright_value < 100):
		bright_value += 10
	pwm_led.ChangeDutyCycle(bright_value)
	print(val+str(bright_value))

global bright_value
global pwm_led
bright_value = 0
led_pin = 18
up_btn = 20
down_btn = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(up_btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(down_btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led_pin, GPIO.OUT)
pwm_led = GPIO.PWM(led_pin, 500)
pwm_led.start(0)

GPIO.add_event_detect(up_btn, GPIO.FALLING, callback=lambda x: led_bright("up"), bouncetime=300)
GPIO.add_event_detect(down_btn, GPIO.FALLING, callback=lambda x: led_dark("down"), bouncetime=300)

try:
	while True:
		#GPIO.wait_for_edge(20, GPIO.RISING)
		#GPIO.wait_for_edge(21, GPIO.RISING)
		time.sleep(10)
	
except KeyboardInterrupt:
	GPIO.cleanup()
GPIO.cleanup()

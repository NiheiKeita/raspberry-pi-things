# PWM テスト
# LEDをだんだん明るく、だんだん暗くする

# machineライブラリからPinに加えてPWMもインポート
from machine import Pin, PWM
import utime

# 使用するのはGP0 = PWM0 A ピン
pwm_led = PWM(Pin(0))
pwm_led.freq(1000)	# 1秒間に発生させるパルスの数

# 3回繰り返す
for i in range(3):
    # 0から65535まで、変数duty1を1ずつ大きくする
    for duty1 in range(65536):
        # 0から65535までの整数値をduty_u16()に渡す
        # だんだん明るくなる
        pwm_led.duty_u16(duty1)
        #utime.sleep(0.0001)
    # 65535から0まで、変数duty2を1ずつ小さくする
    for duty2 in range(65535,-1,-1):
        # だんだん暗くなる
        pwm_led.duty_u16(duty2)
        #utime.sleep(0.0001)
        
print("終わり")   
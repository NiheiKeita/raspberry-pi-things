#timeモジュールをインポート
import time

#RPi.GPIOモジュールをインポート
import RPi.GPIO as GPIO

# BCM(GPIO番号)で指定する設定
GPIO.setmode(GPIO.BCM)

# GPIO17/18を出力モード設定
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

sleepTime = 0.1

while True:
  # GPIO17の出力を1にして、LED点灯
  GPIO.output(17, 1)
  GPIO.output(18, 0)
  GPIO.output(25, 0)

  # 0.5秒待つ
  time.sleep(sleepTime)

  # GPIO17の出力を0にして、LED消灯
  GPIO.output(17, 0)
  GPIO.output(18, 1)
  GPIO.output(25, 0)

  # 0.5秒待つ
  time.sleep(sleepTime)
  # GPIO17の出力を0にして、LED消灯
  GPIO.output(17, 0)
  GPIO.output(18, 0)
  GPIO.output(25, 1)

  # 0.5秒待つ
  time.sleep(sleepTime)
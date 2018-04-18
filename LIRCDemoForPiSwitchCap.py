'''
Copyright [2018] [Nanomesher Limited - www.nanomesher.com]

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
'''


import lirc
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(12, GPIO.OUT)



toggle1 = False
toggle2 = False
GPIO.output(12,GPIO.LOW)

while True:
  sockid = lirc.init("myprogram")
  code=lirc.nextcode()
  
  
  if(len(code)>0 and code[0]=="LED1"):
	print("button 1 detected")
	if(toggle1 == False):
		GPIO.output(12,GPIO.HIGH)
		toggle1 = True
	elif(toggle1 == True):
		GPIO.output(12,GPIO.HIGH)
		toggle1 = False

  if(len(code)>0 and code[0]=="LED2"):
	print("button 2 detected")
    if(toggle2 == False):
        GPIO.output(12,GPIO.LOW)
        toggle2 = True
    elif(toggle2 == True):
        GPIO.output(12,GPIO.LOW)
        toggle2 = False


	
	


lirc.deinit()

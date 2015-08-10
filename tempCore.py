##
##  filename: demoCore.py
##

import os
import serial
import re
import datetime
from nanpy import Arduino
from nanpy import serial_manager
serial_manager.connect('/dev/ttyACM0')
from time import sleep
import time
import json

analogPort = 0
powervoltage = 5.

CURRENTDIR = os.path.dirname(__file__)
BASEDIR    = os.path.dirname(CURRENTDIR)

last_received = ''

class TempCore():

    def index(self,request):

        json = 0
        data = 0    
            
        if request.args.get('json', '') == "1":
            json = 1
            ser = Arduino()
            data = self.receiving(ser)
            sensorValue = Arduino.analogRead(analogPort)
            data= (sensorValue/1023.)*powervoltage*100
            print "data = ", data
        html = self.showDemoHTML(data,json)
        return html

    def receiving(self, ser):
	print "..recieving...."
        global last_received
#        data = 0.0
        
#        buffer = ''
#         while True:
        sensorValue = Arduino.analogRead(analogPort)
        data= (sensorValue/1023.)*powervoltage*100
#            buffer = buffer + ser.analogRead(analogPort)
#            data = temp_demo
#            if '\r\n' in buffer:
#               print ('Alas...')              
        print ("temperature=",data)
        return data
        
        
    def showDemoHTML(self,data,json):
        ## reads an html file and does things with it
        ## there are better ways, but they are more complicated
        print "....showDemoHTML...."
        while True:
          sensorValue = Arduino.analogRead(analogPort)

          data= (sensorValue/1023.)*powervoltage*100

          if json == 1:
            f = open(CURRENTDIR +"/json.html")
            html = f.read()           
            html = html.replace("%Temperature%",str(data))
            print html            
            return html        

          else:
            f = open(CURRENTDIR +"/temp.html")
            html = f.read()
	    html = html.replace("%Temperature%",str(data))
            print ".....demo....", data 
            return html

if __name__ == "__main__":
    print "Hello World";

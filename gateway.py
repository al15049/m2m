mport serial
import requests

ser = serial.Serial('/dev/ttyUSB0',9600,timeout=None)
url =  "http://160.16.210.86:16049"

while True:
  line = ser.readline()
  lux = line.strip().decode('utf-8')
  requests.get(url + "?lux=" + lux);
ser.close()


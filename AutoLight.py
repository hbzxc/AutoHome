import os
import requests
import time

while 0==0:

  from datetime import datetime

  now = datetime.now()

  current_time = now.strftime("%H:%M:S")

  hostname = "Target machine ip"
  response = os.system("ping -c 3 " + hostname)

  try:
    headers = {
      'Accept': 'application/json',
    }

    getState = requests.get('http://192.168.1.110:8080/rest/items/AlexaGuardonFirstplug_PowerState', headers=headers)

    if response == 0 and (current_time > '17:50:00' or current_time < '05:00:00') and getState.json()["state"] == 'OFF' :
      try:
        headers = {
          'Content-Type': 'text/plain',
          'Accept': 'application/json',
        }

        data = 'ON'

        setState = requests.post('http://192.168.1.110:8080/rest/items/AlexaGuardonFirstplug_PowerState', headers=headers, data=data)
      except:
        print("not connected yet")
    elif getState.json()["state"] == 'ON' and response != 0:
        time.sleep(240)
        try:
          headers = {
            'Content-Type': 'text/plain',
            'Accept': 'application/json',
          }

          data = 'OFF'

          setState = requests.post('http://192.168.1.110:8080/rest/items/AlexaGuardonFirstplug_PowerState', headers=headers, data=data)
        except:
          print("not connected yet")
    else:
      print("Holding State")
  except:
    print("openhab not running")
  time.sleep(5)


import requests
from gpiozero import LED
from time import sleep
import threading

URL = "http://132.148.146.12/RestApiOOps/token"
PAYLOAD = "grant_type=password&UserName=&Password="
HEADERS = {'content-type': "application/x-www-form-urlencoded"}

URL_PUERTA = "http://132.148.146.12/RestApiOOps/api/Taquilla/PuertasAbiertas"
MAC = {"mac": "B8:27:EB:74:57:F8"}
pin_door = LED(17)


def toggleDoor(status):
    print('TOGGLE DOOR !!! ')
    if status:
        pin_door.on()
        sleep(2)


def getToken():
    print ('Get Token !')
    r = requests.request("POST", URL, data=PAYLOAD, headers=HEADERS)
    response = r.json()
    if response:
        token = response['access_token']
        return token


def getStatusDoor():
    print('GET STATUS DOOR ! ')
    token = getToken()
    headers_puerta = {'Content-Type': 'application/json',
                      'Authorization': 'Bearer {}'.format(token)}
    r = requests.request(
        "POST", URL_PUERTA, headers=headers_puerta, params=MAC)

    response = r.json()

    if response:
        status_door = response['RspetaTaquillaPuertas']['ListaPines'][1]
        return status_door


def pollStatusDoor():
    while True:
        status_door = getStatusDoor()
        print ('Estados puerta: ', status_door['PuertaAbierta'])

        if status_door['PuertaAbierta']:
            print('Open Door')
            pin_door.on()
        if not status_door['PuertaAbierta']:
            print('Close Door')
            pin_door.off()
        
        sleep(5)

print('START !!! ')

pollStatusDoor()

# t = threading.Thread(target=pollStatusDoor)
# t.start()


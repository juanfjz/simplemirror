#!/usr/bin/env python3
from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import signal
import sys
import RPi.GPIO as GPIO
import xml.etree.ElementTree as ET
from io import open
import re
import subprocess
from threading import Timer

GPIO.setmode(GPIO.BCM)
BUTTON1 = 22
BUTTON2 = 24
BUTTON3 = 16
GPIO.setup(BUTTON1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
estadomonitor = 'encendido'

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
conjunto = [""]
eventop = [""]

cuenta = 0
numeronot = ''
latitudf = [""]
longitudf = [""]
keyf = [""]
titulotiemf = [""]
rssf = [""]
logof = [""]
fondof = [""]
colorf = [""]
t = ''

class repetirtimer(object):
    def __init__(self, interval, function, args=[], kwargs={}):
        self._interval = interval
        self._function = function
        self._args = args
        self._kwargs = kwargs
    def start(self):
        global t
        t = Timer(self._interval, self._function, *self._args, **self._kwargs)
        t.start()
        
    def cancel(self):
        global t
        t.cancel()

def lucesfuera():
    global estadomonitor
    if estadomonitor == 'encendido':
         subprocess.call (['vcgencmd', 'display_power', '0'])
         estadomonitor = 'apagado'
         GPIO.output(35, False)
         GPIO.output(31, False)

energia = repetirtimer(300,lucesfuera,())

def listToString(aaa):  
    str1 = "" 
    return (str1.join(aaa)) 

def replace_line(file_name, cualquitas, text):
    lines = open(file_name, errors='ignore').readlines()
    cualquitas2 = cualquitas - 1
    antes = lines[:cualquitas2]
    antes[-1] = antes[-1].strip()
    antes2 = listToString(antes)
    despues = lines[cualquitas:]
    despues2 = listToString(despues)
    completo = antes2 + '\n' + text + '\n' + despues2
    out = open(file_name, 'w')
    out.writelines(completo)
    out.close()

def replace_color(file_name2, colornuev):
    linescolor = open(file_name2, 'r').readlines()
    reemplazado = [re.sub('\([^\)]*\)', colornuev, lineass) for lineass in linescolor]
    outcolor = open(file_name2, 'w')
    outcolor.writelines(reemplazado)
    outcolor.close()


def contador():
  global cuenta
  global numeronot
  cuenta+=1
  if cuenta > numeronot:
    cuenta = 1

def leervariables():  
    tree = ET.parse('variables.xml')
    root = tree.getroot()

    global latitudf
    global longitudf
    global keyf
    global titulotiemf   
    global rssf
    global logof
    global fondof
    global colorf
    global numeronot
    
    for latitud in root.iter('latitud'):
        latitudf.append(latitud.text)
    
    for longitud in root.iter('longitud'):
        longitudf.append(longitud.text)

    for apikey in root.iter('apikey'):
        keyf.append(apikey.text)
     
    for titulotiem in root.iter('titulotiem'):
        titulotiemf.append(titulotiem.text)        
    
    for url in root.iter('url'):
        rssf.append(url.text)
        
    for logo in root.iter('logo'):
        logof.append(logo.text)

    for fondo in root.iter('fondo'):
        fondof.append(fondo.text)
        
    for color in root.iter('color'):
        colorf.append(color.text)
    
    numeronot = len(rssf) - 1  

def usarvariables():  
    global cuenta
    global numeronot
    latitudfinal = 'var lat = ' + latitudf[1] + ';'
    longitudfinal = 'var lon = ' + longitudf[1] + ';'
    keyfinal = 'var key = "' + keyf[1] + '";'
    titulotiemfinal = '    <div id="titulo">' + titulotiemf[1] +'</div>'
    contador()
    rssfinal = rssf[cuenta]
    logofinal = logof[cuenta]   
    fondofinal = '--fondod: url("../archivos/fondos/' + fondof[cuenta] + '");'
    colorfinal = colorf[cuenta] + ','
    colorfinall = '(' + colorfinal + '1)'
    colorpri = '--colorpri: rgba(' + colorfinal + '1);'
    colorsec = '--colorsec: rgba(' + colorfinal + '1);'
    resplandor = '--resplandorentrada: 0px 0px 10px rgba(' + colorfinal + '0.8);'
    sombraesp3 = '--sombraesp3: inset 0px 0px 15px 5px rgba(200,200,200,0.8), inset 0px 0px 15px 5px rgba(' + colorfinal + '0.3);'
    sombra = '--fc-today-bg-color: rgba(' + colorfinal + '0.4);'
    colornoti = '--temahora: rgba(' + colorfinal + '1);'
       
    replace_color('archivos/iconostiempo/01d.svg', colorfinall)
    replace_color('archivos/iconostiempo/01n.svg', colorfinall)
    replace_color('archivos/iconostiempo/02d.svg', colorfinall)
    replace_color('archivos/iconostiempo/02n.svg', colorfinall)
    replace_color('archivos/iconostiempo/03.svg', colorfinall)
    replace_color('archivos/iconostiempo/04.svg', colorfinall)
    replace_color('archivos/iconostiempo/09.svg', colorfinall)
    replace_color('archivos/iconostiempo/10d.svg', colorfinall)
    replace_color('archivos/iconostiempo/10n.svg', colorfinall)
    replace_color('archivos/iconostiempo/11.svg', colorfinall)
    replace_color('archivos/iconostiempo/13.svg', colorfinall)
    replace_color('archivos/iconostiempo/50.svg', colorfinall)
    replace_color('archivos/iconostiempo/bottom.svg', colorfinall)
    replace_color('archivos/iconostiempo/clouds.svg', colorfinall)
    replace_color('archivos/iconostiempo/dawn.svg', colorfinall)      
    replace_color('archivos/iconostiempo/drop.svg', colorfinall)
    replace_color('archivos/iconostiempo/rain.svg', colorfinall)
    replace_color('archivos/iconostiempo/sunset.svg', colorfinall)
    replace_color('archivos/iconostiempo/termometro.svg', colorfinall)
    replace_color('archivos/iconostiempo/top.svg', colorfinall)
    replace_color('archivos/iconostiempo/uv.svg', colorfinall)
    replace_color('archivos/iconostiempo/wind.svg', colorfinall)    

    replace_line('css/principal.css', 19, colorpri)
    replace_line('css/principal.css', 20, colorsec)
    replace_line('css/principal.css', 27, resplandor)
    replace_line('css/principal.css', 33, sombraesp3)              
    replace_line('css/principal.css', 35, fondofinal)
    replace_line('css/calendario.css', 32, sombra)
    replace_line('calendario/evento.html', 13, colorsec)            
    replace_line('scripts/tiempo.js', 2, latitudfinal) 
    replace_line('scripts/tiempo.js', 3, longitudfinal)
    replace_line('scripts/tiempo.js', 4, keyfinal)
    replace_line('noticias/loading.html', 5, colorsec)          
    replace_line('noticias/noticias.html', 13, colornoti)
    replace_line('tiempo/tiempo.html', 22, titulotiemfinal)
    subprocess.call (['xdotool', 'key', 'F7'])
    actualizanoticias(rssfinal, logofinal)

def actualizanoticias(rssfinal, logofinal):          
    subprocess.call (['curl', '-k', rssfinal, '-o', 'noticias/noticias.xml'])
    
    tree2 = ET.parse('noticias/noticias.xml')
    root2 = tree2.getroot()

    titulo = [""]
    descripcion = [""]
    fecha = [""]

    for item in root2.findall('./channel/item'):
        for title in item.findall('title'): 
            titulo.append(title.text)
    
        for description in item.findall('description'):
            descripcion.append(description.text)
    
        for pubDate in item.findall('pubDate'):
            fecha.append(pubDate.text)

    imagen = '<img width="100%" height="100%" src="../archivos/iconos/' + logofinal + '" style="border: solid 1px var(--temahora); box-shadow: var(--sombra); opacity: 0.85; border-radius: 3px;"></img>';

    cuenta2 = 1
    posimag = 235
    postit = 238
    posdes = 245
    posfec = 248

    while cuenta2 < 11:
        titulof = titulo[cuenta2]
        titulof = re.sub( r'<[^>]*>', '<>', titulof ).strip()
        titulof = re.sub( r'>', '', titulof ).strip()
        titulof = re.sub( r'<', '', titulof ).strip()
        titulof = titulof.replace("\r","")
        titulof = titulof.replace("\n","")
        longi1 = len(titulof)
        if longi1 > 150:
            titulof = titulof[0:147] + '...'

        descripcionf = descripcion[cuenta2]
        descripcionf = re.sub( r'<[^>]*>', '<>', descripcionf ).strip()
        descripcionf = re.sub( r'>', '', descripcionf ).strip()
        descripcionf = re.sub( r'<', '', descripcionf ).strip()
        descripcionf = descripcionf.replace("\r","")
        descripcionf = descripcionf.replace("\n","")
        descripcionf = descripcionf.replace('&gt;'," ")  #especial sensacine
        longi2 = len(descripcionf)
        if longi2 > 400:
            descripcionf = descripcionf[0:397] + '...'    
  
        fechaf = fecha[cuenta2]
        fechaf = re.sub( r'<[^>]*>', '<>', fechaf ).strip()
        fechaf = re.sub( r'>', '', fechaf ).strip()
        fechaf = re.sub( r'<', '', fechaf ).strip()
        fechaf = fechaf[0:16] + '.' + fechaf[16:25] + 'h.'
        fechaf = re.sub( r'Mon', 'Lunes', fechaf ).strip()
        fechaf = re.sub( r'Tue', 'Martes', fechaf ).strip()
        fechaf = re.sub( r'Wed', 'Miercoles', fechaf ).strip()
        fechaf = re.sub( r'Thu', 'Jueves', fechaf ).strip()
        fechaf = re.sub( r'Fri', 'Viernes', fechaf ).strip()
        fechaf = re.sub( r'Sat', 'Sabado', fechaf ).strip()
        fechaf = re.sub( r'Sun', 'Domingo', fechaf ).strip()
        fechaf = fechaf.replace("\r","")
        fechaf = fechaf.replace("\n","")

        replace_line('noticias/noticias.html', posimag, imagen) 
        replace_line('noticias/noticias.html', postit, titulof)
        replace_line('noticias/noticias.html', posdes, descripcionf)    
        replace_line('noticias/noticias.html', posfec, fechaf) 

        cuenta2+=1
        posimag = posimag + 23
        postit = postit + 23
        posdes = posdes + 23
        posfec = posfec + 23    
        
def actualizacal():
    creds = None
    # The file scripts/token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('scripts/token.pickle'):
        with open('scripts/token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'scripts/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('scripts/token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    
    global conjunto  
    
    for event in events:
        fecha = event['start'].get('dateTime', event['start'].get('date'))
        fecha = fecha[0:10]
        titulo = event['summary']
        texto = '{title: "' + titulo + '", start: "' + fecha + '"},'
        ano = fecha[0:4]
        dia = fecha[8:10]
        mesito = fecha[5:7]
        if mesito == '01':
            mes = 'Enero'
        if mesito == '02':
            mes = 'Febrero'
        if mesito == '03':
            mes = 'Marzo'
        if mesito == '04':
            mes = 'Abril'
        if mesito == '05':
            mes = 'Mayo'
        if mesito == '06':
            mes = 'Junio'
        if mesito == '07':
            mes = 'Julio'
        if mesito == '08':
            mes = 'Agosto'   
        if mesito == '09':
            mes = 'Septiembre'
        if mesito == '10':
            mes = 'Octubre'
        if mesito == '11':
            mes = 'Noviembre'
        if mesito == '12':
            mes = 'Diciembre'               
        fechaguay = dia + ' de ' + mes + ' de ' + ano
        texto2 = '<div id="eventin"><span id=orig>' + titulo + '<div id="separador"></div><span id=copia>' + titulo + '</span></span></div><div id="fechaeventin">' + fechaguay + '</div>'
        global eventop
        conjunto.append(texto)
        eventop.append(texto2)        
        
    conjunto2 = listToString(conjunto)
    evento1 = eventop[1]
    replace_line('calendario/calendario.html', 17, conjunto2)
    conjunto = [""]
    replace_line('calendario/evento.html', 62, evento1)
    

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

def boton1(channel):
    energia.cancel()
    leervariables()
    usarvariables()
    subprocess.call (['xdotool', 'key', 'F6'])
    energia.start()        
  
def boton2(channel):
    global estadomonitor
    if estadomonitor == 'encendido':
         subprocess.call (['vcgencmd', 'display_power', '0'])
         estadomonitor = 'apagado'
         energia.cancel()
    else:
         subprocess.call (['vcgencmd', 'display_power', '1'])
         estadomonitor = 'encendido'
         actualizacal()
         energia.start()

def boton3(channel):
    subprocess.call (['shutdown', '-h', 'now'])

if __name__ == '__main__':
    energia.start()
    actualizacal()
    GPIO.add_event_detect(BUTTON1, GPIO.FALLING, callback=boton1, bouncetime=300)
    GPIO.add_event_detect(BUTTON2, GPIO.FALLING, callback=boton2, bouncetime=300)
    GPIO.add_event_detect(BUTTON3, GPIO.FALLING, callback=boton3, bouncetime=300)    
    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()

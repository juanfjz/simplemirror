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
conjunto = []
eventop = []
eventop2 = []

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
    colorpri01 = '--colorpri01: rgba(' + colorfinal + '0.1);'
    colorpri06 = '--colorpri06: rgba(' + colorfinal + '0.6);'
    resplandor = '--resplandorentrada: 0px 0px 10px rgba(' + colorfinal + '0.8);'
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
    replace_color('archivos/iconosev/calendario.svg', colorfinall)  
    replace_color('archivos/iconosev/rel.svg', colorfinall)      

    replace_line('css/principal.css', 19, colorpri)
    replace_line('css/principal.css', 20, colorpri01)
    replace_line('css/principal.css', 23, resplandor)          
    replace_line('css/principal.css', 34, fondofinal)
    replace_line('css/calendario.css', 32, sombra)
    replace_line('calendario/eventos.html', 9, colorpri)
    replace_line('calendario/eventos.html', 10, colorpri01) 
    replace_line('calendario/eventos.html', 11, colorpri06)     
    replace_line('scripts/tiempo.js', 2, latitudfinal) 
    replace_line('scripts/tiempo.js', 3, longitudfinal)
    replace_line('scripts/tiempo.js', 4, keyfinal)
    replace_line('noticias/loading.html', 5, colorpri)          
    replace_line('noticias/noticias.html', 11, colornoti)
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
    replace_line('noticias/noticias.html', 248, imagen) 

    cuenta2 = 1
    postit = 252
    posdes = 287

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

        descripciontotal = descripcionf + '<p class="tiemp">' + fechaf + '</p>'

        replace_line('noticias/noticias.html', postit, titulof)
        replace_line('noticias/noticias.html', posdes, descripciontotal)    

        cuenta2+=1
        postit = postit + 3
        posdes = posdes + 3  
        
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
                                        maxResults=31, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    
    nohayeve = '--activa0evento: block;'
    nohayeve2 = '--activa00evento: none;'
    
    if not events:
        replace_line('calendario/eventos.html', 12, nohayeve)
        replace_line('calendario/eventos.html', 13, nohayeve2)
    
    global conjunto 
    global eventop
    global eventop2    
    contador3 = 1
    
    for event in events:
        fecha = event['start'].get('dateTime', event['start'].get('date'))
        fecha = fecha[0:10]
        titulo = event['summary']
        tituloge = titulo
        titulope = titulo
        longi = len(titulo)
        if longi > 50:
           tituloge = titulo[0:47] + '...'
        if longi > 30:
           titulope = titulo[0:27] + '...'
        texto = '{title: "' + titulope + '", start: "' + fecha + '"},'
        ano = fecha[0:4]
        dia = fecha[8:10]
        mesito = fecha[5:7]
        hora = fecha[11:16]
        if mesito == '01':
            mes = 'Ene'
        if mesito == '02':
            mes = 'Feb'
        if mesito == '03':
            mes = 'Mar'
        if mesito == '04':
            mes = 'Abr'
        if mesito == '05':
            mes = 'May'
        if mesito == '06':
            mes = 'Jun'
        if mesito == '07':
            mes = 'Jul'
        if mesito == '08':
            mes = 'Ago'   
        if mesito == '09':
            mes = 'Sep'
        if mesito == '10':
            mes = 'Oct'
        if mesito == '11':
            mes = 'Nov'
        if mesito == '12':
            mes = 'Dic'               
        ano2 = int(ano)
        mesito2 = int(mesito)
        dia2 = int(dia)
        ditt = datetime.date(ano2, mesito2, dia2)
        ditt2 = ditt.isocalendar()[2]
        if ditt2 == 1:
            diasem = 'Lunes'
        if ditt2 == 2:
            diasem = 'Martes'
        if ditt2 == 3:
            diasem = 'Miercoles'
        if ditt2 == 4:
            diasem = 'Jueves'
        if ditt2 == 5:
            diasem = 'Viernes'
        if ditt2 == 6:
            diasem = 'Sabado'
        if ditt2 == 7:
            diasem = 'Domingo'
            
        fechaguay = diasem + ', ' + dia + ' ' + mes + ' ' + ano + ' a las ' + hora + 'h.'
        if not hora:
            fechaguay = diasem + ', ' + dia + ' ' + mes + ' ' + ano + '.'
            
        texto2 = '<div class="texto11"><div class="centrado">' + tituloge + '</div></div>'
        texto3 = '<div class="texto22"><div class="centrado">' + fechaguay + '</div></div>'
        if contador3 == 1:
            texto2 = '<div class="texto1"><div class="centrado">' + tituloge + '</div></div>'
            texto3 = '<div class="texto2"><div class="centrado">' + fechaguay + '</div></div>'
        
        conjunto.append(texto)
        eventop.append(texto2)
        eventop2.append(texto3)
        contador3+=1        
    
    numeroeventos = len(eventop)

    imaeven1 = '<div class="imagen11"><div class="centrado"><img src="../archivos/iconosev/calendario.svg" width="30%" style="margin-left: 35%;"></div></div>'
    imaeven2 = '<div class="imagen22"><div class="centrado"><img src="../archivos/iconosev/rel.svg" width="30%" style="margin-left: 35%;"></div></div>'
    
    solo1eve1 = '--activa0evento: none;'
    solo1eve2 = '--activa00evento: block;'
    solo1eve3 = '--activa1evento: block;'
    solo1eve4 = '--activa11evento: none;'
 
    masdeuno1 = '--activa0evento: none;'
    masdeuno2 = '--activa00evento: block;'
    masdeuno3 = '--activa1evento: none;'
    masdeuno4 = '--activa11evento: block;'
 
    abiso = '<div class="aviso"><div class="centrado">No hay mas eventos que mostrar</div></div>'
    hueco = ' '

    doseves1 = '--opacidad2: 0.5;' 
    doseves2 = '--opacidad3: 0.3;' 
    doseves3 = '--opacidad4: 0.3;'

    treseves1 = '--opacidad2: 1;' 
    treseves2 = '--opacidad3: 0.5;' 
    treseves3 = '--opacidad4: 0.3;'

    cuatroeves1 = '--opacidad2: 1;' 
    cuatroeves2 = '--opacidad3: 1;' 
    cuatroeves3 = '--opacidad4: 0.5;'
 
    cincoeves1 = '--opacidad2: 1;' 
    cincoeves2 = '--opacidad3: 1;' 
    cincoeves3 = '--opacidad4: 1;'
 
    if numeroeventos > 0:
        evento1 = eventop[0]
        evento1f = eventop2[0]
        replace_line('calendario/eventos.html', 245, evento1)
        replace_line('calendario/eventos.html', 247, evento1f)
        replace_line('calendario/eventos.html', 12, solo1eve1)
        replace_line('calendario/eventos.html', 13, solo1eve2)        
        replace_line('calendario/eventos.html', 14, solo1eve3)
        replace_line('calendario/eventos.html', 15, solo1eve4)
    if numeroeventos > 1:
        evento2 = eventop[1]
        evento2f = eventop2[1]
        replace_line('calendario/eventos.html', 255, imaeven1)
        replace_line('calendario/eventos.html', 256, evento2)
        replace_line('calendario/eventos.html', 257, imaeven2)
        replace_line('calendario/eventos.html', 258, evento2f)
        replace_line('calendario/eventos.html', 12, masdeuno1)
        replace_line('calendario/eventos.html', 13, masdeuno2)        
        replace_line('calendario/eventos.html', 14, masdeuno3)
        replace_line('calendario/eventos.html', 15, masdeuno4)
        replace_line('calendario/eventos.html', 17, doseves1)
        replace_line('calendario/eventos.html', 18, doseves2)        
        replace_line('calendario/eventos.html', 19, doseves3)
        replace_line('calendario/eventos.html', 263, abiso)
        replace_line('calendario/eventos.html', 262, hueco)
        replace_line('calendario/eventos.html', 264, hueco)        
        replace_line('calendario/eventos.html', 265, hueco)
        replace_line('calendario/eventos.html', 270, hueco)
        replace_line('calendario/eventos.html', 269, hueco)
        replace_line('calendario/eventos.html', 271, hueco)        
        replace_line('calendario/eventos.html', 272, hueco) 
        replace_line('calendario/eventos.html', 278, hueco)
        replace_line('calendario/eventos.html', 277, hueco)
        replace_line('calendario/eventos.html', 279, hueco)        
        replace_line('calendario/eventos.html', 280, hueco) 
                        
    if numeroeventos > 2:
        evento3 = eventop[2]
        evento3f = eventop2[2]
        replace_line('calendario/eventos.html', 262, imaeven1)
        replace_line('calendario/eventos.html', 263, evento3)
        replace_line('calendario/eventos.html', 264, imaeven2)
        replace_line('calendario/eventos.html', 265, evento3f)       
        replace_line('calendario/eventos.html', 12, masdeuno1)
        replace_line('calendario/eventos.html', 13, masdeuno2)        
        replace_line('calendario/eventos.html', 14, masdeuno3)
        replace_line('calendario/eventos.html', 15, masdeuno4)  
        replace_line('calendario/eventos.html', 17, treseves1)
        replace_line('calendario/eventos.html', 18, treseves2)        
        replace_line('calendario/eventos.html', 19, treseves3)
        replace_line('calendario/eventos.html', 270, abiso)
        replace_line('calendario/eventos.html', 269, hueco)
        replace_line('calendario/eventos.html', 271, hueco)        
        replace_line('calendario/eventos.html', 272, hueco)
        replace_line('calendario/eventos.html', 278, hueco)
        replace_line('calendario/eventos.html', 277, hueco)
        replace_line('calendario/eventos.html', 279, hueco)        
        replace_line('calendario/eventos.html', 280, hueco) 
                 
    if numeroeventos > 3:
        evento4 = eventop[3]
        evento4f = eventop2[3]
        replace_line('calendario/eventos.html', 269, imaeven1)
        replace_line('calendario/eventos.html', 270, evento4)
        replace_line('calendario/eventos.html', 271, imaeven2)
        replace_line('calendario/eventos.html', 272, evento4f)
        replace_line('calendario/eventos.html', 12, masdeuno1)
        replace_line('calendario/eventos.html', 13, masdeuno2)        
        replace_line('calendario/eventos.html', 14, masdeuno3)
        replace_line('calendario/eventos.html', 15, masdeuno4)  
        replace_line('calendario/eventos.html', 17, cuatroeves1)
        replace_line('calendario/eventos.html', 18, cuatroeves2)        
        replace_line('calendario/eventos.html', 19, cuatroeves3)
        replace_line('calendario/eventos.html', 278, abiso)
        replace_line('calendario/eventos.html', 277, hueco)
        replace_line('calendario/eventos.html', 279, hueco)        
        replace_line('calendario/eventos.html', 280, hueco) 
    if numeroeventos > 4:
        evento5 = eventop[4]
        evento5f = eventop2[4]
        replace_line('calendario/eventos.html', 277, imaeven1)
        replace_line('calendario/eventos.html', 278, evento5)
        replace_line('calendario/eventos.html', 279, imaeven2)
        replace_line('calendario/eventos.html', 280, evento5f)
        replace_line('calendario/eventos.html', 12, masdeuno1)
        replace_line('calendario/eventos.html', 13, masdeuno2)        
        replace_line('calendario/eventos.html', 14, masdeuno3)
        replace_line('calendario/eventos.html', 15, masdeuno4)
        replace_line('calendario/eventos.html', 17, cincoeves1)
        replace_line('calendario/eventos.html', 18, cincoeves2)        
        replace_line('calendario/eventos.html', 19, cincoeves3)        
        
    conjunto2 = listToString(conjunto)
    replace_line('calendario/calendario.html', 18, conjunto2)
    conjunto = []
    contador3 = 1
    

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
    leervariables()
    usarvariables()
    actualizacal()
    energia.start()
    GPIO.add_event_detect(BUTTON1, GPIO.FALLING, callback=boton1, bouncetime=300)
    GPIO.add_event_detect(BUTTON2, GPIO.FALLING, callback=boton2, bouncetime=300)
    GPIO.add_event_detect(BUTTON3, GPIO.FALLING, callback=boton3, bouncetime=300)    
    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()

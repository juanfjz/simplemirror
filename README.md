# simplemirror
Smart Mirror for raspberry Pi written in Python




  1. Instalación del software:

1.1. Configuracion del archivo "variables.xml".
-En este archivo configuramos la sección del tiempo, las noticias y el tema del programa:

-En primer lugar debemos crear una cuenta en openwheathermap (https://openweathermap.org/) y obtener una API KEY gratuita que deberemos introducir en el archivos de configuracion.

-Además, debemos completar los campos que piden la latitud y longitud geográficas, así como el nombre de la ciudad para la que deseemos consultar el tiempo. Podemos obtener estos datos en https://openweathermap.org/find. 

-Las distintas fuentes RSS que deseemos mostrar en el apartado de noticias junto con el fondo de pantalla, los iconos y el color de enfasis que deben acompañarlas. No hay limitacion para el numero de fuentes RSS. Los fondos e iconos deben localizarse en sus carpetas correspondientes y el color debe ser introducido en formato RGB tal como se muestra en el ejemplo.

1.2. Vincular el calendario con tu cuenta Google.
-Para sincronizar el calendario con nuestro calendario google debemos activar la API de google calendar en nuestra cuenta google. Para ello:
     -Acudimos a: https://developers.google.com/calendar/quickstart/python.
     -Clickamos en "Eneable Calendar API" y completamos los pasos que nos piden. Se descargaran 2 archivos llamados "credentials.json" y "token.pickle" que debemos ubicar en la      carpeta "scripts". 
     -Instalamos las librerias necesarias ejecutando el comando que nos dan en nuestro directorio principal: "pip install --upgrade google-api-python-client google-auth-httplib2       google-auth-oauthlib".
     -La primera vez que ejecutemos el programa nos abrira una pestaña solicitandonos que permitamos el acceso del programa a nuestra cuenta google, una vez que aceptemos            habremos terminado este paso.

1.3. Ejecutar el programa al inicio. 
Para ello debemos ubicar el lanzador "simplemirror.desktop" en el directorio /home/"your user"/.config/autostart. Para que funcione correctamente debemos asegurarnos de que tanto "simplemirror.desktop" como "iniciar.sh" poseen permisos de ejecucion. 

1.4. Resolución de pantalla.
El programa deberia visualizarse bien en la mayoria de monitores convencionales. No obstante puede haber secciones que se muestren mal debido al tamaño de las fuentes o las estructuras. Para solucionarlos deberemos localizar en los respectivos archivos css los elementos con tamaño desproporcionado y ajustar su tamaño manualmente. Para ello recomiendo utilizar las herramientas para desarrollador de chromium.



  2. Instalacion del Hadware.
Simple mirror viene preparado para ser utilizado con 3 pulsadores conectados al puerto GPIO (en nuestro caso a los pines X,Z,Y). Dichos botones tendrian las siguientes funciones:
-A. Cambio entre fuentes RSS y temas. (Pin 22 - Modo BCM)
-B. Apagar y encender la pantalla. (Pin 24 - Modo BCM)
-C. Apagar raspberry pi. (Pin 12 - Modo BCM)




  3. Recursos utilizados:
- Librerias javascript Theter y Jquery.
- Fullcalendar.
- Google Calendar API.
- OpenWeatherMap API.
- Animated weather icons from https://github.com/basmilius/weather-icons.
- Algunos fondos de pantalla y otros iconos que obtuve en internet y que tan solo uso como ejemplos de personalización. 

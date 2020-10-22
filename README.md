# simplemirror
Smart Mirror for raspberry Pi written in Python




  1. Instalación del software:

1.1. Configuracion del archivo "variables.xml".
-En este archivo debemos introducir la latitud y longitud geograficas asi como el nombre de la ciudad para la que deseemos consultar el tiempo. Podemos obtener estos datos en https://openweathermap.org/find

-Las distintas fuentes RSS que deseemos mostrar en el apartado de noticias junto con el fondo de pantalla, los iconos y el color de enfasis que deben acompañarlas. No hay limitacion para el numero de fuentes RSS. Los fondos e iconos deben localizarse en sus carpetas correspondientes y el color debe ser introducido en formato RGB tal como se muestra en el ejemplo.

1.2. Vincular el calendario con tu cuenta Google.
- Para sincronizar el calendario con nuestro calendario google debemos activar la API de google calendar en nuestra cuenta google. Para ello:
     -Acudimos a: https://developers.google.com/calendar/quickstart/python.
     -Clickamos en "Eneable Calendar API" y completamos los pasos que nos piden.
     -Instalamos las librerias necesarias ejecutando el comando que nos dan en nuestro directorio principal: "pip install --upgrade google-api-python-client google-auth-httplib2       google-auth-oauthlib".
     - La primera vez que ejecutemos el programa nos abrira una pestaña solicitandonos que permitamos el acceso del programa a nuestra cuenta google, una vez que aceptemos            habremos terminado este paso.

1.3. Ejecutar el programa al inicio. 
Para ello debemos ubicar el lanzador "simplemirror.desktop" en el directorio /home/"your user"/.config/autostart. Para que funcione correctamente debemos asegurarnos de que tanto "simplemirror.desktop" como "iniciar.sh" poseen permisos de ejecucion. 




  2. Instalacion del Hadware.
Simple mirror viene preparado para ser utilizado con un chip MPR121. Si desea usarse dicho chip se deben configurar adecuadamente las comunicaciones I2C. Para esto pueden utilizarse algunas guias de internet: 
- https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c
- https://www.mbtechworks.com/projects/mpr121-capacitive-touch-for-raspberry-pi-project.html

Una vez configuradas las comunicaciones I2C se debe conectar el chip MPR121 al puerto GPIO. En nuestro caso utilizamos como sensores los pines 2,3,4 del chip MPR121 y conectamos el pin IQR al pin 7 de GPIO para detectar cuando hay una pulsacion. Se muestra en el siguiente esquema:
- https://github.com/scottgarner/BeetBox/blob/master/schematic/beetbox.jpg 

No obstante el codigo esta preparado para ser utilizado con 3 pulsadores o botones corrientes conectados a GPIO. Dichos botones tendrian las siguientes funciones:
-A. Cambio entre fuentes RSS y temas.
-B. Apagar y encender la pantalla.
-C. Apagar raspberry pi.




  3. Recursos utilizados:
- Librerias javascript Theter y Jquery.
- Interprete Python para chip MPR121 from https://github.com/scottgarner/BeetBox
- Fullcalendar.
- Google Calendar API.
- OpenWeatherMap API.
- Animated weather icons from https://github.com/basmilius/weather-icons.
- Algunos fondos de pantalla y otros iconos que obtuve en internet y que tan solo uso como ejemplos de personalización. 

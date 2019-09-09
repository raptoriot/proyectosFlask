# proyectosFlask
Varios Proyectos Flask
basico:
  levanta un servidor en el 500o que muestra el mensaje, para correrlo se debe crear la siguiente variable de entorno
  export  FLASK_APP=basico.py
echo $FLASK_APP

  el programa se corre con
  flask run
  ejemplo sacado del curso de platzy
  
  Proyecto BASICO2
  
  al proyecto anterior se agrego la opcion de main, para que comienze solo sin tener que hacer una flask run
  ademas se puede seleccionar el puerto
  
  --archivo main.py 
  ejemplo basado en libro "Mastering Flask Web Development"
  
 APIejemplo1
 (https://blog.nearsoftjobs.com/crear-un-api-y-una-aplicación-web-con-flask-6a76b8bf5383)
 ejemplo para una api, donde en la ruta 127.0.0.1/hello/nombre
 devuelve un get con {
    "Hello": "nombre"
}
ejemplo basico de api-get
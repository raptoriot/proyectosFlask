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
APIejemplo2
ejemplo que devuelve un valor con el metodo GET, el valor se devuelve de segun un diccionario
se ejecuta http://127.0.0.1:5000/valor/alvaro y devuelve
{
    "Hello": "papa"
}

###### APIejemplo3
Codigo con programa que recibe los metodos GET, POST y PUT, sacados de aca
https://dev.to/aligoren/building-basic-restful-api-with-flask-restful-57oh


GET http://127.0.0.1:5000/valor/alvaro
POST http://127.0.0.1:5000/?prueba1=unValor&prueba2=segundovalor
PUT http://127.0.0.1:5000/update/6
(ver evernote con uso de programa Postman para probar)
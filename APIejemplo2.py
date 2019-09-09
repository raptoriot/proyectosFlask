
from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

diccionario={'alvaro':'papa','ximena':'mama','sayen':'hija','pascual':'mascota'}

class Hello(Resource):
    def get(self, name):
        namesalida=buscarTitulo(diccionario,name)

        return {"Hello":namesalida}

api.add_resource(Hello, '/valor/<name>')

def buscarTitulo(dic,nombre):
    salida=dic.get(nombre)
    return salida

if __name__ == '__main__':
    app.run(debug=True)
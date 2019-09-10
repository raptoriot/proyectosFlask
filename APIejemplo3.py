
from flask import Flask
from flask_restful import Resource, Api,reqparse
import mysql.connector


app = Flask(__name__)
api = Api(app)

parser=reqparse.RequestParser()


class Hello(Resource):
    def get(self,name):

        dic=consultasql()
        valor1=dic.get("valor")
        fecha1=dic.get("fecha")
        print(valor1)
        return {"valor":valor1,"fecha":fecha1}

    def post(self):
        print("entro a POST")
        parser.add_argument('prueba', type=str)
        parser.add_argument('prueba2', type=str)
        args = parser.parse_args()

        return {
            'status': True,
            'prueba': '{} added. Good'.format(args['prueba']),
            'prueba2': '{} added. Good'.format(args['prueba2'])
        }

    def put(self, id):
        parser.add_argument('quote', type=str)
        args = parser.parse_args()

        return {
            'id': id,
            'status': True,
            'quote': 'The quote numbered {} was updated.'.format(id)
        }


api.add_resource(Hello,'/' ,'/valor/<name>', '/update/<int:id>')

def consultasql():
    print("genera consulta")
    db = mysql.connector.connect(host="127.0.0.1", user="alvarov", passwd="lata5comprar", db="prueba_appengine",
                                 charset="utf8")
    cur = db.cursor()
    consulta="SELECT valor, fecha FROM datosConsumo ORDER BY id DESC LIMIT 1"
    cur.execute(consulta)
    dic={'valor'}
    for row in cur.fetchall():
        print(str(row[0])+ " "+str(row[1]))
    print(" ")
    dic = {'valor':row[0],'fecha':row[1]}
    #salida=dic.get(nombre)
    return dic




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
   # app.run(debug=True)
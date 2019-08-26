class Config(object):
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG= True
    #SQLALCHEMY_DATABASE_URI = "mysql+pymysql://alvarov:lata5comprar@127.0.0.1:3306/prueba_appengine"
    #SQLALCHEMY_DATABASE_URI = "mysql+pymysql://USER:PASSWORD@/DATABASE?unix_socket=/cloudsql/INSTANCE_CONNECTION_NAME"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://alvarov:lata5comprar@/prueba_appengine?unix_socket=/cloudsql/asistente-180018:southamerica-east1:bd-bsa-chequeo-planta"
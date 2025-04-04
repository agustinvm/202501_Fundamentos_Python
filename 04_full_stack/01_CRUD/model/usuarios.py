from config.mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self. nombre = data['nombre']
        self. email = data['email']
        self. contraseña = data['contraseña']
        self. created_at = data['created_at']
        self. update_at = data['update_at']


    @classmethod
    def get_all(cls):

        query = "SELECT * FROM usuarios;"
        resultados = connectToMySQL().query_db(query)    # Llamamos a función connectToMySQL con el esquema al que te diriges
        
        instancia = []                                               # Creamos una lista vacía para agregar nuestras instancias de mascota
        for dato in resultados:                                # Iteramos sobre los resultados de la base de datos y crear instancias de mascota con cls
               instancia.append( cls(dato) )
       
        return instancia
    
    @classmethod
    def get_data_by_id(cls, id):
         
        query = f"SELECT * FROM usuarios WHERE id = %(id) s;" #Inyección SQL: evitamos que nuestro código sea vulnerable a ataques de inyección SQL
        data = {
             'id' : id
        }
        resultado = connectToMySQL().query_db(query, data) 
        instancia_nueva = cls(resultado[0])
        return instancia_nueva                                         # Creamos una lista vacía para agregar nuestras instancias de mas

    def __str__(self):
         return f"Usuario: {self.id} - {self.nombre} - {self.email}"
    
    def __repr__(self):
         return f"Usuario: {self.id} - {self.nombre} - {self.email}"
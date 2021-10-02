# Conectarse a la bd

psql --host=db --dbname=hello_flask_dev --username=hello_flask

contraseña:
    hello_flask

# Importante

Si se cambia el DDL de la tabla de la base de datos se debe de eliminar la tabla y volver a correr el proyecto.

# Eliminar todas las imagenes

 - docker rmi -f $(docker images -a -q)

# Eliminar todos los contenedores

 - docker rm $(docker ps -a -q)
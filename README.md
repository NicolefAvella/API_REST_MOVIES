# API_REST_MOVIES
Api creada para la gestión de películas y actualización programada     

# Endpoints disponibles:

1. Creación de películas:
  POST  /movie/
  PARAMS: title, description, image, ranking
 
2. Listar películas
  GET  /movie/
 
3. Obtener pelicula
  GET /movie/<int:pk>

4. Borrar pelicula
  DELETE /movie/<int:pk>

5. Calificar película
  PUT /movie/ranking/<int:pk>
  PARAMS: rate

Esta aplicación utiliza autenticación por token
6. POST /token/
   PARAMS: username, password

7. Para la actualización de películas, se consume la API EXTERNA THEMOVIEDB y se utiliza redis, huey para la consulta y actualización diariamente a las 2:00 a.m.
   apt-get install redis-server


Comandos para correr el proyecto:
python manage.py runserver;
python manage.py migrate;
python manage.py run_huey

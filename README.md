# Git4nStats

### Configuraciones iniciales

1. python 3.7
Pagina de descarga: [https://www.python.org/downloads/]()
2. Instalar librerias necesarias
```
pip install -r requirements.txt

```
3. Postgres: puede instalar una maquina local, en nuestro caso usamos docker
descarga de docker: [https://www.docker.com/get-started]()
verificar instalación.ejecutar en la terminal
```
docker version
```
Resultado
```
Client: Docker Engine - Community
 Version:           19.03.8
 API version:       1.40
 Go version:        go1.12.17
 Git commit:        afacb8b
 Built:             Wed Mar 11 01:21:11 2020
 OS/Arch:           darwin/amd64
 Experimental:      false
```
Ya tenemos docker. Ahora descargamos la imagen oficial de postgres

```
docker pull postgres
```
Iniciamos contenedor con la imagen descargada y con las variables iniciales.
```
docker run -d --name aguirre -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -e POSTRGRES_DB=postgres -p 5432:5432 postgres
```
Configuración anterior esta confuguracion esta en el archivo db_util.
sera necesario modificar las variables para su ambiente
```
{'dbname': 'postgres',
 'user': 'postgres',
 'password': 'postgres',
 'host': 'localhost',
 'port': 5432}
```
Despues de verificar que la base de datos esta corriendo se ejecuta el siguiente query sql para la 
creación de la tabla donde persistirarn los datos.

```
CREATE TABLE public.s4n_github (
	id serial NOT NULL,
	created_at timestamp NOT NULL DEFAULT now(),
	user_git varchar NOT NULL,
	gists varchar NULL,
	events varchar NULL
);
```


###Correr aplicación
Subiendo el servidor  
```
python main.py
```
Creando peticiones 
```
test='["fabpot", "andrew", "taylorotwell", "egoist", "HugoGiraudel"]'
res=requests.post(url='http://127.0.0.1:8080/get_users',data=test)
```
###logs
Cada que el servidor se levanta se crea un nuevo log

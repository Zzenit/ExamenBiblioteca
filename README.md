CREANDO UN REPOSITORIO DESDE 0
- Se debe ingresar a la carpeta y abrir el powershell
    . "Archivo" -> Abrir Windows PowerShell -> abrir como administrador.
  
- Se debe crear el ambiente virtual para que las dependencias queden isoladas de otros proyectos:
  . python -m venv myvenv
  . activar el ambiente virtual antes de instalar las dependencias: en myvenv/Scripts ejecutar .\activate
  . actualizar PIP: python -m pip install --upgrade pip
  
-  al crear el archivo requirements.txt al lado de myvenv para indicar las dependencias del actual proyecto.
  Para instalar Django, dentro del archivo requirements.txt registramos Django==4.1.2

-  ejecutamos pip install -r requirements.txt para instalar las dependencias de Django en la carpeta raiz

- dentro del Examenbiblioteca, ejecutar python manage.py runserver


TRAYENDO UN REPOSITORIO CON DJANGO YA INSTALADO
  	. git clone de nuestro repositorio
	. python -m venv myvenv (para recrear el myvenv) dentro del repositorio
	. ir a activar (en myvenv/Scripts) => .\activate
	. pip install -r requirements.txt (en el directorio raiz del repositorio)
	. dentro del Examenbiblioteca, ejecutar python manage.py runserver


 -------------------------------------------
 Ya con python manage.py runserver ejecutado
 - se debe entrar a localhost:8000/index
